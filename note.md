## Lua value representation
- 8 basic types: `nil`, `boolean`, `number`, `string`, `table`, `function`, `userdata`, `thread`
- `number`: double-precision floating-point number
- `table`: associative array, can be indexed by any value (except `nil`)
- `userdata`: pointers to user memory blocks
    - `heavy`: blocks are allocated by Lua, subject to GC
    - `light`: blocks are allocated and freed by user
- `thread`: coroutine

## Table in Lua 5.0
- Hybrid datastructure: a hash part & an array part
- Table automatically & dynamically adapt the two parts
    - Array part tries to store values corresponding to integer key from 1 to some limit `n`
    - Non-integer & integer keys outside the array range are stores in hash part
- Size of the array part is the largest `n` such that:
    1. At least half the slots between 1 and `n` are in use, and
    1. There is at least one used slot between `n/2 + 1` and `n`
- Computed new size -> create new parts -> re-insert elements for old parts
- Hash part uses a mix of chained scatter table with Brent's variation.
    - Load factor can be 100% without performance penalties
    - For now, just use Python `dict`
