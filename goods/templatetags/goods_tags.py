from django import template
from django.utils.http import urlencode


from goods.models import Categories


register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    # example with other context vars
    # print(context['title'])
    # print(context['slug_url'])
    # print(context['goods'])
    # print([product.name for product in context['goods']])
    query.update(kwargs)
    return urlencode(query)