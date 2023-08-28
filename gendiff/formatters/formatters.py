from .stylish_formatter import stylish
from .plain_formatter import plain
from .json_fomatter import json_parser

FORMATTERS = {
    "stylish": stylish,
    "plain": plain,
    "json": json_parser
}
