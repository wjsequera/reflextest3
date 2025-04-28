import reflex as rx
import reflextest3.stilos.stilos as stilos
from reflextest3.stilos.colors import Color as Color


def link_icon(url: str)-> rx.Component:
    return rx.link(
              rx.icon(
                  tag="link"),
              href=url,
              is_external= True,
              color_scheme="orange"
          
              )
    
