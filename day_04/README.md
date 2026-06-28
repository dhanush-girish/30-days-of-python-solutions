Here's a quick summary of Day 4:

**Creating Strings**
- Strings use single, double, or triple quotes; triple quotes allow multiline strings
- `len()` returns the length of a string

**String Concatenation**
- Join strings using `+` e.g. `first_name + ' ' + last_name`

**Escape Sequences**
- `\n` new line, `\t` tab, `\\` backslash, `\'` / `\"` quotes

**String Formatting (3 ways)**
- Old style: `'I am %s, age %d' % (name, age)`
- `str.format()`: `'I am {}, age {}'.format(name, age)`
- f-strings (recommended, Python 3.6+): `f'I am {name}, age {age}'`

**Strings as Sequences**
- Characters can be unpacked into variables: `a, b, c = 'abc'`
- Access by index: `str[0]` (first), `str[-1]` (last)
- Slicing: `str[0:3]`, reverse: `str[::-1]`, skip: `str[0:6:2]`

**Key String Methods**
- Case: `upper()`, `lower()`, `capitalize()`, `title()`, `swapcase()`
- Search: `find()`, `rfind()`, `index()`, `rindex()`, `count()`
- Check: `startswith()`, `endswith()`, `isalpha()`, `isdigit()`, `isnumeric()`, `islower()`, `isupper()`, `isidentifier()`
- Modify: `replace()`, `split()`, `strip()`, `join()`