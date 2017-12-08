from django.core.validators import URLValidator
from django import forms
import re

_url_prefix = re.compile(r'https?://')


def validate_url(url):
    url_validator = URLValidator()
    transform = url
    if not _url_prefix.match(url):
        transform = 'http://' + url

    try:
        url_validator(transform)
    except:
        raise forms.ValidationError('Invalid URL for this field')
    return url
