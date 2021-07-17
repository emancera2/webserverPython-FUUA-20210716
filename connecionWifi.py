import network
import utime
ssid="Harry Mancera"
passwd="80352754*"
wf = network.WLAN(network.STA_IF) #AP_IF
wf.active(True)
listaWifi = wf.scan()
for i in listaWifi:
    print(i[0].decode())
"""wf.connect(ssid,passwd)
while not wf.isconnected():
    print(".")
    utime.sleep(1)
print(wf.ifconfig())
#wf.config("mac")
#wf.ifconfig()
"""