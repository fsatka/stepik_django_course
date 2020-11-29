from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def comma_to_dot(value):
    return value.replace(",", " • ")
