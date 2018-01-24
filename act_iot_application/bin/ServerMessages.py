#Autor:Diego Lopes da Silva
#Data:29/11/2017
#Projeto:ACT
#Descrição:criar server para receber mensagem
from TranslatorCommand import *
from socket import *

def ServerNet():
    #porta e host
    port=5000
    host=''

    #definindo protocolo
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(10)
    print("---------------")
    print("Sistema On-line")
    print("---------------")
    while True:
        connect, address = sock.accept()
        print("Sistema foi conectado por: ", address)
        while True:
            msg = connect.recv(1024)
            if not msg: break
            at=msg.decode("utf-8")
            print(at)
            sTraCommand(at)
        print("Conexao fechada")
        connect.close()

