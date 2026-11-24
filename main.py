"""user-1125: ships the one-word username; gate 1..30."""

import json
import os

MANTLE = 30


def weigh_name(folder):
    tag_path = os.path.join(folder, "entry.txt")
    blob = open(tag_path, "rb").read()
    name = blob.decode("utf-8").strip()
    if len(name) > MANTLE or len(name) < 1:
        raise SystemExit("name weighs %d chars; the gate allows 1..%d" % (len(name), MANTLE))
    if any(ch.isspace() for ch in name):
        raise SystemExit("one word means one word")
    return name


def hang_name(folder, name):
    rack = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(rack, exist_ok=True)
    hook = os.path.join(rack, "entry.txt")
    with open(hook, "w", encoding="utf-8", newline="\n") as hanger:
        hanger.write(name + "\n")
    return hook


lobby = os.path.dirname(os.path.abspath(__file__))
name = weigh_name(lobby)
print(json.dumps({"handle": name, "weight": len(name), "swagger": "quiet", "hook": hang_name(lobby, name)}))
