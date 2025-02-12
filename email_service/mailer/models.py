from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()

    def __unicode__(self):
        return self.email

class Mailing(models.Model):
    subject = models.CharField(max_length=255)
    html_template = models.TextField()
    scheduled_time = models.DateTimeField(null=True, blank=True)
    is_sent = models.BooleanField(default=False)

    def __unicode__(self):
        return self.subject
