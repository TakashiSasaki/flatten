def flatten(value, path='', result=None):
    """
    Flattens a nested data structure consisting of dictionaries, lists, tuples, and simple data types
    (strings, floats, integers, None, and booleans) into a list of key-value pairs where keys represent
    the path to the value in the original structure.

    The paths use slashes (/) to separate dictionary keys and hashes (#) to indicate indices within lists or tuples.

    Parameters:
    value: The nested data structure to flatten. It can be a dict, list, tuple, or a simple data type.
    path (str, optional): The current path in the recursive traversal. Defaults to an empty string.
    result (list, optional): The accumulator for the key-value pairs. Defaults to None, where a new list is created.

    Returns:
    list: A list of tuples where each tuple contains a path and the corresponding value from the original data structure.

    Raises:
    TypeError: If the data type of an element is not supported.

    Examples:
    >>> flatten({"a": 1, "b": {"c": 2, "d": [3, 4]}})
    [('a', 1), ('b/c', 2), ('b/d#0', 3), ('b/d#1', 4)]
    >>> flatten([1, [2, 3], {"a": 4}])
    [('#0', 1), ('#1#0', 2), ('#1#1', 3), ('#2/a', 4)]
    """
    if result is None:
        result = []
    if isinstance(value, (str, float, int, type(None), bool)):
        result.append((path, value))
    elif isinstance(value, (list, tuple)):
        for index, item in enumerate(value):
            flatten(item, f'{path}#{index}' if path else f'#{index}', result)
    elif isinstance(value, dict):
        for key, val in value.items():
            flatten(val, f'{path}/{key}' if path else key, result)
    else:
        raise TypeError(f"Unsupported data type: {type(value)}")
    return result

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


if __name__ == "__main__":
    print(flatten(complex_data))
    print(flatten("simple string"))
    print(flatten(None))
