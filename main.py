import time
import asyncio
from tkinter import *
import ttkbootstrap as tb
import tkinter as tk
from ttkbootstrap.constants import *
from pyModbusTCP.client import ModbusClient



# Declaro Variables
peso = 20.65
global C


# Ahora armo la ventana con ttkbootstrap, una masa
root = tb.Window(themename="superhero")
# TCP auto connect on modbus request, dont close after it
c = ModbusClient(host="192.168.1.10",
                 auto_open=True,
                 auto_close=False,
                 port=502
                 )


#Acá hago los ponmenores de ModBus
#def conectar_modbus():


async def const_window():

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

    my_meter = tb.Meter(root,
                        bootstyle="danger",
                        subtext="Lectura Actual",
                        interactive=True,
                        textright=" Kgs",
                        metertype="semi",
                        stripethickness=10,
                        metersize=400)

    my_meter.pack(pady=50)

    my_meter.configure(amountused=peso)


async def leer_regs():
        regs = c.read_holding_registers(0, 10)
        if regs:
            print(regs)
        else:
            print("read error")
        valor = regs[0] / 100

        await asyncio.sleep(0.5) # espera de 1 segundo para simular la actualización



async def main():

    await const_window()
    #conectar_modbus()
    while (True):
        print("hola")
        # se ejecutan las tareas en segundo plano utilizando asyncio
        await leer_regs()
        print("por aca pasa")
        #my_meter.configure(amountused=result)
        # se actualiza la GUI
        root.update()

asyncio.run(main())

