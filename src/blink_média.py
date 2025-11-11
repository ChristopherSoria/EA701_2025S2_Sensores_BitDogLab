from machine import Pin, I2C
from time import sleep
from bme280 import BME280  # Certifique-se de ter bme280.py salvo na raiz da placa

# --- Configuração I2C e LED ---
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
led = Pin(25, Pin.OUT)  # GPIO25 é o LED onboard no Raspberry Pi Pico

bme = BME280(i2c=i2c)

# --- Parâmetros da média móvel ---
N = 5  # número de amostras na média
leituras_temp = []

print("Iniciando leituras com média móvel...\n")

while True:
    # Pisca o LED para indicar nova leitura
    led.value(1)
    
    # Lê valores do sensor
    temp_str, pressao_str, umidade_str = bme.values
    
    # Extrai apenas o número da temperatura (ex: "25.34C" -> 25.34)
    temperatura = float(temp_str.replace("C", ""))
    
    # Atualiza a lista de leituras
    leituras_temp.append(temperatura)
    if len(leituras_temp) > N:
        leituras_temp.pop(0)  # remove a leitura mais antiga
    
    # Calcula a média
    media_temp = sum(leituras_temp) / len(leituras_temp)
    
    # Mostra os dados
    print("Temp atual: {:.2f} °C | Média ({} leit.): {:.2f} °C".format(
        temperatura, len(leituras_temp), media_temp))
    
    # Apaga o LED e espera
    led.value(0)
    sleep(2)

