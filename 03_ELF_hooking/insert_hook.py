#!/usr/bin/env python3

# Description
# -----------
# Hook the 'exp' function from the standard math library (libm)

import lief

libm = lief.parse("/usr/lib/libm.so.6")
hook = lief.parse("hook")

offset, size = libm.insert_content(hook.segments[0].content)

print("Hook inserted at offset: 0x{:06x}".format(offset))

exp_symbol = next(filter(lambda e : e.name == "exp", libm.exported_symbols))
hook_symbol = next(filter(lambda e : e.name == "hook", hook.exported_symbols))

exp_symbol.value = offset + hook_symbol.value
libm.write("libm.so.6")
