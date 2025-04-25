import paho.mqtt.publish as publish

# IP de la Raspberry Pi
broker = "192.168.243.231"  # reemplaza con la IP real de tu Raspberry

print("Envia 'X'(90°), 'C'(180°), 'V'(270°), 'B'(360°) o 'SALIR' para terminar.\n")

while True:
    mensaje = input("Comando a enviar: ").strip().upper()
    
    if mensaje == "salir":
        print("Saliendo del programa...")
        break
    elif mensaje in ["X", "C", "V", "B"]:
        publish.single("casa/motor", mensaje, hostname=broker)
        print(f"Mensaje '{mensaje}' enviado al broker {broker}")
    else:
        print("Comando no válido. Usa 'X', 'C', 'V', 'B' o 'SALIR'.")
