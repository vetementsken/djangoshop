from django import template
from shop.models import Category

register = template.Library()


@register.inclusion_tag('categories_posts_tpl.html')
def get_cat():
    categories = Category.objects.all()
    return {"categories": categories}
