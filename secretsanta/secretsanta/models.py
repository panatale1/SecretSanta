from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50, blank=True, null=True)
    address_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    extension = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class SantaRelation(models.Model):
    giver = models.ForeignKey(Person, related_name='santa')
    recipient = models.ForeignKey(Person)
    created = models.DateTimeField(auto_now_add=True)


class ExcludedPeople(models.Model):
    this_person = models.ForeignKey(Person, related_name='excluded')
    excluded = models.ForeignKey(Person)
    created = models.DateTimeField(auto_now_add=True)
