from RegisterOperation import *
from Cut_command import *
from drivercut import *

def sTraCommand(cmd):
    #split para quebra do comando
    com,act,scode,sdate,sip = cmd.split(",")
    print("----------------------------")
    print("comando>> "+com)
    print("tipo>> "+act)
    print("security code>> "+scode)
    print("Data do comando>> " + sdate)
    print("ip do dispositivo>> " + sip)
    print("----------------------------")
    
    #executando comando
    msg=""
    
    try:
       #checa no banco se code bate
       respcode = ValidSecurityCode(scode)
       msg="Codigo Invalido"
       
       #valida qual comanda a ser realizado e se code está ok
       if((com == "cut") and (respcode ==True)):
          msg="Processo Realizado com Sucesso"
          
          if(1 == int(act)):
             print("Comando de religar")
             CutON(act,scode,sdate,sip)
             cutOn()

          elif(0 == int(act)):
             print("Comando de corte")
             CutON(act,scode,sdate,sip)
             cutOff()
             
    except:
        msg="Erro ao processar comando"
    finally:
        print(msg)


#string com comando de corte
#cmd="cut,0,aX23fg15,01122017094512,192.168.0.35"
#sTraCommand(cmd)
