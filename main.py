from machine import Pin, ADC
from time import sleep
from math import log

led = Pin(25,Pin.OUT)
adc = ADC(26)

while True:
  lect = adc.read_u16()
  print("valor del ADC es:{}".format(lect))
  tension= 3.3 / 65535 * lect
  print("valor de tension es: {}".format(tension))
  R1=10000
  R2=(tension*R1) / (3.3 - tension)
  BETA=3950
  print("valor de R2 es:{}".format(R2))
  temperatura = (BETA / (log(R2/R1)+BETA/298))-273
  print("la temperatura es de: {}".format(temperatura))