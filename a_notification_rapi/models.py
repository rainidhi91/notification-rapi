from django.db import models
from uuid import uuid4


type_choices = (
    ("email", "email"),
    ("sms", "sms"),
    ("simple", "simple"),
    ("in_app", "in_app"),
)


class MailTemplate(models.Model):
    name = models.CharField(max_length=200)
    html = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Notification(models.Model):
    id = models.UUIDField(default = uuid4, primary_key = True, editable = False)
    scheduled = models.DateTimeField(blank = True, null = True)
    subject = models.CharField(max_length = 150)
    message = models.TextField(blank=True, null=True)
    type = models.CharField(max_length = 20, choices = type_choices)
    sent_date_time = models.DateTimeField(blank = True, null = True)
    email = models.EmailField(blank = True, null = True)
    from_email = models.EmailField(blank = True, null = True)
    template = models.ForeignKey(MailTemplate, on_delete = models.SET_NULL, blank = True, null = True)
    use_template = models.BooleanField(default=False)
    created_by = models.UUIDField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.subject}"