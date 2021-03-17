import tkinter as tk


ventana = tk.Tk()


canvas = tk.Canvas(ventana, width = 800, height = 600)
canvas.pack()

lblMensaje = tk.Label(ventana, text = "DRUGS")
lblMensaje.pack()

print("Fuck that police")

ventana.mainloop()