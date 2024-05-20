simple_dict = {
    'key1': None,
    'key2': True,
    'key3': 1.234
}
from pprint import pprint
from flatjson import flatten
pprint(flatten(simple_dict))