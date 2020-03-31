#!/usr/bin/env python
import os
import sys

SRC = os.path.abspath("src")
sys.path.insert(0, SRC)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rapidpro_community_portal.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
