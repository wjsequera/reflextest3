import reflex as rx
import datetime
from reflextest3.stilos.stilos import Size as Size
from reflextest3.stilos.colors import TextColor as TextColor
import reflextest3.constants as const

def footer()-> rx.Component:
    return rx.vstack(
                rx.image(src="publicidadScada.png", width="80px", height="80px", margin_bottom="0px"),
                rx.link(f"2020-{datetime.date.today().year} wjsequera@gmail.com. python developer practice",
                        href=const.WJSSEQUERA_TWICH,
                        is_external=True,margin_top="0px"
                        ),
                rx.text("2025 wjsequera@gmail.com. python developer practice",
                        margin_top="0px",
                        color=TextColor.FOOTER.value
                        ),
        align="center",  # Centra los elementos horizontalmente
        justify="center", # Centra los elementos verticalmente
        margin_bottom=Size.MEDIUM.value,
        #padding_bottom=Size.BIG.value,
        padding_y=Size.BIG.value,
        font_size=Size.MEDIUM.value,
        #bg="white"
    )
