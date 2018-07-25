from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name')
    last_name = models.CharField(max_length=128, verbose_name='Last Name')
    birthdate = models.DateField(verbose_name='Date of birth')
    bio = models.TextField(verbose_name='Bio')
    contacts = models.IntegerField(verbose_name='Contacts')
    jabber_id = models.CharField(max_length=128, verbose_name='Jabber: JID')
    skype_id = models.CharField(max_length=256, verbose_name='Skype: id')
    other_contacts = models.TextField(verbose_name='Other Contacts')

    def __str__(self):
        return self.name
