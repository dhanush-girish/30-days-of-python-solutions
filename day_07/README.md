Here's a quick summary of Day 7:

**What is a Set?**
- Unordered, unindexed collection of **unique** items — no duplicates allowed
- Created with `{}` or `set()`; use `set()` for empty (not `{}` — that creates a dict)
- Items can't be accessed by index; use loops instead
- Use `in` to check membership

**Adding & Removing**
- `add(item)` — adds one item
- `update([items])` — adds multiple items
- `remove(item)` — removes item, raises error if not found
- `discard(item)` — removes item, no error if missing
- `pop()` — removes a random item
- `clear()` — empties the set; `del st` — deletes it entirely

**Converting**
- `set(list)` → removes duplicates automatically, great for deduplication

**Set Operations (Math style)**
- `union()` or `|` — all items from both sets
- `intersection()` or `&` — only items common to both
- `difference()` or `-` — items in one set but not the other
- `symmetric_difference()` or `^` — items in either set, but **not** in both
- `issubset()` — checks if one set is inside another
- `issuperset()` — checks if one set contains another
- `isdisjoint()` — checks if two sets share no common items