from decimal import Decimal
from django import template

register = template.Library()


def format_float(f):
    s = "{:,f}".format(f)
    if "." not in s:
        return s

    return s.rstrip("0").rstrip(".")


@register.filter
def nanokepler(nanokepler):
    if nanokepler == 0:
        return kepler(0)

    if nanokepler < 1000:
        return "%d nKMW" % nanokepler

    return microkepler(Decimal(nanokepler) / Decimal(1000))


@register.filter
def microkepler(microkepler):
    if microkepler == 0:
        return kepler(0)

    if microkepler < 1000:
        return "%s µKMW" % format_float(microkepler)

    return millikepler(Decimal(microkepler) / Decimal(1000))


@register.filter
def millikepler(millikepler):
    if millikepler == 0:
        return kepler(0)

    if millikepler < 1000:
        return "%s mKMW" % format_float(millikepler)

    return kepler(Decimal(millikepler) / Decimal(1000))


@register.filter
def kepler(kepler):
    return "%s KMW" % format_float(kepler)
