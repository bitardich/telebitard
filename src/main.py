import flet as ft
from gui.main import ProgramInterface

def start_ui(): #исправить
    async def _start_ui(page: ft.Page):
        program_ui = ProgramInterface(page)

    ft.app(target=_start_ui)

if __name__ == "__main__":
    start_ui()
