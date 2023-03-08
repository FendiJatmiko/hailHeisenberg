#!/usr/bin/env python3

# import shutil
import os
import subprocess

# define src, and dst
src  = "00-welcome"
dst ="/etc/update-motd.d/00-welcome"
dir_path = "/etc/update-motd.d/"

# shutil.copyfile(src, dst)
# clean existing
for file in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file)
    os.remove(file_path)

# subprocess.run(["sudo", "cp", src, dst])

subprocess.run(["sudo", "cp", "00-welcome", "/etc/update-motd.d/" ])
subprocess.run(["ls", "-la", "/etc/update-motd.d"])
