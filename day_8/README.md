Here's a quick summary of Day 8:

**What is a Dictionary?**
- Unordered, mutable collection of **key: value** pairs
- Created with `{}` or `dict()`; values can be any data type (string, list, bool, even another dict)
- Use `len()` to get the number of pairs

**Accessing Items**
- By key: `dct['key1']` — raises an error if key doesn't exist
- Safer: `dct.get('key1')` — returns `None` if key doesn't exist (no error)
- Nested access: `dct['address']['street']`

**Adding & Modifying**
- Add: `dct['new_key'] = 'value'`
- Modify: `dct['existing_key'] = 'new_value'`

**Checking Keys**
- `'key' in dct` → returns `True` or `False`

**Removing Items**
- `pop('key')` — removes item by key
- `popitem()` — removes the last item
- `del dct['key']` — removes item by key
- `clear()` — empties the dictionary; `del dct` — deletes it entirely

**Useful Methods**
- `copy()` — makes a true copy (avoids mutating the original)
- `keys()` — returns all keys as a list
- `values()` — returns all values as a list
- `items()` — returns all key-value pairs as a list of tuples