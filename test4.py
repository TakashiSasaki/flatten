
complex_data = {
    'integer': 42,
    'float': 3.14159,
    'string': "Hello, world!",
    'dict': {
        'nested_integer': 100,
        'nested_list': [1, 2, 3, ['sublist', {'subdict': 'value'}]],
        'empty_dict': {},
    },
    'list': [0, [1, 2], ('tuple', {'nested_dict_in_tuple': {'nested_key': 'nested_value'}})],
    'empty_list': [],
    'special_chars': {
        'key_with_space': 'value',
        'key-with-dash': 'another value',
        '@special!#$%^&*()': 'special value'
    },
    'none_value': None,
    'boolean': True
}





from pprint import pprint
from flatjson import flatten

if __name__ == "__main__":
    pprint(flatten(complex_data))

