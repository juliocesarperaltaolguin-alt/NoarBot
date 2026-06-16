import customtkinter as ctk

# ================= CONFIG =================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ================= FUNCIONES =================

def enviar():
    mensaje = entrada.get()

    if mensaje.strip() == "":
        return

    chat.insert("end", f"\n🧑 Tú:\n{mensaje}\n")

    mensaje_lower = mensaje.lower()

    if "hola" in mensaje_lower:
        respuesta = "Qué onda bro 😎"
    elif "como estas" in mensaje_lower:
        respuesta = "Ando al cien 🔥"
    elif "tu nombre" in mensaje_lower:
        respuesta = "Soy NoarBot 🤖"
    else:
        respuesta = "Todavía sigo aprendiendo bro."

    chat.insert("end", f"\n🤖 NoarBot:\n{respuesta}\n")

    entrada.delete(0, "end")

# ================= VENTANA =================

app = ctk.CTk()
app.title("NoarBot AI")
app.geometry("1100x700")

# ================= TITULO =================

titulo = ctk.CTkLabel(
    app,
    text="🤖 NOARBOT AI",
    font=("Segoe UI", 34, "bold")
)

titulo.pack(pady=(20, 5))

subtitulo = ctk.CTkLabel(
    app,
    text="Asistente Inteligente",
    font=("Segoe UI", 15)
)

subtitulo.pack()

# ================= CHAT =================

chat = ctk.CTkTextbox(
    app,
    width=950,
    height=500,
    corner_radius=20,
    font=("Segoe UI", 16)
)

chat.pack(pady=20)

chat.insert("end", "🤖 NoarBot AI iniciado correctamente.\n")
chat.insert("end", "🤖 Bienvenido bro.\n")

# ================= BARRA INFERIOR =================

frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

frame.pack(pady=10)

entrada = ctk.CTkEntry(
    frame,
    width=750,
    height=50,
    corner_radius=25,
    placeholder_text="Escribe un mensaje..."
)

entrada.grid(row=0, column=0, padx=10)

boton = ctk.CTkButton(
    frame,
    text="Enviar",
    width=130,
    height=50,
    corner_radius=25,
    command=enviar
)

boton.grid(row=0, column=1)

# ================= ENTER =================

entrada.focus()
entrada.bind("<Return>", lambda event: enviar())

# ================= LOOP =================

app.mainloop()
