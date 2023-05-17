from pyModbusTCP.client import ModbusClient

#c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=False)
try:
    c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=False)
except ValueError:
    print("Error with host or port params")

print(c.unit_id)
print(c.last_error_as_txt)

if c.open():
    print(c.last_error_as_txt)
    print("pasa por if")
    regs = c.read_holding_registers(0, 10)
    if regs:
        print(regs)
    else:
        print("read error")
else:
    print("no esta conectado")
    print(c.last_error_as_txt)


