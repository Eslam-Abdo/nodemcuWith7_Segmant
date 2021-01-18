from machine import Pin
from utime import sleep_ms

from display import SegmantDisplay

num = 0 

def callback(pin):
    state = machine.disable_irq()
    sleep_ms(50)
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

num=seg.Display(num)








