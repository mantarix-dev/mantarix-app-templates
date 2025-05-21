import mantarix as mx

def main(page: mx.Page):
    page.title = "Mantarix counter example"
    page.vertical_alignment = mx.MainAxisAlignment.CENTER

    txt_number = mx.TextField(value="0", text_align=mx.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        mx.Row(
            [
                mx.IconButton(mx.Icons.REMOVE, on_click=minus_click),
                txt_number,
                mx.IconButton(mx.Icons.ADD, on_click=plus_click),
            ],
            alignment=mx.MainAxisAlignment.CENTER,
        )
    )

mx.app(main)