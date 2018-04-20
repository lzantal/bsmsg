from django import template


register = template.Library()


@register.inclusion_tag('bsmsg/bsmsg.html', takes_context=True)
def bsmsg(context):
    return context # not altering context simply use it by returning it
