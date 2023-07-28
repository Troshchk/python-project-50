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


def compare_values(v0, v1, v0_set, v1_set):
    if v0 == v1:
        comparison_result = None
    elif v0_set is False:
        comparison_result = f"added with value: {format_string(v1)}"
    elif v1_set is False:
        comparison_result = "removed"
    else:
        v0 = format_string(v0)
        v1 = format_string(v1)
        comparison_result = f"updated. From {v0} to {v1}"
    return comparison_result


def plain_inner(diff_dict, key=''):
    out_str = ""
    for k, v_in in diff_dict.items():
        if not isinstance(v_in, dict):
            v0, v1, v0_set, v1_set = v_in
            comparison_result = compare_values(v0, v1, v0_set, v1_set)
            if comparison_result is not None:
                out_str += PATTERN_PLAIN.format(f"{key}.{k}".lstrip("."),
                                                comparison_result)
        else:
            comparison_result = plain_inner(v_in, key=f"{key}.{k}")
            out_str += comparison_result
    return out_str


def plain(diff_dict):
    return format_output(plain_inner)(diff_dict)
