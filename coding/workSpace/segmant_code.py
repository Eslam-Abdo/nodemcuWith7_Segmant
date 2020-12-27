# Complete project details at https://RandomNerdTutorials.com

from machine import Pin,ADC
from time import sleep
#from SevenSegmantDisplay import Display

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

pin_a = Pin(D1 , Pin.OUT)
pin_b = Pin(D2 , Pin.OUT)
pin_c = Pin(D3 , Pin.OUT)
pin_d = Pin(D4 , Pin.OUT)
pin_e = Pin(D5 , Pin.OUT)
pin_f = Pin(D6 , Pin.OUT)
pin_g = Pin(D7 , Pin.OUT)

increase = Pin(D8, Pin.IN)
decrease = Pin(D0, Pin.IN)
reset    =  ADC(A0)
#########################################################
def Display(number):
  
  if number == 0:
    pin_a.on()
    pin_b.on()
    pin_c.on()
    pin_d.on()
    pin_e.on()
    pin_f.on()
    pin_g.off()
    
  elif number == 1:
    pin_a.off()
    pin_b.on()
    pin_c.on()
    pin_d.off()
    pin_e.off()
    pin_f.off()
    pin_g.off()
    
  elif number == 2:
    pin_a.on()
    pin_b.on()
    pin_c.off()
    pin_d.on()
    pin_e.on()
    pin_f.off()
    pin_g.on()
    
  elif number == 3:
    pin_a.on()
    pin_b.on()
    pin_c.on()
    pin_d.on()
    pin_e.off()
    pin_f.off()
    pin_g.on()
    
  elif number == 4:
    pin_a.off()
    pin_b.on()
    pin_c.on()
    pin_d.off()
    pin_e.off()
    pin_f.on()
    pin_g.on()
    
  elif number == 5:
    pin_a.on()
    pin_b.off()
    pin_c.on()
    pin_d.on()
    pin_e.off()
    pin_f.on()
    pin_g.on()
    
  elif number == 6:
    pin_a.on()
    pin_b.off()
    pin_c.on()
    pin_d.on()
    pin_e.on()
    pin_f.on()
    pin_g.on()
    
  elif number == 7:
    pin_a.on()
    pin_b.on()
    pin_c.on()
    pin_d.off()
    pin_e.off()
    pin_f.off()
    pin_g.off()
    
  elif number == 8:
    pin_a.on()
    pin_b.on()
    pin_c.on()
    pin_d.on()
    pin_e.on()
    pin_f.on()
    pin_g.on()
    
  elif number == 9:
    pin_a.on()
    pin_b.on()
    pin_c.on()
    pin_d.on()
    pin_e.off()
    pin_f.on()
    pin_g.on()
    
#########################################################


num = 0
Display(0)
flag = 0

while True:
  #for i in range(10)
  '''increase_state =  increase.value()
  decrease_state = not (decrease.value())
  reset_state = reset.read()'''
 #sleep(0.1)
  #read buttons
  if (increase.value()==1) and (flag != 1):
    sleep(0.15)
    if (increase.value()==1) and (flag != 1):
      num = num + 1
      flag = 1
      print(flag)
    #sleep(0.1)
  elif (decrease.value() == 0 )and (flag != 2):
    sleep(0.15)
    if (decrease.value() == 0 )and (flag != 2):
      num = num - 1
      flag = 2
      print(flag)
      
  elif (reset.read() >= 1000) and (flag != 3):
    sleep(0.1)
    if (reset.read() >= 1000) and (flag != 3):
      num = 0
      flag = 3
      print(flag)
  elif flag !=0: 
    flag = 0
    print(flag)
     
  #Display (num)
  #display number
  if num <= 0:
   num = 0 
   Display(0)
  elif num >= 9:
    num = 9
    Display(9)
  else:
    Display(num)
  #sleep(0.5)

sleep(0.4)

