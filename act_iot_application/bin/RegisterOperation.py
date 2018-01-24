from  connectdb import *

def ValidSecurityCode(scode):
    #monta instrução sql para busca da chave
    sql = "select 1 from act_security_code"
    sql = sql + " where key_scurity ='"
    sql = sql + scode +"';"

    #valida se chave exite no banco de dados
    st = dbCommunicationFind(sql)
    st = st.replace('(','')
    st = st.replace(')','')
    st = st.replace(',','')

    if st == '1':
        stt = True
    else:
        stt = False
    return stt

