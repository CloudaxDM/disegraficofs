"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from navbar import navbar_link, navbar_dropdown, modulo
class HeaderState(rx.State):
    show_menu: bool = False

    def toggle_menu(self):
        self.show_menu = not self.show_menu

### Tu componente de cabecera, ahora corregido y responsivo.
def header_component():
    return rx.box( # Usamos un rx.box como contenedor principal
        rx.hstack(
            # Logo
            rx.image(
                src="/logo_disegrafico.webp",
                alt="Logo Disegrafico",
                width="200px",
                height="auto"
            ),
            
            rx.spacer(),
            
            # ENLACES PARA ESCRITORIO: Se ocultan en móvil
            rx.hstack(
                rx.link("Inicio", href="/", color="white", font_size="1.3em"),
                rx.link("Servicios", href="/servicios", color="white", font_size="1.3em"),
                rx.link("Contacto", href="/contacto", color="white", font_size="1.3em"),
                spacing="5",
                display=["none", "none", "flex", "flex"], # Oculto en pantallas pequeñas
            ),

            # ICONO HAMBURGUESA: Se muestra solo en móvil
            rx.icon(
                tag="hamburger",
                font_size="2em",
                color="white",
                display=["flex", "flex", "none", "none"], # Oculto en pantallas grandes
                cursor="pointer",
                on_click=HeaderState.toggle_menu,
            ),
            
            # --- Estilos del Hstack principal ---
            width="100%",
            height="80px",
            align_items="center",
            padding_x="5%",
        ),

        # MENÚ DESPLEGABLE: Se muestra u oculta según el estado
        rx.cond(
            HeaderState.show_menu,
            rx.vstack(
                rx.link("Inicio", href="/", color="white", width="100%"),
                rx.link("Servicios", href="/servicios", color="white", width="100%"),
                rx.link("Contacto", href="/contacto", color="white", width="100%"),
                
                align_items="center",
                spacing="4",
                padding="2em",
                bg="black",
                width="100%",
            )
        ),

        # --- Estilos del contenedor general ---
        bg="black",
        width="100%",
        position="fixed", # Fija la cabecera
        top="0px",
        z_index="10",
    )
# --- ESTILOS REUTILIZABLES ---

# Estilo para las tarjetas de información
info_card_style = {
    "border": "2px solid black",
    "border_radius": "30px",
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
def header_component():
    """Componente de cabecera con logo y enlaces."""
    return rx.hstack(
    # 1. El logo, sin margen a la izquierda
    rx.image(
        src="/logo_disegrafico.webp", 
        alt="Logo Disegrafico",
        width="200px", 
        height="auto"
    ),
    
    # 2. Un espaciador que empuja los elementos a los extremos
    rx.spacer(),
    
    # 3. Los enlaces agrupados, usando spacing en lugar de márgenes
    rx.hstack(
        rx.link("Inicio", href="/", color="white", font_size="1.3em"),
        rx.link("Servicios", href="/servicios", color="white", font_size="1.3em"),
        rx.link("Contacto", href="/contacto", color="white", font_size="1.3em"),
        spacing="5",  # Controla el espacio entre los enlaces
    ),

    # --- Estilos del contenedor principal ---
    width="100%",
    height="80px",
    bg="black",
    align_items="center",
    # 4. Padding para dar espacio en los bordes, en vez de un margen en el logo
    padding_x=["1em", "2em", "5%"], 
),
def header_card() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading(
                "DISEÑADOR WEB PARA EMPRESAS",
                font_size=["2.5em", "3em", "3em", "3.5em", "3.8em"],
                line_height="1.5",
                color="white",
                height="auto",
                margin_top="20px",
                text_align="center",
            ),
            rx.text(
                "SEO y visibilidad en Google e IA",
                color="white",
                font_size=["2em", "2em", "2em", "2em", "2em"],
                margin_top="30px",
                text_align="center",
            ),
            align="center",
            spacing="6",
            height="400px",
            width=["50%","70%","40%","40%"],
        ),
        
            rx.image(
                src="/diseno-de-paginas-web-en-madrid-3-980x854.webp",
                alt="Diseño de páginas web en Madrid",
                border_radius="30px",
                padding="10px",
                width=["100%","70%","40%","40%"],
                #width={"base":"300px","sm":"400px","md":"400px","lg":"400px"},
                #height="auto",
            ),
            #width={"base":"50%","md":"50%"},
            #display="flex",
            #align_items="center",
            #justify_content="center",
       
        # --- aquí es donde cambia ---
        direction={"base": "column", "md": "row"},  # columna en móvil, fila en desktop
        wrap="wrap",
        bg="black",
        align="center",
        justify="center",
        width="95%",
        box_shadow="0 8px 32px rgba(0, 0, 0, 0.2)",
        border_radius="30px",
        padding={"base":"2em","md":"0em"},
        spacing="9",
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
        height="100%",
        spacing="3",
    )

# --- PÁGINA PRINCIPAL ---

def index() -> rx.Component:
    return rx.vstack(
        navbar_dropdown(),
        
        header_card(),
        
        rx.grid(
            info_card(
                title="Diseño Web Personalizado para Empresas",
                text="Tu página web es la carta de presentación de tu empresa en Internet, por lo que es crucial que destaque en diseño, funcionalidad y rendimiento. En Disegrafico nos especializamos en la creación de páginas web a medida, 100% adaptables a cualquier dispositivo (responsive), fáciles de gestionar y totalmente seguras."
            ),
            info_card(
                title="SEO para empresas: visibilidad en Google y en IA",
                text="El SEO ya no es solo aparecer en Google. Ahora tus clientes también buscan en ChatGPT, Gemini o Claude. Estas inteligencias artificiales no muestran listados: generan respuestas y citan fuentes fiables."
            ),
            wrap="wrap",
                columns={
        "base": "1",  # Valor por defecto (móvil)
        "md": "2",    # A partir del breakpoint 'md' (tablet)
        "lg": "2",    # A partir del breakpoint 'lg' (escritorio)
    },
            spacing="5",
            padding="2em",
            width="100%",
            align="stretch",
            justify="center",
           # margin_top="2em",
        ),
        modulo(),
        
        spacing="5",
        align="center",
        min_height="85vh",
        padding_bottom="2em",
    )

# Configuración de la App (sin cambios aquí)
app = rx.App(
    enable_state=False,

    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="yellow"
    )
)
app.add_page(index,title="Diseño Web y SEO para Empresas | Tu Marca",
    description="Especialistas en diseño web a medida y posicionamiento SEO. Creamos páginas rápidas, seguras y optimizadas para Google y las nuevas búsquedas por IA.",)