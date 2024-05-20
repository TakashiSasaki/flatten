def flatten(value, path='', result=None):
    """
    辞書、リスト、タプル、および単純なデータ型（文字列、浮動小数点数、整数、None、ブール値）からなる
    入れ子になったデータ構造を、元の構造内の値へのパスを表すキー、リーフの名前（またはリスト/タプルのインデックス）、
    および値の3要素のタプルのリストにフラット化します。

    パスはスラッシュ（/）を使用して辞書のキーを区切り、リストやタプルのインデックスはそのまま整数として格納されます。

    パラメータ:
    value: フラット化する入れ子になったデータ構造。dict、list、tuple、または単純なデータ型が可能。
    path (str, オプション): 再帰的なトラバーサル中の現在のパス。デフォルトは空の文字列。
    result (list, オプション): キー、リーフの名前（またはインデックス）、および値のペアのアキュムレータ。デフォルトはNoneで、新しいリストが作成されます。

    戻り値:
    list: 各タプルが元のデータ構造からのパス、リーフの名前（またはインデックス）、および対応する値を含む3要素のタプルのリスト。

    例外:
    TypeError: 要素のデータ型がサポートされていない場合に発生。

    例:
    >>> flatten({"a": 1, "b": {"c": 2, "d": [3, 4]}})
    [('', 'a', 1), ('b', 'c', 2), ('b', 'd', 3), ('b', 'd', 4)]
    >>> flatten([1, [2, 3], {"a": 4}])
    [('', 0, 1), ('0', 0, 1), ('0', 1, 2), ('1', 'a', 4)]
    """
    if result is None:
        result = []
    if isinstance(value, (str, float, int, type(None), bool)):
        leaf_name = path.split('/')[-1] if '/' in path else path
        result.append((path, leaf_name, value))
    elif isinstance(value, (list, tuple)):
        for index, item in enumerate(value):
            flatten(item, path, result)
            leaf_name = index
            result.append((path, leaf_name, item))
    elif isinstance(value, dict):
        for key, val in value.items():
            new_path = f'{path}/{key}' if path else key
            flatten(val, new_path, result)
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
