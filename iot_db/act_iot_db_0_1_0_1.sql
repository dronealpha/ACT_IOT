/*
Autor:Diego Lopes da Silva
Data:16/11/2017
Descrição:criar tabela para guardar as chaves de segurança, tabela usuários proprietarios e add coluna na tabela act_msg_history
*/

--tabela para guarda chaves
create table act_security_code(
   code_id int primary key not null auto_increment,
   key_scurity varchar(200) not null
);


commit;

--tabela de ususários
create table act_user(
   user_id int primary key not null auto_increment,
   user_name varchar(200) not null,
   user_code_id int not null
);

alter table act_user
add constraint  fk_user_code_security
foreign key(user_code_id)
references act_security_code(code_id); 

commit;

--add campo para usuários na tabela act_msg_history
alter table act_msg_history
add msg_history_user_id
int not null;


alter table act_msg_history
add constraint fk_msg_history_user
foreign key(msg_history_user_id)
references act_user(user_id);

commit;






   
   
