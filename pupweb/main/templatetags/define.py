from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def to_list(*args):
    return [arg.split(" ") for arg in args]


@register.simple_tag
def set(value):
    return value


@register.simple_tag
def add(mylist, *args):
    mylist = mylist + [arg.split(" ") for arg in args]
    return mylist


@register.simple_tag
def get_current_date(format_string):
    return datetime.now().strftime(format_string)