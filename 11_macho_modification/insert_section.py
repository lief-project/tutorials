import lief

app = lief.parse("./MachO64_x86-64_binary_id.bin")

raw_shell = None
with open("./shell.raw", "rb") as f:
    raw_shell = list(f.read())

__TEXT = app.get_segment("__TEXT")
section = lief.MachO.Section("__shell", raw_shell)
section.alignment = 2
section += lief.MachO.SECTION_FLAGS.SOME_INSTRUCTIONS
section += lief.MachO.SECTION_FLAGS.PURE_INSTRUCTIONS

section = app.add_section(section)
print(section)

app.main_command.entrypoint = section.virtual_address - __TEXT.virtual_address
app.remove_signature()
app.write("./id.modified")




