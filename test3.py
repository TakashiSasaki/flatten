simple_dict = {
    'key1': None,
    'key2': True,
    'key3': 1.234
}
from pprint import pprint
from flatten_pnv import flatten_pnv
pprint(flatten_pnv(simple_dict))