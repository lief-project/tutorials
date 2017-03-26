import lief

hashme = lief.parse("hashme")
libm   = lief.parse("/usr/lib/libm.so.6")


def swap(obj, a, b):
    symbol_a = next(filter(lambda e : e.name == a, obj.dynamic_symbols))
    symbol_b = next(filter(lambda e : e.name == b, obj.dynamic_symbols))
    b_name = symbol_b.name
    symbol_b.name = symbol_a.name
    symbol_a.name = b_name

hashme_pow_sym = next(filter(lambda e : e.name == "pow", hashme.imported_symbols))
hashme_log_sym = next(filter(lambda e : e.name == "log", hashme.imported_symbols))

hashme_pow_sym.name = "cos"
hashme_log_sym.name = "sin"

swap(libm, "log", "sin")
swap(libm, "pow", "cos")

hashme.write("hashme.obf")
libm.write("libm.so.6")

print("done")

