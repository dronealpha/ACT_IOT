/*
Autor:Diego Lopes da Silva
Data:09/11/2017
Descrição:criar base de dados para projeto ACT_IOT
*/

create database act_iot_db;

use act_iot_db;

commit; 

--create tabela para tipos de mensagem
create table act_rec_type(
   rec_type_id int primary key not null auto_increment,
   rec_type_desc varchar(500)  not null
);

commit;

--carga de tipos de mensagem
insert into act_rec_type(rec_type_desc) values('Religar ponto');
insert into act_rec_type(rec_type_desc) values('Desligar ponto');
insert into act_rec_type(rec_type_desc) values('Leitura Temperatura');
insert into act_rec_type(rec_type_desc) values('Leitura Umidade');
insert into act_rec_type(rec_type_desc) values('Presença de usuário');

commit;


--create table para receber mensagens
create table act_rec_msg(
   rec_msg_id int primary key not null auto_increment,
   rec_msg_type_id int not null,
   rec_msg_command varchar(500) not null
);


--definindo relacionamento entre tabelas act_rec_msg com act_rec_type
alter table act_rec_msg
add constraint fk_rec_msg_type
foreign key(rec_msg_type_id)
references act_rec_type(rec_type_id); 

commit;

--criando tabela com status de processamento
create table act_process_status(
    process_status_id int primary key not null auto_increment,
    process_status_desc varchar(500) not null
);

insert into act_process_status(process_status_desc) values('Corte efetuado com sucesso');
insert into act_process_status(process_status_desc) values('Religa efetuado com sucesso');
insert into act_process_status(process_status_desc) values('Leitura processada com sucesso');
insert into act_process_status(process_status_desc) values('Erro comando invalido ou não existe');
insert into act_process_status(process_status_desc) values('Erro usuário não cadastrado');

commit;




--criando tabela para armazenar historicos de comandos
create table act_msg_history(
   msg_history_id int primary key not null auto_increment,
   msg_history_rec_id int not null,
   msg_history_proc_status int not null,
   msg_history_date datetime not null
);

alter table act_msg_history
add constraint fk_msg_history_rec
foreign key(msg_history_rec_id)
references act_rec_msg(rec_msg_id);

alter table act_msg_history
add constraint fk_msg_history_pro_status
foreign key(msg_history_proc_status)
references act_process_status(process_status_id);


commit;


