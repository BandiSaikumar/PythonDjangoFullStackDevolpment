from django import template

register = template.Library()
@register.filter(name = 'cut')
def cut(value, arg):
    """
    It cuts all values of all arguements in string
    """
    return value.replace(arg, '')
# register.filter('cut',cut)