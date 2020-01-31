#!/usr/bin/env python3

import keyboard
import sys

keywords = ["create", "delete"]
args = sys.argv
if len(args) == 1:
    print("Ex: environ create python")
    exit()

name = args[1]
if name in keywords:
    name = args[2]
    print(f"Creating or deleting {name}")
    exit()
print(f"Setting up environment {name}")
