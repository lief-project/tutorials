#!/usr/bin/python3.6

import lief
import zipfile
import shutil
import subprocess
import tempfile
import os
import pathlib

def rcmd(cmd):
    if type(cmd) is str:
        cmd = cmd.split(" ")
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False, check=False)
    if p.returncode > 0:
        print(p.stdout.decode("utf8"))
        print(p.stderr.decode("utf8"))


JARSIGNER = shutil.which("jarsigner")
ADB       = shutil.which("adb")
KEYSTORE  = "keystore.jks"

apk  = "org.telegram.messenger_4.8.4-12207.apk"
lib  = "libgadget.so"
conf = "libgadget.config.so"

workingdir = tempfile.mkdtemp(suffix='_lief_frida')

# Unzip
print(f"[+] Unzip the {apk} in {workingdir}")
zip_ref = zipfile.ZipFile(apk, 'r')
zip_ref.extractall(workingdir)
zip_ref.close()

# Add 'frida-gadget-10.7.3-android-arm64.so' to libtmessages.28.so
libdir = pathlib.Path(workingdir) / "lib"
libcheck_path = libdir / "arm64-v8a" / "libtmessages.28.so"


print(f"[+] Injecting {lib} into {libcheck_path}")
libcheck = lief.parse(libcheck_path.as_posix())

# Injection
libcheck.add_library("libgadget.so")
libcheck.write(libcheck_path.as_posix())

# Copy the hook library
print(f"[+] Copying {lib} and {conf} in the APK")
shutil.copy(lib, libdir / "arm64-v8a")
shutil.copy(conf, libdir / "arm64-v8a")

# Remove old signature
shutil.rmtree(os.path.join(workingdir, "META-INF"))

# Zip
print(f"[+] APK Building...")
shutil.make_archive("new", 'zip', workingdir)
shutil.move("new.zip", "new.apk")

cmd_sign = [
    JARSIGNER,
    "-verbose",
    "-sigalg", "SHA1withRSA",
    "-digestalg", "SHA1",
    "-keystore", KEYSTORE,
    "-storepass", "android",
    "new.apk",
    "android"]

print(f"[+] Signing the APK")
rcmd(cmd_sign)

