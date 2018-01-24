/*
Autor:Diego Lopes da Silva
Data:30/11/2017
Descrição:update na tabela act_process_status e adicionando campo para tabela act_msg_history
*/

--update na tabela act_process_status
update act_process_status
set process_status_desc='Religa efetuado com sucesso'
where process_status_id=1;

update act_process_status
set process_status_desc='Corte efetuado com sucesso'
where process_status_id=2;


--adicionando campo registro de ip
alter table act_msg_history add act_msg_ip varchar(100) not null;
