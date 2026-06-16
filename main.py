import random
import requests
import re

# =====================================
# VARIABLES
# =====================================

dado_usuario = None
dado_bot = None

# =====================================
# CALCULADORA
# =====================================

def calcular_expresion(texto):

    texto = texto.replace(" ", "")

    if not re.match(r'^[0-9+\-*/().%]+$', texto):
        return None

    try:
        resultado = eval(texto)
        return f"NoarBot: Resultado = {resultado}"

    except:
        return "NoarBot: No pude resolver esa operación."


# =====================================
# CLIMA ACTUAL
# =====================================

def obtener_clima_real():

    try:

        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=19.43"
            "&longitude=-99.13"
            "&current=temperature_2m"
        )

        datos = requests.get(url, timeout=5).json()

        temperatura = datos["current"]["temperature_2m"]

        return f"NoarBot: Temperatura actual {temperatura}°C"

    except:

        return "NoarBot: No pude obtener el clima real."


# =====================================
# CLIMA SEMANAL
# =====================================

def obtener_clima_semanal():

    try:

        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=19.43"
            "&longitude=-99.13"
            "&daily=temperature_2m_max,temperature_2m_min"
            "&timezone=auto"
        )

        datos = requests.get(url, timeout=5).json()

        maximas = datos["daily"]["temperature_2m_max"]
        minimas = datos["daily"]["temperature_2m_min"]

        dias = [
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo"
        ]

        respuesta = "Pronóstico semanal:\n\n"

        for i in range(7):

            respuesta += (
                f"{dias[i]}\n"
                f"Máx: {maximas[i]}°C\n"
                f"Mín: {minimas[i]}°C\n\n"
            )

        return respuesta

    except:

        return "No pude obtener el clima semanal."
    # =====================================
# RESPONDER
# =====================================

def responder(user):

    global dado_usuario
    global dado_bot

    user = user.lower()

    # ---------------- SALUDOS ----------------

    if (

        "hola" in user or
        "holaa" in user or
        "holi" in user or
        "hey" in user or
        "ey" in user or
        "qué onda" in user or
        "que onda" in user or
        "buenas" in user or
        "hello" in user or
        "saludos" in user or
        "qué pasa" in user or
        "que pasa" in user or
        "cómo va" in user or
        "como va" in user or
        "qué haces" in user or
        "que haces" in user

    ):

        saludos = [

            "NoarBot: Hola, ¿cómo estás?",
            "NoarBot: Hey bro, ¿qué tal?",
            "NoarBot: Qué onda",
            "NoarBot: Hola soy la version nueva",
            "NoarBot: Hey, aquí ando",
            "NoarBot: Buenas",
            "NoarBot: Qué pasa",
            "NoarBot: Hola, ¿qué haces?"

        ]

        return random.choice(saludos)

    # ---------------- CONVERSACIÓN ----------------

    elif (

        "qué tal" in user or
        "que tal" in user or
        "cómo estás" in user or
        "como estas" in user or
        "todo bien" in user or
        "cómo andas" in user or
        "como andas" in user or
        "cómo te va" in user or
        "como te va" in user or
        "qué cuentas" in user or
        "que cuentas" in user or
        "cómo va todo" in user or
        "como va todo" in user

    ):

        respuestas = [

            "NoarBot: Todo tranquilo",
            "NoarBot: Bastante bien",
            "NoarBot: Aquí andamos",
            "NoarBot: Relax",
            "NoarBot: Todo cool",
            "NoarBot: Todo bien bro",
            "NoarBot: Ando chill",
            "NoarBot: Todo en orden"

        ]

        return random.choice(respuestas)

    # ---------------- FELIZ ----------------

    elif (

        "estoy feliz" in user or
        "ando feliz" in user or
        "me siento bien" in user or
        "estoy contento" in user or
        "ando contento" in user or
        "estoy alegre" in user or
        "me siento genial" in user or
        "estoy emocionado" in user

    ):

        felices = [

            "NoarBot: Qué bueno bro",
            "NoarBot: Me alegra escuchar eso",
            "NoarBot: Buena esa",
            "NoarBot: Así debe ser",
            "NoarBot: Me gusta escuchar eso"

        ]

        return random.choice(felices)

    # ---------------- TRISTE ----------------

    elif (

        "estoy triste" in user or
        "ando triste" in user or
        "me siento mal" in user or
        "estoy deprimido" in user or
        "ando mal" in user or
        "me siento solo" in user or
        "estoy cansado" in user or
        "hoy fue un mal día" in user

    ):

        tristes = [

            "NoarBot: Ánimo bro",
            "NoarBot: Espero que todo mejore",
            "NoarBot: Aquí ando",
            "NoarBot: Ojalá te sientas mejor",
            "NoarBot: Todo pasa bro"

        ]

        return random.choice(tristes)
        # ---------------- JUGAR ----------------

    elif (

        "jugar" in user or
        "juego" in user or
        "vamos a jugar" in user or
        "quieres jugar" in user or
        "jugamos algo" in user or
        "hay que jugar" in user or
        "me aburro" in user or
        "hagamos algo" in user or
        "quiero divertirme" in user

    ):

        juegos = [

            "NoarBot: Claro, juguemos a los dados",
            "NoarBot: Va, lancemos un dado",
            "NoarBot: Me gusta ese juego",
            "NoarBot: El número más alto gana"

        ]

        return random.choice(juegos)

    # ---------------- TU DADO ----------------

    elif (

        "lanzo mi dado" in user or
        "lanza mi dado" in user or
        "tiro mi dado" in user or
        "voy yo" in user or
        "me toca" in user or
        "mi turno" in user

    ):

        dado_usuario = random.randint(1, 6)

        return f"NoarBot: Tu dado cayó en {dado_usuario}"

    # ---------------- DADO BOT ----------------

    elif (

        "lanza tu dado" in user or
        "ahora tu" in user or
        "ahora tú" in user or
        "te toca" in user or
        "tu turno" in user

    ):

        dado_bot = random.randint(1, 6)

        return f"NoarBot: Mi dado cayó en {dado_bot}"

    # ---------------- GANADOR ----------------

    elif (

        "quien gano" in user or
        "quién ganó" in user or
        "quien gana" in user or
        "quién gana" in user or
        "quién va ganando" in user or
        "quien va ganando" in user

    ):

        if dado_usuario and dado_bot:

            if dado_usuario > dado_bot:
                return "NoarBot: Tú ganaste"

            elif dado_bot > dado_usuario:
                return "NoarBot: Yo gané"

            else:
                return "NoarBot: Fue empate"

        return "NoarBot: Primero debemos lanzar ambos dados"

    # ---------------- LOTERÍA ----------------

    elif (

        "loteria" in user or
        "lotería" in user or
        "numeros de loteria" in user or
        "números de lotería" in user or
        "dame suerte" in user or
        "otra loteria" in user or
        "otra lotería" in user or
        "numeros random" in user or
        "números random" in user

    ):

        numeros = random.sample(range(1, 100), 4)

        return (
            f"NoarBot:\n\n"
            f"Números de lotería:\n\n"
            f"{numeros[0]}\n"
            f"{numeros[1]}\n"
            f"{numeros[2]}\n"
            f"{numeros[3]}"
        )

    # ---------------- NÚMERO ALEATORIO ----------------

    elif (

        "numero random" in user or
        "número random" in user or
        "numero aleatorio" in user or
        "número aleatorio" in user

    ):

        return f"NoarBot: {random.randint(1,1000)}"
        # ---------------- CLIMA SEMANAL ----------------

    elif (

        "clima semanal" in user or
        "pronostico" in user or
        "pronóstico" in user or
        "clima de la semana" in user or
        "semana" in user

    ):

        return obtener_clima_semanal()

    # ---------------- CLIMA ACTUAL ----------------

    elif (

        "clima" in user or
        "temperatura" in user or
        "como esta el clima" in user or
        "cómo está el clima" in user

    ):

        return obtener_clima_real()

    # ---------------- CALCULADORA ----------------

    resultado = calcular_expresion(user)

    if resultado:

        return resultado

    # ---------------- NO ENTIENDE ----------------

    desconocido = [

        "NoarBot: No entendí muy bien eso",
        "NoarBot: Hmm, intenta decirlo diferente",
        "NoarBot: Creo que no comprendí",
        "NoarBot: ¿Puedes repetirlo de otra forma?",
        "NoarBot: No capté eso"

    ]

    return random.choice(desconocido)
# =====================================
# INICIO DEL BOT
# =====================================

if __name__ == "__main__":

    print("NOARBOT PRO MAX")

    while True:

        mensaje = input("\nTú: ")

        if mensaje.lower() in [

            "salir",
            "exit",
            "adios",
            "adiós",
            "bye",
            "nos vemos"

        ]:

            print("\nNoarBot: Nos vemos bro")
            break

        respuesta = responder(mensaje)

        print(f"\n{respuesta}")