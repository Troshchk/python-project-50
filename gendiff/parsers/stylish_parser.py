from .common import jsonify, format_output

NEW_LEVEL = "    "
PATTERN = "{}{}{}: {}"


def compare_values(v0, v1, v0_set, v1_set):
    if v0 == v1:
        comparison_result = ["  "]
        vals = [v0]
    elif v0_set is False:
        comparison_result = ["+ "]
        vals = [v1]
    elif v1_set is False:
        comparison_result = ["- "]
        vals = [v0]
    else:
        comparison_result = ["- ", "+ "]
        vals = [v0, v1]
    return comparison_result, vals


def create_dict_structure(input_dict, indent, addition="  "):
    out_str_from_dict = "{\n"
    for k, v in input_dict.items():
        if not isinstance(v, dict):
            value = v
        else:
            value = create_dict_structure(v, indent + NEW_LEVEL)
        out_str_from_dict += PATTERN.format(indent, addition, k, value)
        out_str_from_dict += "\n"
    out_str_from_dict += f"{indent.replace('  ', '', 1)}"
    out_str_from_dict += "}"
    return out_str_from_dict


def stylish_inner(diff_dict, indent="  ", out_str=""):
    out_str += "{\n"
    for k, v_in in diff_dict.items():
        if not isinstance(v_in, dict):
            v0, v1 = [v if isinstance(v, dict) else
                      jsonify(v) for v in
                      [v_in.val_1st_input, v_in.val_2nd_input]]
            v0_set, v1_set = v_in.exists_in_1st_input, v_in.exists_in_2nd_input
            comparison_result, vals = compare_values(v0, v1, v0_set, v1_set)
            vals = [create_dict_structure(v, indent=indent + NEW_LEVEL)
                    if isinstance(v, dict) else v for v in vals]
            for i in zip(comparison_result, vals):
                comparison_result, value = i[0], i[1]
                out_str += PATTERN.format(indent, comparison_result, k, value)
                out_str += "\n"
        else:
            comparison_result = "  "
            value = stylish_inner(v_in, out_str='', indent=indent + NEW_LEVEL)
            out_str += PATTERN.format(indent, comparison_result, k, value)
    out_str += f"{indent.replace('  ', '', 1)}"
    out_str += "}\n"
    return out_str


def stylish(diff_dict):
    return format_output(stylish_inner)(diff_dict)
