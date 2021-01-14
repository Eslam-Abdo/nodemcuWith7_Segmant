from machine import Pin,ADC
import utime




class SegmantDisplay:
  def __init__(self , decoder=True,callback=None):
    self.D = [16,5,4,0,2,14,12,13,15,3,1] #pin mapping
    self.decoder=decoder
    self.callback=callback
    self.pin_init()
    self.led.on()
    
  def pin_init(self):
  
    if self.decoder == True:
      #output
      self.pin_a = Pin(self.D[5] , Pin.OUT)
      self.pin_b = Pin(self.D[6] , Pin.OUT)
      self.pin_c = Pin(self.D[7] , Pin.OUT)
      self.pin_d = Pin(self.D[8] , Pin.OUT)
      self.led   = Pin(self.D[4] , Pin.OUT)
      #################
      
      #input
      self.increase = Pin(self.D[1], Pin.IN,Pin.PULL_UP)
      self.decrease = Pin(self.D[2], Pin.IN,Pin.PULL_UP)
      self.reset    = Pin(self.D[3], Pin.IN,Pin.PULL_UP)
      
    else:
      #output
      self.pin_a = Pin(self.D[1] , Pin.OUT)
      self.pin_b = Pin(self.D[2] , Pin.OUT)
      self.pin_c = Pin(self.D[3] , Pin.OUT)
      self.pin_d = Pin(self.D[4] , Pin.OUT)
      self.pin_e = Pin(self.D[5] , Pin.OUT)
      self.pin_f = Pin(self.D[6] , Pin.OUT)
      self.pin_g = Pin(self.D[7] , Pin.OUT)
      #input
      self.increase = Pin(self.D[0], Pin.IN)
      self.decrease = Pin(self.D[8], Pin.IN)
      self.reset = ADC(0)

  
  
    
  def Display(self,number):
    if number < 0:
      number = 9 
    elif number > 9:
      number = 0
      
    if self.decoder == True:
      self.decoderDisplay(number)
    else:
      self.NO_decoderDisplay(number)
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
    

  def NO_decoderDisplay(self,number):
    
    if number == 0:
      self.pin_a.on()
      self.pin_b.on()
      self.pin_c.on()
      self.pin_d.on()
      self.pin_e.on()
      self.pin_f.on()
      self.pin_g.off()
      
    elif number == 1:
      self.pin_a.off()
      self.pin_b.on()
      self.pin_c.on()
      self.pin_d.off()
      self.pin_e.off()
      self.pin_f.off()
      self.pin_g.off()
      
    elif number == 2:
      self.pin_a.on()
      self.pin_b.on()
      self.pin_c.off()
      self.pin_d.on()
      self.pin_e.on()
      self.pin_f.off()
      self.pin_g.on()
      
    elif number == 3:
      self.pin_a.on()
      self.pin_b.on()
      self.pin_c.on()
      self.pin_d.on()
      self.pin_e.off()
      self.pin_f.off()
      self.pin_g.on()
      
    elif number == 4:
      self.pin_a.off()
      self.pin_b.on()
      self.pin_c.on()
      self.pin_d.off()
      self.pin_e.off()
      self.pin_f.on()
      self.pin_g.on()
      
    elif number == 5:
      self.pin_a.on()
      self.pin_b.off()
      self.pin_c.on()
      self.pin_d.on()
      self.pin_e.off()
      self.pin_f.on()
      self.pin_g.on()
      
    elif number == 6:
      self.pin_a.on()
      self.pin_b.off()
      self.pin_c.on()
      self.pin_d.on()
      self.pin_e.on()
      self.pin_f.on()
      self.pin_g.on()
      
    elif number == 7:
      self.pin_a.on()
      self.pin_b.on()
      self.pin_c.on()
      self.pin_d.off()
      self.pin_e.off()
      self.pin_f.off()
      self.pin_g.off()
      
    elif number == 8:
      self.pin_a.on()
      self.pin_b.on()
      self.pin_c.on()
      self.pin_d.on()
      self.pin_e.on()
      self.pin_f.on()
      self.pin_g.on()
      
    elif number == 9:
      self.pin_a.on()
      self.pin_b.on()
      self.pin_c.on()
      self.pin_d.on()
      self.pin_e.off()
      self.pin_f.on()
      self.pin_g.on()
    
  def input_read(self,num_value):
    if self.increase.value()==1:
      sleep_ms(50)
      if self.increase.value()==1:
        num_value = num_value +1         
    elif self.decrease.value() == 0:
      sleep_ms(50)
      if self.decrease.value() == 0:
        num_value = num_value -1
        
    elif self.decoder == True:
      if self.reset.value() == 0:
        sleep_ms(50)
        if self.reset.value() == 0:
          num_value =  0
    else:
      if self.reset.read() >= 1000:
        sleep_ms(50)
        if self.reset.read() >= 1000:
          num_value =  0
        
        
 
    return num_value
    
 



