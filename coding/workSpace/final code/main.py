# Complete project details at https://RandomNerdTutorials.com
from machine import Pin
#from utime import sleep_ms

from display import SegmantDisplay



num = 0

def web_page():
  global num
  
  num = seg.Display(num)
    
  html = """<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="1">
  </head>
  <body>
      <p><strong>""" + str(num) + """</strong></p>
  </body>
  </html>"""
  
  return html
  
def callback(pin):
    state = machine.disable_irq()
    sleep_ms(150)
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
num = seg.Display(num)

#Create a socket and specify the socket type. 
#We create a new socket object called s with the given address family, and socket type. This is a STREAM TCP socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to an address (network interface and port number) using the bind() method. 
#accepts a tupple variable with the ip address, and port number:
s.bind(('', 80))
#enables the server to accept connections;#
s.listen(5)

while True:
  conn, addr = s.accept()
  conn.settimeout(3.0)
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  conn.settimeout(None)
  request = str(request)
  print('Content = %s' % request)
  print(request.find('/?num=increase'))
  increase = request.find('/?num=increase')
  decrease = request.find('/?num=decrease')
  reset = request.find('/?num=reset')
  
  if increase == 6:
    print('Increase')
    num = num + 1
  if decrease == 6:
    print('Decrease')
    num = num - 1
  if reset == 6:
    print('Reset')
    num = 0
    
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
 



