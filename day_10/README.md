Here's a quick summary of Day 10:

**Two Types of Loops**
- `while` — repeats as long as a condition is `True`
- `for` — iterates over a sequence (list, tuple, dict, set, string)

**While Loop**
- Stops when condition becomes `False`
- Can have an optional `else` block that runs after the loop ends

**For Loop**
- Works on any iterable: lists, tuples, strings, sets, dicts
- When looping a dict, you get keys by default; use `.items()` to get both key and value
- Also has an optional `else` block that runs when the loop finishes normally

**break & continue**
- `break` — exits the loop immediately
- `continue` — skips the rest of the current iteration and moves to the next

**range()**
- Generates a sequence of numbers: `range(start, end, step)`
- Default start is `0`, default step is `1`; end is exclusive
- e.g. `range(0, 11, 2)` → `[0, 2, 4, 6, 8, 10]`

**Nested Loops**
- A loop inside a loop — useful for multi-level iteration (e.g. looping over a list inside a dict)

**pass**
- A placeholder keyword — does nothing, but prevents syntax errors when a code block is required but empty