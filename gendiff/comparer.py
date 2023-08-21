from collections import namedtuple


def compare_data(data1, data2):
    """Output format:
    (val_1st_input, val_2nd_input, status)
    First two fields are field values from the input.
    Third field contains information about the change of values"""
    diff_dict = {}
    ComparisonResult = namedtuple("ComparisonResult", ["val_1st_input",
                                                       "val_2nd_input",
                                                       "status"])
    if isinstance(data1, dict) and isinstance(data2, dict):
        for k1, v1 in data1.items():
            if k1 in data2.keys():
                if isinstance(data2[k1], dict):
                    diff_dict[k1] = compare_data(data1[k1], data2[k1])
                    continue
                diff_dict[k1] = ComparisonResult(v1, data2[k1],
                                                 "UPDATED" if v1 != data2[k1]
                                                 else "UNCHANGED")
            else:
                diff_dict[k1] = ComparisonResult(v1, None, "REMOVED")
        for k2, v2 in data2.items():
            if k2 not in diff_dict.keys():
                diff_dict[k2] = ComparisonResult(None, v2, "ADDED")
    else:
        return ComparisonResult(data1, data2,
                                "UPDATED" if data1 != data2 else "UNCHANGED")
    return dict(sorted(diff_dict.items()))
