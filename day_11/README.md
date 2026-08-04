Here's a quick summary of Day 11:

**What is a Function?**
- A reusable block of code designed to perform a specific task
- Defined with `def` keyword; only runs when called

**Types of Functions**
- **No parameters** — runs with fixed values inside
- **With parameters** — accepts inputs when called
- **With default parameters** — uses a fallback value if no argument is passed: `def greet(name='Guest'):`
- **With return value** — use `return` to send a result back; without it, the function returns `None`

**Keyword Arguments**
- Pass arguments by name, order doesn't matter: `func(name='Alice', age=30)`

**Arbitrary Arguments**
- `*args` — accepts any number of positional arguments (stored as a tuple)
- `**kwargs` — accepts any number of named/keyword arguments (stored as a dict)
- Can mix both: `def func(team, *args):`

**Dictionary Unpacking**
- Pass a dict as keyword arguments using `**`: `greet(**my_dict)`

**Functions as Parameters**
- Functions can be passed into other functions as arguments — the foundation of higher-order functions:
  ```python
  def do_something(f, x):
      return f(x)
  ```