"""Load a script from a skill folder (the folder names have hyphens)."""

import importlib.util
import os

# Im Vault liegen die Skills in .claude/skills, die Tests in .claude/tests/day-trader
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(os.path.dirname(os.path.dirname(HERE)), "skills")
FIX = os.path.join(HERE, "fixtures")


def load(folder, name):
    path = os.path.join(ROOT, folder, name + ".py")
    spec = importlib.util.spec_from_file_location("trader_" + name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
