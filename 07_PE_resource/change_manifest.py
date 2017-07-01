#!/usr/bin/env python3
import lief
import sys

filezilla = lief.parse("filezilla.exe")

resources_manager = filezilla.resources_manager
print(resources_manager)

if not resources_manager.has_manifest:
    print("'{}' has no manifest. Abort!".format(filezilla.name), file=sys.stderr)
    sys.exit(1)

manifest = resources_manager.manifest

print(manifest)

manifest = manifest.replace("asInvoker", "requireAdministrator")
resources_manager.manifest = manifest

builder = lief.PE.Builder(filezilla)
builder.build_resources(True)
builder.build()
builder.write("filezilla_v1.exe")





