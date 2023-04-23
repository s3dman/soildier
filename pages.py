from os import walk
import flet as ft
import modifier


def mainPage(page):
    page.clean()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
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
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )
    )


def optimalListPage(page, db):
    page.clean()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    ac = [
        ft.DataColumn(ft.Text(i))
        for i in "Score Crop Nitrogen Phosphorous Pottasium Temperature Humidity pH Rainfall".split()
    ]
    ar = []
    rdb = modifier.getCrops()
    for j in db:
        print(j[1], j[0], rdb[j[0]])
        r = [ft.DataCell(ft.Text(round(j[1], 6))), ft.DataCell(ft.Text(j[0]))]
        for i in rdb[j[0]]:
            r.append(ft.DataCell(ft.Text(i)))

        ar.append(ft.DataRow(r))
    table = ft.DataTable(
        columns=ac,
        rows=ar,
    )

    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.IconButton(
                        ft.icons.ARROW_BACK, on_click=lambda err: optimalityPage(page)
                    ),
                    table,
                ],
            ),
            alignment=ft.alignment.center,
        )
    )


def optimalityPage(page):
    page.clean()
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    input_cells = [ft.TextField(scale=0.85) for i in range(7)]

    def checkOptimality(e):
        data = []
        for i in input_cells:
            if i.value == "":
                return -1
            data.append(float(i.value))
        optimalListPage(page, modifier.getOptimalList(data))

    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Nitrogen", width=100), numeric=True),
                            ft.DataColumn(
                                ft.Text("Phosphorous", width=100), numeric=True
                            ),
                            ft.DataColumn(
                                ft.Text("Pottasium", width=100), numeric=True
                            ),
                            ft.DataColumn(
                                ft.Text("Temperature", width=100), numeric=True
                            ),
                            ft.DataColumn(ft.Text("Humidity", width=100), numeric=True),
                            ft.DataColumn(ft.Text("pH Value", width=100), numeric=True),
                            ft.DataColumn(ft.Text("Rainfall", width=100), numeric=True),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[ft.DataCell(i) for i in input_cells],
                            ),
                        ],
                    ),
                    ft.Row(
                        [
                            ft.IconButton(
                                ft.icons.ARROW_BACK,
                                on_click=lambda err: mainPage(page),
                            ),
                            ft.IconButton(ft.icons.ADD, on_click=checkOptimality),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )
    )


def addItemPage(page):
    page.clean()
    input_cells = [ft.TextField(scale=0.85) for i in range(8)]

    def addItem(e):
        data = []
        for i in input_cells:
            if i.value == "":
                return -1
            if i == input_cells[0]:
                data.append(i.value)
                continue
            data.append(float(i.value))
        modifier.addOptimality(data[0], data[1:])
        editPage(page)

    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(
                                ft.Text(
                                    "Crop", width=100, text_align=ft.TextAlign.RIGHT
                                )
                            ),
                            ft.DataColumn(
                                ft.Text(
                                    "Nitrogen", width=100, text_align=ft.TextAlign.RIGHT
                                ),
                                numeric=True,
                            ),
                            ft.DataColumn(
                                ft.Text(
                                    "Phosphorous",
                                    width=100,
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                numeric=True,
                            ),
                            ft.DataColumn(
                                ft.Text(
                                    "Pottasium",
                                    width=100,
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                numeric=True,
                            ),
                            ft.DataColumn(
                                ft.Text(
                                    "Temperature",
                                    width=100,
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                numeric=True,
                            ),
                            ft.DataColumn(
                                ft.Text(
                                    "Humidity", width=100, text_align=ft.TextAlign.RIGHT
                                ),
                                numeric=True,
                            ),
                            ft.DataColumn(
                                ft.Text(
                                    "pH Value", width=100, text_align=ft.TextAlign.RIGHT
                                ),
                                numeric=True,
                            ),
                            ft.DataColumn(
                                ft.Text(
                                    "Rainfall", width=100, text_align=ft.TextAlign.RIGHT
                                ),
                                numeric=True,
                            ),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[ft.DataCell(i) for i in input_cells],
                            ),
                        ],
                    ),
                    ft.Row(
                        [
                            ft.IconButton(
                                ft.icons.ARROW_BACK, on_click=lambda err: editPage(page)
                            ),
                            ft.IconButton(ft.icons.ADD, on_click=addItem),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )
    )


def editPage(page):
    page.clean()
    db = modifier.getCrops()
    ar = []

    def deleteRow(data):
        cropname = data.control.data
        modifier.delCrop(cropname)
        editPage(page)

    for j in db:
        r = [ft.DataCell(ft.Text(j))]
        for i in db[j]:
            r.append(ft.DataCell(ft.Text(i)))

        r.append(
            ft.DataCell(
                ft.IconButton(ft.icons.DELETE_OUTLINED, on_click=deleteRow, data=j)
            )
        )
        ar.append(ft.DataRow(r))

    ac = [
        ft.DataColumn(ft.Text(i))
        for i in "Crop Nitrogen Phosphorous Pottasium Temperature Humidity pH Rainfall".split()
    ]
    ac.append(
        ft.DataColumn(
            ft.IconButton(ft.icons.ADD_ROUNDED, on_click=lambda err: addItemPage(page))
        )
    )
    table = ft.DataTable(
        columns=ac,
        rows=ar,
    )

    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.IconButton(
                        ft.icons.ARROW_BACK, on_click=lambda err: mainPage(page)
                    ),
                    table,
                ],
            ),
            alignment=ft.alignment.center,
        )
    )


def main(page: ft.Page):
    page.title = "jomama"
    page.window_full_screen = True
    mainPage(page)


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)