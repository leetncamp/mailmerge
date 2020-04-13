#!/bin/bash
rm -rf build dist send.command
pyinstaller send.py -F --hidden-i Cookie  --hidden-i django.template.defaulttags --hidden-i django.template.loader_tags --hidden-import pkg_resources.py2_warn 
mv dist/send send.command
rm -rf build dist send.spec
