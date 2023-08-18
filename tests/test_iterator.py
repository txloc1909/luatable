from luatable import Table, pairs, ipairs


def test_iterator():
    t = Table()
    t[-1] = "y"
    t[0] = "z"
    t[1] = "a"
    t[3] = "b"
    t[2] = "c"
    t[4] = "d"
    t[6] = "e"
    t["hello"] = "world"

    ipairs_output = tuple(ipairs(t))
    pairs_output = tuple(pairs(t))

    # numeric order of keys is guaranteed in `ipairs`
    assert ipairs_output == ((1, "a"), (2, "c"), (3, "b"), (4, "d"))

    # `pairs` guarantee no order, so just check if output exists
    assert (1, "a") in pairs_output
    assert (2, "c") in pairs_output
    assert (3, "b") in pairs_output
    assert (4, "d") in pairs_output
    assert (0, "z") in pairs_output
    assert (6, "e") in pairs_output
    assert ("hello", "world") in pairs_output
    assert (-1, "y") in pairs_output
