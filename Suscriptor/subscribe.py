import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

# === CONFIGURACION GPIO ===
GPIO.setmode(GPIO.BCM)
# Pines conectados a las entradas IN1ï¿½IN4 del driver H-Bridge (p.ej. A4988/L298N)
IN1, IN2, IN3, IN4 = 17, 18, 27, 22
pins = [IN1, IN2, IN3, IN4]
for p in pins:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, False)

# Secuencia half-step para motor bipolar 1.8ï¿½ (200 full-step -> 400 half-step)
step_seq = [
    [1,0,0,0],
    [1,0,1,0],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [0,1,0,1],
    [0,0,0,1],
    [1,0,0,1],
]

# Parï¿½metros del motor bipolar
steps_per_revolution = 400  # medios pasos por vuelta
current_angle = 0           # posiciï¿½n actual en grados (0ï¿½359)

def step(steps, delay=0.002):
    """Gira el motor 'steps' medio-pasos en sentido horario."""
    idx = 0
    for _ in range(steps):
        for pin, val in zip(pins, step_seq[idx]):
            GPIO.output(pin, val)
        time.sleep(delay)
        idx = (idx + 1) % len(step_seq)
    # Apagar bobinas
    for p in pins:
        GPIO.output(p, False)

def move_to(target_angle):
    """
    Avanza siempre en sentido horario desde current_angle hasta target_angle,
    moviendo sï¿½lo los grados que faltan.
    """
    global current_angle
    target = target_angle % 360

    if target >= current_angle:
        delta = target - current_angle
    else:
        delta = (360 - current_angle) + target

    steps = int(delta * steps_per_revolution / 360)
    if steps > 0:
        step(steps)
    current_angle = target

# === CALLBACK MQTT ===
def on_message(client, userdata, msg):
    cmd = msg.payload.decode().upper()
    print(f"Mensaje recibido: {cmd}")

    if cmd == "X":
        move_to(90)
        print("? Movido a 90")
    elif cmd == "C":
        move_to(180)
        print("? Movido a 180")
    elif cmd == "V":
        move_to(270)
        print("? Movido a 270")
    elif cmd == "B":
        move_to(360)
        print("? Movido a 360")
    else:
        print("? Comando no reconocido")

# === ARRANQUE MQTT ===
client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("casa/motor")

print("Escuchando comandos en 'casa/motor'")
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSaliendo")
finally:
    GPIO.cleanup()