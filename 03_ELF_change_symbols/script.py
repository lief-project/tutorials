import lief

hashme = lief.parse("hashme")
libm   = lief.parse("/usr/lib/libm.so.6")


def swap(obj, a, b):
    symbol_a = [e for e in obj.dynamic_symbols if e.name == a].pop()
    symbol_b = [e for e in obj.dynamic_symbols if e.name == b].pop()
    b_name = symbol_b.name
    symbol_b.name = symbol_a.name
    symbol_a.name = b_name

hashme_pow_sym = [e for e in hashme.imported_symbols if e.name == "pow"].pop()
hashme_log_sym = [e for e in hashme.imported_symbols if e.name == "log"].pop()

hashme_pow_sym.name = "cos"
hashme_log_sym.name = "sin"

swap(libm, "log", "sin")
swap(libm, "pow", "cos")

hashme.write("hashme.obf")
libm.write("libm.so.6")

print("done")

