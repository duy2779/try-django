from django.db.models.signals import post_save
from django.contrib.auth.models import User
from customers.models import Customer
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        #add group to user
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        #create customer for that username
        Customer.objects.create(user=instance, name=instance.username)
        print('created user')
