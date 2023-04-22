import flet as ft
import modifier


def mainPage(page):
    page.clean()
    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.TextButton(
                        "Check Crop Optimality",
                        on_click=lambda err: optimalityPage(page),
                    ),
                    ft.TextButton(
                        "Add/Modify Crop Details",
                        on_click=lambda err: editPage(page),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            )
        )
    )


def optimalityPage(page):
    page.clean()
    page.add(ft.Container())


# def editPage(page):
#     page.clean()
#     page.add(ft.Container(
#         for i in modifier.
#         ))


def main(page: ft.Page):
    page.title = "jomama"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    mainPage(page)


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)