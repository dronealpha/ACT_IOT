from connectdb import *

def CutON(tipo,scode,sdate,sip):
    if int(tipo) == 0:
        tipo='2'
    #Busca descrição do tipo de rec
    sql = "select @DCTP:=rec_type_desc from act_rec_type where rec_type_id ="+tipo+";"

    #valida se chave exite no banco de dados
    st = dbCommunicationFind(sql)
    st = st.replace('(','')
    st = st.replace(')','')
    st = st.replace(',','')
    print(st)

    #insert na tabela act_rec_msg para registro de tipode mensagem se é corte ou religa
    comando ="insert into act_rec_msg(rec_msg_type_id,rec_msg_command) values ("+tipo+","+st+");"
    #print(comando)
    dbCommunicationTransaction(comando)

    #pega o id do usuário 
    sql2 = "select @user:= p.user_id from act_user p inner join act_security_code"
    sql2 = sql2 + " sc on p.user_code_id = sc.code_id where sc.key_scurity='"+scode+"';"

    st2 = dbCommunicationFind(sql2)
    st2 = st2.replace('(','')
    st2 = st2.replace(')','')
    st2 = st2.replace(',','')
    

    #pega o status da operação
    sql3 = "select @cdstt:= process_status_id from act_process_status where process_status_id="+tipo+";"
    st3 = dbCommunicationFind(sql3)
    st3 = st3.replace('(','')
    st3 = st3.replace(')','')
    st3 = st3.replace(',','')
    

    #monda string de data
    sdatabanco = sdate[4:8]+"-"+sdate[2:4]+"-"+sdate[0:2]+" "+sdate[8:10]+":"+sdate[10:12]+":"+sdate[12:14]
    

    #pegar Id do rec_msg_history
    sql4 = "select @reid:=  max(rec_msg_id) from act_rec_msg;"
    st4 = dbCommunicationFind(sql4)
    st4 = st4.replace('(','')
    st4 = st4.replace(')','')
    st4 = st4.replace(',','')
    

    #insert na tabela de Registro de msg processada
    sqlinst = "insert into act_msg_history(msg_history_rec_id,msg_history_proc_status,msg_history_date,msg_history_user_id,act_msg_ip)"
    sqlinst = sqlinst + " values("+st4+","+st3+",'"+sdatabanco+"',"+st2+",'"+sip+"');"
    #print(sqlinst)
    dbCommunicationTransaction(sqlinst)
    
    

#tipo='1'
#scode='aX23fg15'
#sdate='01122017094512'
#sip='192.168.0.35'
#CutON(tipo,scode,sdate,sip)

    
