from django import template

register = template.Library()


def authors(quote_authors):
    return ''.join([str(fullname) for fullname in quote_authors.all()])


register.filter('authors', authors)