import flet as ft
from gui.main import ProgramInterface

async def main(page: ft.Page):
    program_ui = ProgramInterface(page)

if __name__ == "__main__":
    ft.app(target=main)
