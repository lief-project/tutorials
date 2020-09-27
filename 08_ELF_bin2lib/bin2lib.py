import sys
import lief

if len(sys.argv) != 3:
    print("Usage {} <input binary> <address>".format(sys.argv[0]))
    sys.exit(1)

path    = sys.argv[1]
address = int(sys.argv[2], 16)

app = lief.parse(path)
app[lief.ELF.DYNAMIC_TAGS.FLAGS_1].remove(lief.ELF.DYNAMIC_FLAGS_1.PIE)
app.add_exported_function(address, "check_found")
app.write("libcrackme101.so")
