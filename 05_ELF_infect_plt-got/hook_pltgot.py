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

# Remove bind now if present
if lief.ELF.DYNAMIC_TAGS.FLAGS in crackme:
    flags = crackme[lief.ELF.DYNAMIC_TAGS.FLAGS]
    flags.remove(lief.ELF.DYNAMIC_FLAGS.BIND_NOW)

if lief.ELF.DYNAMIC_TAGS.FLAGS_1 in crackme:
    flags = crackme[lief.ELF.DYNAMIC_TAGS.FLAGS_1]
    flags.remove(lief.ELF.DYNAMIC_FLAGS_1.NOW)

# Remove RELRO
if lief.ELF.SEGMENT_TYPES.GNU_RELRO in crackme:
    crackme[lief.ELF.SEGMENT_TYPES.GNU_RELRO].type = lief.ELF.SEGMENT_TYPES.NULL


crackme.write("crackme.hooked")
