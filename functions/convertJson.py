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
