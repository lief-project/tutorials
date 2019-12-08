#!/usr/bin/env python3

# Description
# -----------
# Hook the 'cos' function from the standard math library (libm)
import lief

libm = lief.parse("/usr/lib/libm.so.6")
hook = lief.parse("hook")

cos_symbol  = libm.get_symbol("cos")
hook_symbol = hook.get_symbol("hook")

code_segment = hook.segment_from_virtual_address(hook_symbol.value)
segment_added = libm.add(code_segment)

print("Hook inserted at VA: 0x{:06x}".format(segment_added.virtual_address))

# Offset of the function 'hook' within the CODE segment
hook_offset = hook_symbol.value - code_segment.virtual_address
new_addr    = segment_added.virtual_address + hook_offset
print(f"Change {cos_symbol.name}!{cos_symbol.value:x} -> {cos_symbol.name}!{new_addr:x}")
cos_symbol.value = new_addr
libm.write("libm.so.6")
