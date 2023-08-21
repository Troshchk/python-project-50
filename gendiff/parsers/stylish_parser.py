from .common import jsonify, format_output

NEW_LEVEL = "    "
PATTERN = "{}{}{}: {}"


PADDING_RESULT_MAPPING = {
    "REMOVED": ["- "],
    "ADDED": ["+ "],
    "UPDATED": ["- ", "+ "],
    "UNCHANGED": ["  "]
}


VALUES_FOR_PARSING = {
    "REMOVED": lambda x: [x.val_1st_input],
    "ADDED": lambda x: [x.val_2nd_input],
    "UPDATED": lambda x: [x.val_1st_input, x.val_2nd_input],
    "UNCHANGED": lambda x: [x.val_1st_input]
}


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
    for k, comparison in diff_dict.items():
        if not isinstance(comparison, dict):
            status = comparison.status
            padding_result = PADDING_RESULT_MAPPING[status]
            vals = VALUES_FOR_PARSING[status](comparison)
            vals = [v if isinstance(v, dict) else
                    jsonify(v) for v in vals]
            vals = [create_dict_structure(v, indent=indent + NEW_LEVEL)
                    if isinstance(v, dict) else v for v in vals]
            for parsed in zip(padding_result, vals):
                padding_result, value = parsed[0], parsed[1]
                out_str += PATTERN.format(indent, padding_result, k, value)
                out_str += "\n"
            continue
        padding_result = "  "
        value = stylish_inner(comparison, out_str='',
                              indent=indent + NEW_LEVEL)
        out_str += PATTERN.format(indent, padding_result, k, value)
    out_str += f"{indent.replace('  ', '', 1)}"
    out_str += "}\n"
    return out_str


def stylish(diff_dict):
    return format_output(stylish_inner)(diff_dict)
