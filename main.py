import random
import string
from flask import Flask

app = Flask(__name__)

# Tus 17 datos aleatorios
datos_aleatorios = [
    "El primer programa informático de la historia fue escrito por una mujer, Ada Lovelace.",
    "El ojo de un avestruz es más grande que su cerebro.",
    "Los pulpos tienen tres corazones y su sangre es de color azul.",
    "Un día en Venus es más largo que un año entero en ese mismo planeta.",
    "La Torre Eiffel puede crecer hasta 15 centímetros en verano por el calor.",
    "Las huellas dactilares de los koalas son casi idénticas a las de los humanos.",
    "El corazón de una ballena azul es del tamaño y peso de un automóvil pequeño.",
    "Los gatos tienen 32 músculos en cada una de sus orejas.",
    "El sonido viaja unas cuatro veces más rápido en el agua que en el aire.",
    "Las abejas pueden recordar y reconocer rostros humanos.",
    "El esqueleto de un tiburón está hecho de cartílago, no de huesos.",
    "Los flamencos nacen grises y se vuelven rosados por los camarones que comen.",
    "El espacio exterior es completamente silencioso porque no hay aire para transmitir el sonido.",
    "Las vacas tienen mejores amigas y se estresan si las separan de ellas.",
    "Las jirafas duermen de pie la mayoría de las veces y solo unos 20 minutos al día.",
    "Los perros tienen un sentido del olfato hasta 100,000 veces más potente que el nuestro.",
    "El agua de la Tierra es más antigua que el mismísimo Sol."
]

# 1. Página de inicio (Conecta a las otras dos páginas)
@app.route("/")
def home():
    return """
    <h1>Página de Inicio</h1>
    <p>¡Bienvenido a nuestro sitio web interactivo!</p>
    <hr>
    <ul>
        <li><a href="/random_fact">¡Ver un dato aleatorio!</a></li>
        <li><a href="/secret">🤫 Ir a la página secreta</a></li>
    </ul>
    """

# 2. Página de datos aleatorios
@app.route("/random_fact")
def random_fact():
    dato = random.choice(datos_aleatorios)
    return f"""
    <h1>Dato Aleatorio del Día</h1>
    <p style="font-size: 18px; color: #333;">💡 {dato}</p>
    <hr>
    <a href="/">⬅ Volver al inicio</a>
    """

# 3. NUEVA RUTA: ¡Página secreta con Generador de Contraseñas!
@app.route("/secret")
def secret_page():
    # Genera una contraseña segura al azar de 12 caracteres
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    contrasena_generada = "".join(random.choice(caracteres) for i in range(12))
    
    return f"""
    <h1>🤫 ¡Has encontrado la página secreta!</h1>
    <p>Aquí tienes una herramienta exclusiva.</p>
    <div style="background-color: #f0f0f0; padding: 15px; border-radius: 5px; display: inline-block;">
        <strong>Tu contraseña segura aleatoria:</strong> 
        <code style="font-size: 18px; color: #d63384;">{contrasena_generada}</code>
    </div>
    <br><br>
    <p><small>(Refresca la página para generar otra contraseña)</small></p>
    <hr>
    <a href="/">⬅ Volver al inicio</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
