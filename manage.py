#!/usr/bin/env python
import os
import sys
from config.environment import SETTINGS_MODULE


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
