import json


def jsonify(v):
    if isinstance(v, bool):
        return json.dumps(v)
    if v is None:
        return json.dumps(v)
    return v
