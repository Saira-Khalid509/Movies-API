from django import template
from django.core.paginator import Paginator

register = template.Library()

@register.simple_tag(takes_context=True)
def paginate(context, object_list, per_page):
    paginator = Paginator(object_list, per_page)
    page = context['request'].GET.get('page')
    return paginator.get_page(page)

