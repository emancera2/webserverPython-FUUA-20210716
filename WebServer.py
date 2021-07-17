#Librerias
import time
from machine import Pin
import network
import socket

#Configuración inicial de WiFi
ssid = 'Harry Mancera'  #Nombre de la Red
password = '80352754*' #Contraseña de la red
wlan = network.WLAN(network.STA_IF)

wlan.active(True) #Activa el Wifi
wlan.connect(ssid, password) #Hace la conexión

while wlan.isconnected() == False: #Espera a que se conecte a la red
    pass

print('Conexion con el WiFi %s establecida' % ssid)
print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi

#Salidas
led = Pin(12, Pin.OUT)

#Pagina web
def web_page():  
    html = """
<html>
<head>
<title>Web Server 2021</title>
</head>            
<body>
<a href="/enciende" >ON</a>
<a href="/apaga" >OFF</a>                                
</body>            
</html>  """
    return html

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 80))
tcp_socket.listen(3)

while True:
    conn, addr = tcp_socket.accept()
    print('Nueva conexion desde:  %s' % str(addr))
    request = conn.recv(1024)
    print('Solicitud = %s' % str(request))
    request = str(request)
    if request.find('/enciende') != -1:
        print('Enciende')
        led.value(1)
    if request.find('/apaga') != -1:
        print('Apaga')
        led.value(0)

    
    #Mostrar Página
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
                   
