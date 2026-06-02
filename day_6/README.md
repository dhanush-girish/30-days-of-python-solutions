Here's a quick summary of Day 6:

**What is a Tuple?**
- Ordered, **immutable** (unchangeable) collection — written with `()`
- Can hold mixed data types; allows duplicates
- Use `len()` to get its length

**Creating a Tuple**
- Empty: `tpl = ()` or `tpl = tuple()`
- With values: `tpl = ('a', 'b', 'c')`

**Accessing & Slicing**
- Same as lists — positive index `tpl[0]`, negative index `tpl[-1]`
- Slicing: `tpl[1:3]`, `tpl[-3:-1]` etc.

**Key Difference from List — Immutability**
- You **cannot** add, remove, or change items directly
- To modify, convert to list → edit → convert back to tuple: `list(tpl)` → `tuple(lst)`

**Available Methods (very few)**
- `count(item)` — counts occurrences
- `index(item)` — finds position
- `+` — joins two tuples into a new one
- `in` — checks membership (returns `True`/`False`)

**Deleting**
- Can't remove a single item; can only delete the entire tuple with `del tpl`