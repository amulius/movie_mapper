from django import template

register = template.Library()



@register.filter
def longTitle(movie):
        return movie['long imdb title']
