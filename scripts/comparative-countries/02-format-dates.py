import os, re
from collections import defaultdict

PATTERN = re.compile(r"^\d+_(\d{2})-(\d{2})-(\d{4})")

for group in os.listdir("."):
    if not os.path.isdir(group):
        continue
    for leader in os.listdir(group):
        parent = os.path.join(group, leader)
        if not os.path.isdir(parent):
            continue
        children = [c for c in os.listdir(parent) if os.path.isdir(os.path.join(parent, c))]
        counts = defaultdict(int)
        for c in children:
            m = PATTERN.match(c)
            if m:
                counts[f"{m.group(3)}-{m.group(1)}-{m.group(2)}"] += 1
        used = defaultdict(int)
        for c in sorted(children):
            m = PATTERN.match(c)
            if not m:
                continue
            base = f"{m.group(3)}-{m.group(1)}-{m.group(2)}"
            used[base] += 1
            new = base if counts[base] == 1 else f"{base} ({used[base]})"
            if c != new:
                os.rename(os.path.join(parent, c), os.path.join(parent, new))
