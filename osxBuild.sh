#!/bin/bash
rm -rf build dist send.command
pyinstaller send.py -F --hidden-i Cookie  --hidden-i django.template.defaulttags --hidden-i django.template.loader_tags
mv dist/send send.command
rm -rf build dist send.spec
