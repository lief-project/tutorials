#!/usr/bin/env python3
import lief

mfc = lief.parse("mfc.exe")
cmd = lief.parse("cmd.exe")

mfc_rsrc_manager = mfc.resources_manager
cmd_rsrc_manager = cmd.resources_manager

if not mfc_rsrc_manager.has_icons:
    print("'{}' has no manifest. Abort!".format(mfc.name), file=sys.stderr)
    sys.exit(1)

if not cmd_rsrc_manager.has_icons:
    print("'{}' has no manifest. Abort!".format(mfc.name), file=sys.stderr)
    sys.exit(1)

mfc_icons = mfc_rsrc_manager.icons
cmd_icons = cmd_rsrc_manager.icons
for i in range(min(len(mfc_icons), len(cmd_icons))):
    mfc_rsrc_manager.change_icon(mfc_icons[i], cmd_icons[i])

builder = lief.PE.Builder(mfc)
builder.build_resources(True)
builder.build()
builder.write("foo.exe")

