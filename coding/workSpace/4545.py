from machine import Pin
from utime import sleep_ms

D0  = 16
D1  = 5
D2  = 4
D3  = 0
D4  = 2
D5  = 14
D6  = 12
D7  = 13
D8  = 15
D9  = 3
D10 = 1
A0 = 0

num = 0
def callback(pin):
    state = machine.disable_irq()
    sleep_ms(100)
    if p0.value() == 0:
        print(pin)
    machine.enable_irq(state)
  
def intterrput(pin):
  pass
  
l2 = Pin(D4, Pin.OUT)
p0 = Pin(D1, Pin.IN,Pin.PULL_UP)
p2 = Pin(D2, Pin.IN,Pin.PULL_UP)
p0.irq(trigger=Pin.IRQ_RISING, handler=callback)
p2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
while True:
  l2.off()
  sleep_ms(500)
  l2.on()
  sleep_ms(500)

