from time import sleep
from SevenSegmantDisplay import SegmantDisplay


num = 0


def callback(pin):
  print(pin)
  if pin == Pin(15):
    global num
    num = num + 1 
    print (num)
    seg.Display(num)
      
seg=SegmantDisplay()
seg.increase.irq(trigger=Pin.IRQ_FALLING, handler=callback)
seg.Display(num)

while True:
  #read button
 ''' value = seg.input_read(num)
  if value != num:
    num =value
    #Display (num)
    if num < 0:
     num = 9 
    elif num > 9:
      num = 0
    seg.Display(num)
    #sleep(0.5)

    sleep(0.1)'''

