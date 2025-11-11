from machine import I2C, Pin
from time import sleep
from bme280 import BME280  # salve o arquivo anterior como bme280.py

# Inicializa o barramento I2C0
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)

# Cria o objeto do sensor (endereço padrão 0x76)
bme = BME280(i2c=i2c)

print("Iniciando leituras do BME280...\n")

while True:
    temperatura, pressao, umidade = bme.values
    print("Temperatura: {} | Pressão: {} | Umidade: {}".format(temperatura, pressao, umidade))
    sleep(2)
