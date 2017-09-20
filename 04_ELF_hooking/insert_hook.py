#!/usr/bin/env python3

# Description
# -----------
# Hook the 'exp' function from the standard math library (libm)

import lief

libm = lief.parse("/usr/lib/libm.so.6")
hook = lief.parse("hook")

segment_added = libm.add(hook.segments[0])

print("Hook inserted at VA: 0x{:06x}".format(segment_added.virtual_address))

exp_symbol  = libm.get_symbol("exp")
hook_symbol = hook.get_symbol("hook")

exp_symbol.value = segment_added.virtual_address + hook_symbol.value

libm.write("libm.so.6")
