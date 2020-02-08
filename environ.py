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
if name == keywords[0]:
    if len(args) != 3:
        print("Please specify a name for this recording")
        exit()
    print(f"Recording setup for {args[2]}\nPress ESC to end\n")
    recordings[args[2]] = keyboard.record(until='esc')
    keyboard.play(recordings[args[2]], speed_factor=10)
elif name == keywords[1]:
    if len(args) != 3:
        print("Please specify the name of the recording to delete")
    printf(f"Deleting recording {args[2]}\n")
    del recordings[args[2]]
elif len(args) == 2:
    print(f"Setting up environment {name}")
