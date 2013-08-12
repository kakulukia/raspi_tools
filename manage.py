#!/usr/bin/env python
import os
import sys

sys.path.append('/home/andy/projects/raspi_tools/')
sys.path.append('/home/andy/.virtualenvs/raspi_tools/lib/python2.7/site-packages/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "raspie_tools.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
