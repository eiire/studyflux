from django import template

register = template.Library()


@register.filter(name='range')
def _range(number):
    return range(number)


@register.filter(name='add')
def _add(val, numb):
    return val + numb


@register.filter(name='minus')
def _minus(val, numb):
    return val - numb


@register.filter(name='print')
def _print(val):
    print(val)
