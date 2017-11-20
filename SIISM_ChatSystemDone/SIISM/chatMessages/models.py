from django.db import models
from userena.utils import user_model_label

class User(models.Model):
    user = models.OneToOneField(user_model_label)

class Message(models.Model):
	"""
	Model to capture messages. 'Sender' and 'Recipient' will
	be automatically filled in when form is filled in. 
	"""
	sender = models.ForeignKey(user_model_label, related_name='sender', editable=False)
	recipient = models.ForeignKey(user_model_label, related_name='recipient', editable=False)
	text = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
