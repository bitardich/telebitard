# -*- coding: utf-8 -*-

import sys

try:
    import core
    from gui.main import App
    print("all done")
except (ImportError, ModuleNotFoundError) as e:
    print(f"error: {e}")
    sys.exit(1)

import flet as ft

def main():
    ft.app(target=App().main)

if __name__ == "__main__":
    main()
