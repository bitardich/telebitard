import flet as ft

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

    def ui(self):

        # контент табов
        tabSessionsCnt = ft.Column(
            controls=[
                #ft.Divider(),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Добавить",
                            icon=ft.icons.ADD
                        ),
                        ft.ElevatedButton(
                            text="Удалить",
                            icon=ft.icons.DELETE
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

        #ROMA PRIVET
