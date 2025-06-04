import flet as ft
from gui.main import Program

async def main(page: ft.Page):
    program_ui = Program(page)

if __name__ == "__main__":
    ft.app(target=main)
