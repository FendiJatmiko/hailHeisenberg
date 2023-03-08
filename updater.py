#!/usr/bin/env python3

import shutil
import subprocess

# define src, and dst
src  = "00-welcome"
dst ="/etc/update-motd.d/00-welcome"

# shutil.copyfile(src, dst)
subprocess.run(["sudo", "cp", src, dst])

# subprocess.run(["sudo", "cp", "00-welcome", "/etc/update-motd.d/" ])
subprocess.run(["ls", "-la", "/etc/update-motd.d"])
