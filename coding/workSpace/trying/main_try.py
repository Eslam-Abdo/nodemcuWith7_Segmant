# Complete project details at https://RandomNerdTutorials.com
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


def web_page():
  global num
  
  num = seg.Display(num)
    
  num_value=str(num)
  html = """<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="10">
  </head>
  <body>
      <p><strong>""" + num_value + """</strong></p>
  </body>
  </html>"""
  
  return html
  
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
  print(num)
  
  

seg=SegmantDisplay(True)
seg.increase.irq(trigger=Pin.IRQ_FALLING, handler=callback)
seg.decrease.irq(trigger=Pin.IRQ_FALLING, handler=callback)
seg.reset.irq(trigger=Pin.IRQ_FALLING, handler=callback)
seg.Display(num)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
    if gc.mem_free() < 102000:
      gc.collect()
     
    conn, addr = s.accept()
    conn.settimeout(3.0)
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    conn.settimeout(None)
    request = str(request)
    print('Content = %s' % request)
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
      
  except OSError as e:
    conn.close()
    print('Connection closed')





