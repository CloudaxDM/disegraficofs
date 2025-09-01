import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="bold", color="white"), href=url
    )


def navbar_dropdown() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo_disegrafico.webp",
                        width="200px",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Inicio", "/#"),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text(
                                    "Servicios",
                                    size="4",
                                    weight="medium",
                                    color="white",
                                ),
                                rx.icon("chevron-down", color="white"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item("Seo"),
                            rx.menu.item("Paginas Web"),
                            rx.menu.item("Redes sociales"),
                        ),
                    ),
                    navbar_link("Blog", "/#"),
                    navbar_link("Contacto", "/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo_disegrafico.webp",
                        width="200px",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30, color="white")
                    ),
                    rx.menu.content(
                        rx.menu.item("Inicio"),
                        rx.menu.sub(
                            rx.menu.sub_trigger("Servicios"),
                            rx.menu.sub_content(
                                rx.menu.item("Seo"),
                                rx.menu.item("Paginas Web"),
                                rx.menu.item("Redes Sociales"),
                            ),
                        ),
                        rx.menu.item("Blog"),
                        rx.menu.item("Contacto"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg="black",
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    ),

def modulo():
    return rx.vstack(
        rx.heading("Tecnologías que utilizamos", size="8", color="white", align="center"),
        rx.grid(
            rx.image(src="/html5.svg", width="100px", height="auto"),
            rx.image(src="/mysql.svg", width="100px", height="auto"),
            rx.image(src="/javascript.svg", width="100px", height="auto"),
            rx.image(src="/favicon.ico", width="100px", height="auto"),
            columns={"base": "2", "md": "4", "lg": "4"},
            spacing="8",
    ),
    bg="black",
    width="96%",
    border_radius="20px",
    padding="2em",
    height="auto",
    align="center",
    justify="center",
    transition="transform 0.35s ease, box-shadow 0.35s ease",
    _hover={
            "transform": "scale(1.02)",
            "box_shadow": "0 12px 40px rgba(0,0,0,0.25)"
        }
    )