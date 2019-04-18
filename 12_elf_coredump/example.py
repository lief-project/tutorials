import lief

# Parse Core file
core = lief.parse("./ELF64_AArch64_core_hello.core")

# Memory State
# ============
segments = core.segments
print("Number of segments {}".format(len(segments)))

for segment in segments:
    print(hex(segment.virtual_address))

# Coredump information
# =====================

# Note File: Relationship between segment and module path
note_file = [n for n in core.notes if n.type_core == lief.ELF.NOTE_TYPES_CORE.FILE]
assert len(note_file) == 1

note_file = note_file.pop().details

for f in note_file:
    print(f)

# PrStatus: Procces state + registers values
for note in core.notes:
    if note.type_core == lief.ELF.NOTE_TYPES_CORE.PRSTATUS:
        details = note.details
        print(details)

        # Print instruction pointer
        print(hex(details[lief.ELF.CorePrStatus.REGISTERS.AARCH64_PC]))
        # or
        print(hex(details.get(lief.ELF.CorePrStatus.REGISTERS.AARCH64_PC)))

# Coredump modification: Changing register value
# ===============================================
note_prstatus = [n for n in core.notes if n.type_core == lief.ELF.NOTE_TYPES_CORE.PRSTATUS][0]
note_prstatus.details[lief.ELF.CorePrStatus.REGISTERS.AARCH64_PC] = 0xDEADC0DE

core.write("/tmp/new.core")






