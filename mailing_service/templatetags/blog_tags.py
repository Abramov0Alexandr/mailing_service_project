from random import sample
from django import template
from blog.models import Blog
from mailing_service.models import MailingSettings, Customers


register = template.Library()


@register.simple_tag()
def total_mailing_number():
    return MailingSettings.objects.count()


@register.simple_tag()
def active_mailing_number():
    return MailingSettings.objects.filter(sending_status='active').count()


@register.simple_tag()
def unique_customers_number():
    return Customers.objects.distinct().count()


@register.filter()
def upload_media(image):
    if image:
        return f'/media/{image}'


@register.simple_tag()
def get_random_articles():
    articles = Blog.objects.all()

    if articles.count() >= 3:
        random_articles = sample(list(articles), 3)
    else:
        random_articles = articles

    return random_articles
