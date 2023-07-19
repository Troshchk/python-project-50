import json

class NotSet:
    """A class to distinguish null from jsom/yaml from None meaning the value
    does not exist in the input """
    isset = False


def jsonify(v):
    if isinstance(v, bool):
        return json.dumps(v)
    if v is None:
        return json.dumps(v)
    return v
