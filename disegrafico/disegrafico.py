"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

# --- ESTILOS REUTILIZABLES ---

# Estilo para las tarjetas de información
info_card_style = {
    "width": ["90%", "80%", "40%"],  # Ancho: 90% en móvil, 80% en tablet, 40% en escritorio
    "align": "center",
    "border": "2px solid black",
    "border_radius": "30px",
    "height": "auto",  # Altura automática para que el texto quepa bien
    "min_height": "200px",
    "padding": "30px",
    "background": "rgba(255, 255, 255, 0.1)",
    "box_shadow": "0 8px 32px rgba(0, 0, 0, 0.2)",
    "transition": "transform 0.35s ease, box-shadow 0.35s ease",
    "_hover": {
        "transform": "scale(1.05)",
        "box_shadow": "0 12px 40px rgba(0,0,0,0.25)"
    }
}

# --- COMPONENTES REUTILIZABLES ---

def header_card() -> rx.Component:
    """La tarjeta negra principal con el título y la imagen grande."""
    return rx.flex(
        # ... (el vstack con los headings no cambia) ...
        rx.vstack(
            rx.heading("DISEÑADOR WEB", font_size=["2.5em", "3.5em", "4.5em"], color="white"),
            rx.heading("PARA EMPRESAS", font_size=["2.5em", "3.5em", "4.5em"], color="white"),
            rx.text("SEO y visibilidad en Google e IA", color="white", font_size=["1em", "1.1em", "1.2em"]),
            width=["100%", "100%", "50%"], 
            align="center",
            spacing="3",
        ),
        # ... (el box con la imagen no cambia) ...
        rx.box(
            rx.image(
                src="/diseno-de-paginas-web-en-madrid-3-980x854.webp", 
                width=["300px", "400px", "600px"], 
                height="auto",
            ),
            width=["100%", "100%", "50%"],
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        
        # 👇 --- CAMBIO AQUÍ --- 👇
        # Usamos el diccionario en lugar de la lista
        direction={"base": "column", "md": "column", "lg": "row"},
        # --- FIN DEL CAMBIO --- 👆

        bg="black",
        height="auto",
        min_height="550px",
        align="center",
        justify="center",
        width="96%",
        box_shadow="0 8px 32px rgba(0, 0, 0, 0.2)",
        border_radius="30px",
        padding=["2em", "2em", "0em"],
        spacing="5",
        transition="transform 0.35s ease, box-shadow 0.35s ease",
        _hover={
            "transform": "scale(1.02)",
            "box_shadow": "0 12px 40px rgba(0,0,0,0.25)"
        }
    )

def info_card(title: str, text: str) -> rx.Component:
    """Una tarjeta de información reutilizable."""
    return rx.vstack(
        rx.heading(title, size="6", color="black"),
        rx.text(text, color="black", size="4"),
        style=info_card_style,
        spacing="3",
    )

# --- PÁGINA PRINCIPAL ---

def index() -> rx.Component:
    return rx.vstack(
        # ... (el box del logo no cambia) ...
        rx.box(
            rx.image(
                src="/Disenador-web-para-empresas.webp",),
            width="200px",
        ),
        
        header_card(),
        
        rx.flex(
            info_card(
                title="Diseño Web Personalizado para Empresas",
                text="..."
            ),
            info_card(
                title="SEO para empresas: visibilidad en Google y en IA",
                text="..."
            ),

            # 👇 --- CAMBIO AQUÍ --- 👇
            # Usamos el diccionario en lugar de la lista
            direction={"base": "column", "md": "column", "lg": "row"},
            # --- FIN DEL CAMBIO --- 👆

            spacing="5",
            width="100%",
            align="center",
            justify="center",
            margin_top="2em",
        ),
        
        spacing="5",
        align="center",
        min_height="85vh",
        padding_bottom="2em",
    )

# Configuración de la App (sin cambios aquí)
app = rx.App(
    enable_state=False,

    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="teal"
    )
)
app.add_page(index)