def getDataBase():
    stbase = load_datas()
    descart,base = stbase[0].split(":")
    return base

def getBaseLogin():
    stlogin = load_datas()
    descart,login = stlogin[1].split(":")
    return login

def getBasePassword():
    stpass = load_datas()
    descart,password = stpass[2].split(":")
    return password

def getBasehost():
    sthost = load_datas()
    descart,host = sthost[3].split(":")
    return host

def load_datas():
    arq = open('/home/diego/Área de Trabalho/act_iot/act_iot_application/conf/act.cfg', 'r')
    texto = arq.readlines()
    arq.close()

    return texto
