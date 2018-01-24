from socket import *
import obd
import codecs
for i in range(10):
    port=35000
    host="192.168.0.10"
    soc =  socket(AF_INET, SOCK_STREAM)
    soc.connect((host,port))
    soc.send(b'010C')
    dados = soc.recv(1024)
    at = dados.decode("utf-8")
    print(at)
    #soc.send(b'cut,1,aX23fg15,01122017094512,192.168.0.35')
    soc.close()
