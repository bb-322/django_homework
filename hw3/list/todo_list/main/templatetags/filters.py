from django import template

register = template.Library()

@register.filter
def priority_filter(task_list):
    return sorted(task_list, key=lambda x: x['priority'], reverse=True)