# ./crackme.hooked XXXXXXXXXXXXXXXXXXXXX
# Hook add
# Damn_YoU_Got_The_Flag
# XXXXXXXXXXXXXXXXXXXXX
# You got it !!
import lief

crackme = lief.parse("crackme.bin")
hook    = lief.parse("hook")

segment_added  = crackme.add(hook.segments[0])

my_memcmp      = hook.get_symbol("my_memcmp")
my_memcmp_addr = segment_added.virtual_address + my_memcmp.value

crackme.patch_pltgot('memcmp', my_memcmp_addr)
crackme.write("crackme.hooked")
