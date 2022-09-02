from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def set(value):
    return value


@register.simple_tag
def get_current_date(format_string):
    return datetime.now().strftime(format_string)