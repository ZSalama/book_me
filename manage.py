#!/usr/bin/env python

import os
import sys

def main():
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
	try:
		from django.core.management import execute_from_command_line
	except ImportError as exc:
		raise ImportError(
			"could not import django. are you sure its insalled?  "
			"and available in PYTHONPATH environment "
			"did you forget to activate a virtual environment "
		) from exc
	execute_from_command_line(sys.argv)

if __name__ == '__main__':
	main()
