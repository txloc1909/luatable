# Lua 5.4 table implementation in Python

Bring Lua's table to the Python world.

## Goals
1. Identical behavior
1. As performance as possible

## Features

```python3
from luatable import Table, pairs, ipairs

t = Table(1, 2, 3, 4, foo="bar", bar="baz")
t[1000] = Table(hello="world")
t.addTwo = lambda x: x + 2

print(t[1])             # 1
print(t.foo)            # bar
print(t["bar"])         # baz
print(t[1000]["hello"]) # world
print(t.addTwo(1))      # 3
print(t["what"])        # None
print(len(t))           # 4

# index by `None` is forbidden
print(t[None])          # None
t[None] = 1             # ValueError: table index is nil

for k, v in ipairs(t):
    print(k, v)         # 1 1
                        # 2 2
                        # 3 3
                        # 4 4

for k, v in pairs(t):
    print(k, v)         # order is not guaranteed, but should look like this:
                        # 1 1
                        # 2 2
                        # 3 3
                        # 4 4
                        # foo bar
                        # bar baz
                        # 1000 table: 0x7fee1d99e260
                        # addTwo <function <lambda> at 0x7fee1d9a39a0
```


## Roadmaps
- [ ] Table manipulation in the Lua Standard Library: `luatable.table`
    - `table.concat`
    - `table.insert`
    - `table.pack`
    - `table.remove`
    - `table.sort`
    - `table.unpack`
- [ ] Support metatables
