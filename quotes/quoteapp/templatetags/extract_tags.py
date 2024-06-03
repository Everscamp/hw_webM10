from django import template
from bson.objectid import ObjectId
from ..models import Quote
# from ..connect import db

register = template.Library()


# def author(_id):
#     # author = db.authors.find_one({'_id':ObjectId(_id)})
#     
#     return author['fullname']


# register.filter('author', author)

def tags(quote_tags):
    tags = []
    for i in quote_tags.all():
        tags.append(i)

    return tags

register.filter('tags', tags)