# coding=utf-8
from django.db import models

from core.models import BaseModel


class IPStatEntry(BaseModel):
    recorded_ip_address = models.IPAddressField()
