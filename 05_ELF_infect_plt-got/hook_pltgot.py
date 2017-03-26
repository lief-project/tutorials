# ./crackme.patched XXXXXXXXXXXXXXXXXXXXX
# Hook add
# Damn_YoU_Got_The_Flag
# XXXXXXXXXXXXXXXXXXXXX
# You got it !!
import lief

crackme = lief.parse("crackme.bin")
hook    = lief.parse("hook")

segment           = lief.ELF.Segment()
segment.type      = lief.ELF.SEGMENT_TYPES.LOAD
segment.flag      = lief.ELF.SEGMENT_FLAGS.PF_R | lief.ELF.SEGMENT_FLAGS.PF_W | lief.ELF.SEGMENT_FLAGS.PF_X
segment.data      = hook.segments[0].data # First LOAD segment which holds payload
segment.alignment = 8
segment           = crackme.add_segment(segment, base=0xA0000000, force_note=True)

my_memcmp = next(filter(lambda s : s.name == "my_memcmp", hook.dynamic_symbols))
my_memcmp_addr = segment.virtual_address + my_memcmp.value
crackme.patch_pltgot('memcmp', my_memcmp_addr)
crackme.write("crackme.hooked")
