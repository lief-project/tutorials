#!/usr/bin/env python3
import lief
import sys

filezilla = lief.parse("filezilla.exe")

if not filezilla.has_resources:
    print("'{}' has no resources. Abort!".format(filezilla.name), file=sys.stderr)
    sys.exit(1)

root = filezilla.resources

# First level => Type
manifest_node = next(filter(lambda e : e.id == lief.PE.RESOURCE_TYPES.MANIFEST, root.childs))
print(manifest_node)

# Second level => ID
id_node = manifest_node.childs[0]
print(id_node)

# Third level => Lang (Data node)
lang_node = id_node.childs[0]
print(lang_node)

manifest = bytes(lang_node.content).decode("utf8")

print(manifest)

manifest = manifest.replace("asInvoker", "requireAdministrator")

lang_node.content = list(manifest.encode("utf8"))

# Rebuild
builder = lief.PE.Builder(filezilla)
builder.build_resources(True)
builder.build()
builder.write("filezilla_v2.exe")





