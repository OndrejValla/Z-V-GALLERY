from django.db import models


class Contact(models.Model):
    """ Save a contact message/model in the database """
    class Meta:
        verbose_name_plural = 'Received messages'

    full_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=25, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(max_length=1500, null=False, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
