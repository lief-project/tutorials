import lief

title = "LIEF is awesome\0"
data  =  list(map(ord, title))

code = [
        0x6a, 0x00,                   # push 0               ; hWnd
        0x68, 0x00, 0x80, 0x40, 0x00, # push 0x408000        ; Title
        0x8b, 0x4d, 0x0c,             # mov ecx, [ebp + 0xC] ; Message
        0x51,                         # push ecx             ;
        0x6a, 0x00,                   # push 0               ; MB_OK
        0xb8, 0x3c, 0x92, 0x40, 0x00, # mov eax, 0x40923C    ; MessageBoxA address
        0xff, 0x10,                   # call [eax]           ; MessageBoxA(hWnd, Message, Title, MB_OK)
        0x6a, 0x00,                   # push 0               ; exit value
        0xb8, 0x34, 0x92, 0x40, 0x00, # mov eax, 0x409234    ; ExitProcess address
        0xff, 0x10,                   # call [eax]           ; ExitProcess(0)
        0xc3,                         # ret                  ; Never reached
        ]

# Create a '.text' section which will contain the hooking code
section_text                 = lief.PE.Section(".htext")
section_text.content         = code
section_text.virtual_address = 0x7000
section_text.characteristics = lief.PE.SECTION_CHARACTERISTICS.CNT_CODE | lief.PE.SECTION_CHARACTERISTICS.MEM_READ | lief.PE.SECTION_CHARACTERISTICS.MEM_EXECUTE

# Create '.data' section for the string(s)
section_data                 = lief.PE.Section(".hdata")
section_data.content         = data
section_data.virtual_address = 0x8000
section_data.characteristics = lief.PE.SECTION_CHARACTERISTICS.CNT_INITIALIZED_DATA | lief.PE.SECTION_CHARACTERISTICS.MEM_READ

binary = lief.parse("PE32_x86_binary_HelloWorld.exe")

# Disable ASLR
binary.optional_header.dll_characteristics &= ~lief.PE.DLL_CHARACTERISTICS.DYNAMIC_BASE

# Disable NX protection
binary.optional_header.dll_characteristics &= ~lief.PE.DLL_CHARACTERISTICS.NX_COMPAT

# Add the sections
section_text = binary.add_section(section_text)
section_data = binary.add_section(section_data)

# Add the 'ExitProcess' function to kernel32
kernel32 = binary.get_import("KERNEL32.dll")
kernel32.add_entry("ExitProcess")

# Add the 'user32.dll' library
user32 = binary.add_library("user32.dll")

# Add the 'MessageBoxA' function
user32.add_entry("MessageBoxA")

# Get the IAT of functions used in the hook
ExitProcess_addr = binary.predict_function_rva("KERNEL32.dll", "ExitProcess")
MessageBoxA_addr = binary.predict_function_rva("user32.dll", "MessageBoxA")
print("Address of 'MessageBoxA': 0x{:06x} ".format(MessageBoxA_addr))
print("Address of 'ExitProcess': 0x{:06x} ".format(ExitProcess_addr))

# Hook the '__acrt_iob_func' function with our code
binary.hook_function("__acrt_iob_func", binary.optional_header.imagebase + section_text.virtual_address)

# Invoke the builder
builder = lief.PE.Builder(binary)

# Configure it to rebuild and patch the imports
builder.build_imports(True).patch_imports(True)

# Build !
builder.build()

# Save the result
builder.write("lief_pe32_hooking.exe")



