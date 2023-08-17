from .common import jsonify, format_output


PATTERN_PLAIN = "Property '{}' was {}\n"


def format_string(v):
    if isinstance(v, str):
        return f"'{v}'"
    if isinstance(v, dict):
        return "[complex value]"
    if isinstance(v, bool) or v is None:
        return jsonify(v)
    return v


def parse_values(v0, v1, status):
    if status == "UNCHANGED":
        parsing_result = None
    elif status == "ADDED":
        parsing_result = f"added with value: {format_string(v1)}"
    elif status == "REMOVED":
        parsing_result = "removed"
    elif status == "UPDATED":
        v0 = format_string(v0)
        v1 = format_string(v1)
        parsing_result = f"updated. From {v0} to {v1}"
    return parsing_result


def plain_inner(diff_dict, key=''):
    out_str = ""
    for k, comparison in diff_dict.items():
        if not isinstance(comparison, dict):
            parsing_result = parse_values(comparison.val_1st_input,
                                          comparison.val_2nd_input,
                                          comparison.status)
            if parsing_result is not None:
                out_str += PATTERN_PLAIN.format(f"{key}.{k}".lstrip("."),
                                                parsing_result)
        else:
            parsing_result = plain_inner(comparison, key=f"{key}.{k}")
            out_str += parsing_result
    return out_str


def plain(diff_dict):
    return format_output(plain_inner)(diff_dict)
