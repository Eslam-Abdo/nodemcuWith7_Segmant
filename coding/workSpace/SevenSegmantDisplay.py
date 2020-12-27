from machine import Pin,ADC
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
pin_e = Pin(D5, Pin.OUT)
pin_f = Pin(D6, Pin.OUT)
pin_g = Pin(D7, Pin.OUT)

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
    
  
