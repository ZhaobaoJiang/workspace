 #!/usr/bin/env python2.7
#coding:utf-8

from django import template
from django.utils.safestring import mark_safe
from django.template.base import Node,TemplateSyntaxError

register = template.Library()

@register.simple_tag
def mymethod(v1):
    result = v1 * 1000
    return result