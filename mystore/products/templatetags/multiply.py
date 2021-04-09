from django import template

register = template.Library()


def mul(val1, val2):
    return val1 * val2


def total(*args):
    l = list(args)
    a = 1
    a *= [b for b in l]
    return a


register.filter("mul", mul)
register.filter("total", total)
