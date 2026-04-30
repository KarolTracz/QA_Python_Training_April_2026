from types import new_class
from typing import Any

def convert_unsupported_types(obj: dict or int) -> dict:
    """
    Convert all numeric values in a nested dictionary to strings.

    This function recursively traverses the input dictionary and its nested structures
    (lists and dictionaries), converting all numeric values (int and float) to strings.
    Other types of values are left unchanged.

    Args:
    obj (dict): The input dictionary with a nested structure.

    Returns:
    dict: A new dictionary with the same structure as the input, but all numeric values converted to strings.

    Example:
    >>> input_dict = {'a': 1, 'b': [2, 3.14], 'c': {'d': 4, 'e': 'hello'}}
    >>> convert_unsupported_types(input_dict)
    {'a': '1', 'b': ['2', '3.14'], 'c': {'d': '4', 'e': 'hello'}}
    """
    # Your implementation here
    if isinstance(obj, (int, float)):
        return str(obj)
    if isinstance(obj, dict):
        return {k: convert_unsupported_types(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert_unsupported_types(v) for v in obj]
    return obj


sample_obj = {
    'Well': 'hello',
    'my': {
        'test': False,
        'dear': 1,
        'Dante.': [1, 'Please', [35, {'take': 18}, 'your'], 'sit']
    }
}
result = convert_unsupported_types(sample_obj)
print(result)