# coding=utf-8
from django.db import models


# basic model stuff
##########################################
from django.db.models import Sum
from django.forms import forms
from django.utils.datetime_safe import datetime


class DataManager(models.Manager):

    def get_query_set(self):
        qs = super(DataManager, self).get_query_set()
        return qs.filter(active=True)
        
    def delete(self):
        self.update(active=False)


class AllObjectsManager(models.Manager):

    def deleted(self):
        return self.filter(active=False)


# base model with useful stuff
class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    deleted = models.DateTimeField(editable=False, null=True)

    active = models.BooleanField(default=True, editable=False)

    # access only active data objects
    data = DataManager()
    # access all (including deleted) data (active is false)
    objects = AllObjectsManager()

    class Meta:
        abstract = True
        ordering = ['-created']

    # deleted data is bad - doing it you shouldn't!
    def delete(self, using=None):
        self.active = False
        self.save()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.active:
            self.deleted = None
        else:
            self.deleted = datetime.now()

        super(BaseModel, self).save(force_insert=force_insert, using=using,
                                    update_fields=update_fields)

    def reload_me(self):
        if self.id:
            return self.__class__.objects.get(id=self.id)


class NamedModel(models.Model):
    name = models.CharField('Name', max_length=150)

    class Meta:
        ordering = ['name']
        abstract = True

    def __unicode__(self):
        return self.name

