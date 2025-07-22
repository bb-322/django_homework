from django import template

register = template.Library()

@register.inclusion_tag('people_list.html')
def tag(people):
    return {'people': people}