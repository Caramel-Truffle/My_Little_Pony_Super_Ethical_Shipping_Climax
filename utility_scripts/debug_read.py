
path = "/home/user/AI/antigravity/MLP_SESC/game/tl/Engrish/common.rpy"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"Read {len(lines)} lines")
    if len(lines) > 366:
        print(f"Line 366: {repr(lines[366])}")
        print(f"Line 367: {repr(lines[367])}")
