# coding=utf-8
from datetime import date
from django.core.management.base import BaseCommand

import requests
import re
from tools.models import IPStatEntry


class Command(BaseCommand):
    """ records the current ip address """

    def handle(self, *args, **options):

        def get_ip_from_dyn_dns():
            response = requests.get('http://checkip.dyndns.com/')
            ips = re.findall(r'\d+\.\d+\.\d+\.\d+', response.content)

            if ips:
                return ips[0]
            return None

        def get_ip_from_42_pl():
            response = requests.get('http://ip.42.pl/short')
            ips = re.findall(r'\d+\.\d+\.\d+\.\d+', response.content)

            if ips:
                return ips[0]
            return None

        def get_ip_from_whatsmyip_de():
            response = requests.get('http://whatsmyip.de/')
            ips = re.findall(r'\d+\.\d+\.\d+\.\d+', response.content)

            if ips:
                return ips[0]
            return None

        def get_ip_from_httpbin_org():

            response = requests.get('http://httpbin.org/ip')
            return response.json()['origin']

        functions = [
            get_ip_from_httpbin_org,
            get_ip_from_42_pl,
            get_ip_from_dyn_dns,
            get_ip_from_whatsmyip_de,
        ]
        ip = index = 0
        while not ip and index < 5:
            ip = functions[0]()
            index += 1
            if ip:
                break

        if not IPStatEntry.data.filter(recorded_ip_address=ip, created__gte=date.today()).exists():
            entry = IPStatEntry.data.create(recorded_ip_address=ip)
