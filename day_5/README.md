Here's a quick summary of Day 5:

**What is a List?**
- Ordered, mutable (changeable) collection that allows duplicate items
- Can hold mixed data types: strings, numbers, booleans, dicts, etc.
- Created with `[]` or `list()`; use `len()` for size

**Accessing Items**
- Positive index: `fruits[0]` → first item
- Negative index: `fruits[-1]` → last item
- Unpacking: `a, b, *rest = lst` — use `*` to capture remaining items

**Slicing**
- `lst[1:3]` — items from index 1 to 2
- `lst[::-1]` — reverses the list
- `lst[::2]` — every 2nd item

**Modifying**
- Change item by index: `lst[0] = 'new'`
- Check membership: `'item' in lst`

**Adding Items**
- `append(item)` — adds to the end
- `insert(index, item)` — inserts at a specific position

**Removing Items**
- `remove(item)` — removes first occurrence
- `pop()` / `pop(index)` — removes last or specific index
- `del lst[index]` — removes by index or range; `del lst` deletes the whole list
- `clear()` — empties the list

**Other Useful Methods**
- `copy()` — makes a true copy (not just a reference)
- `+` or `extend()` — joins two lists
- `count(item)` — counts occurrences
- `index(item)` — finds position
- `reverse()` — reverses in place
- `sort()` — sorts ascending/descending (modifies original); `sorted()` — returns a new sorted list