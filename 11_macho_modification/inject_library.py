import lief
clang = lief.parse("/usr/bin/clang")

clang.add_library("/Users/romain/libexample.dylib")

clang.write("/tmp/clang.new")
