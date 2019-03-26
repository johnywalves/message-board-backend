import datetime
from decimal import Decimal
from sqlalchemy.orm.dynamic import AppenderQuery


def toJSON(object):
    result = {}
    for key in object.__mapper__.c.keys():
        attr = getattr(object, key)
        if attr is not None:
            if isinstance(attr, Decimal):
                result[key] = float(attr)
            elif isinstance(attr, datetime.datetime):
                result[key] = ('{}').format(attr)
            elif isinstance(attr, AppenderQuery):
                elements = []
                for instance in attr:
                    elements.append(instance.toJson())
                result[key] = elements
            else:
                result[key] = attr
    return result


def fromJSON(object, dataJson):
    for key in object.__mapper__.c.keys():
        if (key in dataJson):
            setattr(object, key, dataJson[key])
        else:
            setattr(object, key, None)
    return object


def postJSON(post):
    if post is not None:
        tags = []
        for tag in post.tags:
            tags.append({'name': tag.name})

        comments = []
        for comment in post.comments:
            comments.append({'id': comment.id, 'text': comment.text})

        return {'id': post.id, 'text': post.text, 'likes': post.likes, 'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'), 'tags': tags, 'comments': comments}
    else:
        return {}