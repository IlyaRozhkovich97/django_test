import datetime
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


# Создание тега
@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


# Создание фильтра
@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = "<strong>%s</strong>%s" % (esc(first), esc(other))
    return mark_safe(result)


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'

    return 'holder.js/100px225?theme=thumb&bg=55595c&fg=eceeef&text=None'