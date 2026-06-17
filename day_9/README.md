Here's a quick summary of Day 9:

**What are Conditionals?**
- Control the flow of execution based on whether a condition is `True` or `False`
- Python uses `if`, `elif`, and `else` keywords; indentation is mandatory

**if**
- Runs a block only if the condition is `True`
- `if a > 0: print('positive')`

**if…else**
- Runs the `if` block if `True`, otherwise runs the `else` block

**if…elif…else**
- Used for multiple conditions; checks each one in order, runs the first matching block
- `else` is the fallback if none match

**Shorthand (Ternary)**
- One-liner: `print('positive') if a > 0 else print('negative')`

**Nested Conditions**
- An `if` inside another `if` — useful for multi-level checks
- Can often be replaced with logical operators for cleaner code

**Logical Operators in Conditions**
- `and` — both conditions must be `True`: `if a > 0 and a % 2 == 0:`
- `or` — at least one must be `True`: `if user == 'admin' or access_level >= 4:`