from .serializers import NotificationSerializer
from a_notification_rapi.models import Notification
from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from celery.decorators import task
from django.utils import timezone
from rest_framework import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import Template, Context


@task
def send_notification(id, email, from_email, user_data):

    instance = Notification.objects.filter(id = id).first()

    if instance and instance.type == "email":

        if instance.use_template:
            template = Template(instance.template.html)

            context = Context({
                "instance": instance,
                "user_data" : user_data,
            })

            html_content = template.render(context)
            text_content = strip_tags(html_content)

            # create the email, and attach the HTML version as well.
            msg = EmailMultiAlternatives(instance.subject, text_content, from_email, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        else:

            send_mail(
                instance.subject,
                instance.message,
                from_email,
                [email],
                fail_silently=False,
            )

        # print(f"Email will sent to {email}")


class NotificationListCreateAPIView(ListCreateAPIView):
    serializer_class = NotificationSerializer


    def perform_create(self, serializer):

        if serializer.validated_data.get("scheduled") and not serializer.validated_data.get("scheduled") > timezone.now():
            raise serializers.ValidationError("Scheduled must be in future.")

        if not serializer.validated_data.get("email") and not self.request.user.is_authenticated:
            raise serializers.ValidationError("Email Field is Required.")
        
        if self.request.user.is_authenticated:
            instance = serializer.save(created_by = self.request.user.id)
        else:
            instance = serializer.save()

        from_email = settings.EMAIL_HOST_USER if not serializer.validated_data.get("from_email") else serializer.validated_data.get("from_email")

        print(from_email)

        user_data = {}

        if self.request.user.is_authenticated:
            user_data = {
                "id" : self.request.user.id,
                "roles" : self.request.user.roles,
                "email" : self.request.user.email,
                "company" : self.request.user.company,
            }

        if serializer.validated_data.get("scheduled"):

            send_notification.apply_async([instance.id, self.request.user.email if not instance.email else instance.email, from_email, user_data,], eta = serializer.validated_data.get("scheduled"))
        
        else:

            send_notification.delay(instance.id, self.request.user.email if not instance.email else instance.email, from_email, user_data)


    def get_queryset(self):
        if self.request.user.is_authenticated:
        
           return Notification.objects.filter(created_by = self.request.user.id)
        
        else:
            return []