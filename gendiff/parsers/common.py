import json


def jsonify(v):
    if isinstance(v, bool):
        return json.dumps(v)
    if v is None:
        return json.dumps(v)
    return v


def format_output(f):
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        return r.rstrip("\n")
    return wrapper
