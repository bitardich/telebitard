# -*- coding: utf-8 -*-

# import modules
import sys

try:
    import core
    print("all done")
except (ImportError, ModuleNotFoundError) as e:
    print(f"error: {e}")
    sys.exit(1)


