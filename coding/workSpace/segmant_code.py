from machine import Pin,ADC
from utime import sleep_ms

from SevenSegmantDisplay import SegmantDisplay

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
    sleep_ms(50)
    #print(pin)
    interput()
    machine.enable_irq(state)

def interput():
  global num
  if seg.increase.value()==0:
    num = num + 1
  if seg.decrease.value()==0:
    num = num - 1
  if seg.reset.value()==0:
    num = 0
  num=seg.Display(num)
  
    
  
seg=SegmantDisplay()
seg.increase.irq(trigger=Pin.IRQ_FALLING, handler=callback)
seg.decrease.irq(trigger=Pin.IRQ_FALLING, handler=callback)
seg.reset.irq(trigger=Pin.IRQ_FALLING, handler=callback)

seg.Display(num)






