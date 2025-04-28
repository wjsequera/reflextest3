import reflex as rx
from reflextest3.components.title import title
import reflextest3.constants as const
from reflextest3.components.link_sponsors import link_sponsors
from reflextest3.stilos.stilos import Size as Size

def sponsor()-> rx.Component:
    return rx.vstack(     
        title("Colaboran"),  
        rx.hstack(
            #rx.image(src="publicidadScada.png", width="80px", height="80px", margin_bottom="0px"),
            link_sponsors("publicidadCurso.png",const.WJSSEQUERA_TWICH),
            link_sponsors("tempImg.png",const.WJSSEQUERA_TWICH),
            link_sponsors("tempImg.png",const.WJSSEQUERA_TWICH),
            width="100%"
        
        ),
           align="center",  # Centra los elementos horizontalmente
           justify="center",  # Centra los elementos verticalmente 
           width="100%",
           spacing=Size.Medium.value,
           
    )
