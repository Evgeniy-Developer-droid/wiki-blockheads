from django.db import models
from django.forms import fields

import bleach
from django_summernote.settings import ALLOWED_TAGS, ATTRIBUTES, STYLES
from django_summernote.widgets import SummernoteWidget


class SummernoteTextFormField(fields.CharField):

    """Custom function to fix a bug in the library django-summme"""

    def __init__(self, *args, **kwargs):
        kwargs.update({'widget': SummernoteWidget()})
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        value = super().to_python(value)
        return bleach.clean(
            value, tags=ALLOWED_TAGS, attributes=ATTRIBUTES, css_sanitizer=STYLES)