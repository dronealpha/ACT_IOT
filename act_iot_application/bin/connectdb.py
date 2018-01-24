#---------------------------------------------
#Autor:Diego Lopes da Silva                  #
#Data:04/11/2017                             #
#Descrição:Script acesso ao banco de dados   #
#---------------------------------------------

#import de biblioteca de acesso ao banco de dados
import MySQLdb
from load_settings import *

#função para transações de banco executar(proc, insert, delete ,update)
def dbCommunicationTransaction(cmdtsc):
    db = MySQLdb.connect(host="localhost",user="root",passwd="meteora22",db="act_iot_db")
    cur = db.cursor()
    cur.execute(cmdtsc)
    db.commit()
    db.close()

#função 
def dbCommunicationFind(cmdselect):
    db = MySQLdb.connect(host="localhost",user="root",passwd="meteora22",db="act_iot_db")
    cur = db.cursor()
    cur.execute(cmdselect)
    dados=""
    for row in cur.fetchall():
        dados = dados  + str(row)
    db.close()
    return dados

#sql="select * from act_rec_type;"
#hostbanco=getBasehost()
#dados1=dbCommunicationFind(sql)

