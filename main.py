import time
import asyncio
from tkinter import *
import ttkbootstrap as tb
import tkinter as tk
from ttkbootstrap.constants import *
from pyModbusTCP.client import ModbusClient


# Declaro Variables
peso = 20.65


# Ahora armo la ventana con ttkbootstrap, una masa
root = tb.Window(themename="superhero")
# TCP auto connect on modbus request, dont close after it
c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=False)
valor = tk.DoubleVar(value = 20.65)

#Acá hago los ponmenores de ModBus
#def conectar_modbus():


#async def const_window():

print("Creando interface")
root.title("Demo de Gaude lpm")
root.geometry("800x600")

tk.Label(
        root,
        text="trabajando",
        fg="White",
        bg="Black",
        justify="center",
            ).pack(
            fill=tk.BOTH
                )

my_meter = tb.Meter(
    root,
    bootstyle="danger",
    subtext="Lectura Actual",
    interactive=False,
    textright=" Kgs",
    metertype="semi",
    stripethickness=10,
    meterthickness=80,
    metersize=400)

my_meter.pack(pady=50)

my_meter.configure(amountused=peso)


async def leer_regs():
        regs = c.read_holding_registers(0, 10)
        if regs:
            print(regs)
            val = regs[0] / 100
            global peso
            peso = val
            return (val)
        else:
            print("read error")

        await asyncio.sleep(1) # espera de 1 segundo para simular la actualización


async def main():

    #await const_window()
    #conectar_modbus()
    while (True):
        print("hola")
        # se ejecutan las tareas en segundo plano utilizando asyncio
        await leer_regs()
        print("por aca pasa")
        my_meter.configure(amountused=peso)
        my_meter.update()
        root.update()

asyncio.run(main())

