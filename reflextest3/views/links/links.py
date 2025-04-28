import reflex as rx
from  reflextest3.components.link_button import link_button
from reflextest3.components.title import title
from reflextest3.stilos.stilos import Size as Size
import reflextest3.constants as const

def links()-> rx.Component:
    return rx.vstack(     
        title("Comunidad"),  
        link_button("Twich","Directos de Lunes a Jueves",const.WJSSEQUERA_TWICH,"icons/twitch.svg"),
        link_button("YouTube","Pelis de fin de Semana",const.WJSEQUERA_YOUTUBE,"icons/youtube.svg"),
        link_button("Twitter","Chat de la comunidad",const.SEQUERAWJ_TWITTER,"icons/X.svg"),
        
        title("Ambiente"),
        link_button("Twich","Directos de Lunes a Jueves",const.WJSSEQUERA_TWICH,"icons/twitchOrange.svg"),
        link_button("YouTube","Pelis de fin de Semana",const.WJSEQUERA_YOUTUBE,"icons/youtubeOrange.svg"),
        link_button("Twitter","Chat de la comunidad",const.SEQUERAWJ_TWITTER,"icons/Xorange.svg"),
          
           align="center",  # Centra los elementos horizontalmente
           justify="center",  # Centra los elementos verticalmente 
           width="100%",
           #spacing=Size.Medium.value
    )
