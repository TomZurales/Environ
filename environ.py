#!/usr/bin/env python3

import keyboard
import sys

keywords = ["create", "delete"]
recordings = {}
args = sys.argv
if len(args) == 1:
    print("Ex: environ create python")
    exit()

name = args[1]
if name in keywords:
    if name == keywords[0]:
        print(f"Recording setup for {args[2]}\nPress ESC to end\n")
        recordings[args[2]] = keyboard.record(until='esc')
        keyboard.play(recordings[args[2]], speed_factor=10)
print(f"Setting up environment {name}")
