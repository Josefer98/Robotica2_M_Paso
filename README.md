# Robotica2
## Nombres: Cristian Alejandro Durán Ignacio - Alfaro Ayzama José Fernando - Ever Rolando Rejas Espinoza

# 🚀 Proyecto 4 

## 💡 Control de Motor paso a paso por MQTT entre Laptop y Raspberry Pi 4
### Este proyecto demuestra cómo comunicar una laptop (publicador) y una Raspberry Pi 4 (suscriptor y broker) mediante el protocolo **MQTT**, con el objetivo de controlar un **motor paso a paso** a través de comandos enviados desde la PC (`X`=90, `C`=180, `V`=270, `B`=360).

## 📌 Introducción
### Este proyecto utiliza **Mosquitto MQTT** como broker en la Raspberry Pi. Desde la laptop se envían comandos para mover un motor paso a paso conectado a la Raspberry Pi a posiciones angulares específicas. Esta arquitectura ilustra el modelo clásico **publicador-suscriptor** del protocolo MQTT en una aplicación de robótica.

## 🧰 Tecnologías y Librerías
- Python 3
  
- MQTT con [paho-mqtt](https://pypi.org/project/paho-mqtt/)
  
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) para control de pines en la Raspberry Pi
  
- Raspberry Pi 4 con sistema operativo Raspbian
  
- Driver L298N o similar para el motor paso a paso
  
- Motor paso a paso bipolar (1.8° por paso)
  
- Cables de conexión

## ⚙️ Esquema de funcionamiento
El esquema muestra cómo la laptop envía comandos al tópico "casa/motor", y la Raspberry Pi se suscribe a ese tópico recibe los comandos y controla el motor. 

<p>
  <img src="files_/esquema.png" alt="conecciones" width="700" height="500"/>
</p>

## 🚀Para armado, instalación y ejecución de codigo
### Clonar el repositorio :  
```bash
git clone https://github.com/Josefer98/Robotica2_M_Paso.git 
```
### 🛠️ Dependencias y libreiras necesarias 
## 💻 Laptop
instalar paho-mqtt
```bash
pip install paho-mqtt
```

abrir un entorno que ejecute python y copiar el codigo de publicador 

## 🍓 Raspberry Pi 4 (Suscriptor y Broker)
librerias 
```bash
pip install paho-mqtt RPi.GPIO
```
broker
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```
copiar el codigo de suscriptor en un entorno en la Raspberry Pi 4
## 🔌 🔧 Conexiones del Motor Paso a Paso (GPIO)
- IN1 → GPIO 17
  
- IN2 → GPIO 18
  
- IN3 → GPIO 27
  
- IN4 → GPIO 22
  
  <p>
  <img src="files_/coneciones.png" alt="conecciones" width="700" height="500"/>
  </p>
  
## 🚀 Cómo ejecutar
### 🍓En la Raspberry Pi 4 (Suscriptor)
Guarda el siguiente código como subscribe.py y ejecútalo:
```bash
python subscribe.py
```
Esto suscribe a la Raspberry al tópico "casa/motor" y controla el motor paso a paso.
### 💻En la Laptop (Publicador)
Asegúrate de que la IP del broker en publish.py sea la IP local de tu Raspberry Pi:
```bash
broker = "192.168.84.231" # Reemplaza con tu IP
```
Ejecuta el código:
```bash
python publish.py
```
Escribe comandos:
```bash
Comando a enviar: X    → Mueve el motor a 90°
Comando a enviar: C    → Mueve el motor a 180°
Comando a enviar: V    → Mueve el motor a 270°
Comando a enviar: B    → Mueve el motor a 360°
Comando a enviar: SALIR → Cierra el programa
```

## 📌 Notas importantes

-Ambos dispositivos deben estar conectados a la misma red Wi-Fi.

-El puerto MQTT por defecto (1883) debe estar abierto y accesible en la Raspberry.

-Si usas otro tópico distinto a casa/motor, recuerda modificarlo en ambos códigos.

-Asegúrate de que la IP en publish.py coincida con la de tu Raspberry Pi.
  
# 🎥Demostracion de funcionamineto

![Public](files_/public.gif) ![Suscrib](files_/suscrib.gif)

