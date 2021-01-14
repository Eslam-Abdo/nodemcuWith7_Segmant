from machine import Pin

class SegmantDisplay:
  def __init__(self):
    self.D = [16,5,4,0,2,14,12,13,15,3,1] #pin mapping
    self.pin_init()
    
  def pin_init(self):
    #output
    self.pin_a = Pin(self.D[5] , Pin.OUT)
    self.pin_b = Pin(self.D[6] , Pin.OUT)
    self.pin_c = Pin(self.D[7] , Pin.OUT)
    self.pin_d = Pin(self.D[8] , Pin.OUT)
    #input
    self.increase = Pin(self.D[1], Pin.IN,Pin.PULL_UP)
    self.decrease = Pin(self.D[2], Pin.IN,Pin.PULL_UP)
    self.reset    = Pin(self.D[3], Pin.IN,Pin.PULL_UP)

  def Display(self,number):
    if number < 0:
      number = 9 
    elif number > 9:
      number = 0
    self.decoderDisplay(number)
    return number
      
  def decoderDisplay(self,number):
    if number == 0:
      self.pin_a.off()
      self.pin_b.off()
      self.pin_c.off()
      self.pin_d.off()
      
    elif number == 1:
      self.pin_a.off()
      self.pin_b.off()
      self.pin_c.off()
      self.pin_d.on()
      
    elif number == 2:
      self.pin_a.off()
      self.pin_b.off()
      self.pin_c.on()
      self.pin_d.off()
      
    elif number == 3:
      self.pin_a.off()
      self.pin_b.off()
      self.pin_c.on()
      self.pin_d.on()
      
    elif number == 4:
      self.pin_a.off()
      self.pin_b.on()
      self.pin_c.off()
      self.pin_d.off()
      
    elif number == 5:
      self.pin_a.off()
      self.pin_b.on()
      self.pin_c.off()
      self.pin_d.on()
      
    elif number == 6:
      self.pin_a.off()
      self.pin_b.on()
      self.pin_c.on()
      self.pin_d.off()
      
    elif number == 7:
      self.pin_a.off()
      self.pin_b.on()
      self.pin_c.on()
      self.pin_d.on()
      
    elif number == 8:
      self.pin_a.on()
      self.pin_b.off()
      self.pin_c.off()
      self.pin_d.off()
      
    elif number == 9:
      self.pin_a.on()
      self.pin_b.off()
      self.pin_c.off()
      self.pin_d.on()
    

  



