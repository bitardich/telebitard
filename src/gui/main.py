import flet as ft
from core.session_manager import Manager

class ProgramInterface:
    
    def __init__(self, page: ft.Page):

        self.page = page
        self.setup_page()
        self.ui()

    def setup_page(self):

        self.page.title = "Telebitard"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window.center()
        self.page.padding = 10
        self.page.update()

        self.picker = ft.FilePicker(on_result=self.handler_file_picker)
        self.page.overlay.append(self.picker)
        self.page.update()

    def handler_file_picker(self):
        pass

    def notification(self, message: str, is_error: bool = False):
        self.page.snack_bar = ft.SnackBar(
            ft.Text(message),
            bgcolor=ft.colors.RED_400 if is_error else None,
            open=True
        )
        self.page.update()

    def ui(self):

        # контент табов
        tabSessionsCnt = ft.Column(
            controls=[
                #ft.Divider(),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Добавить",
                            icon=ft.icons.ADD,
                            on_click=self.notification("пр")
                        ),
                        ft.ElevatedButton(
                            text="Удалить",
                            icon=ft.icons.DELETE,
                        )
                    ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10
                ),
                ft.Divider()
                ],
            expand=True
        )

        tabSettingsCnt = ft.Column(
            controls=[
                #скора
            ],
            expand=True
        )
        self.tabs = ft.Tabs(
            selected_index=0,
            animation_duration=100,
            tabs=[
                ft.Tab(
                    text="Сессии",
                    icon=ft.icons.PEOPLE,
                    content=tabSessionsCnt
                ),
                ft.Tab(
                    text="Настройки",
                    icon=ft.icons.SETTINGS,
                    content=tabSettingsCnt
                ),
            ],
            expand=True,
        )
    
        self.page.add(
            ft.Column(controls=[self.tabs], expand=True)
        )
        self.page.update()