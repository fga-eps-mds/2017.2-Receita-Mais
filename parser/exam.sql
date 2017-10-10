/*
Target Server         : Postgres
Target Table          : Exam

Date: 2017-10-10
*/
\copy exam(id_tuss, description) FROM 'TUSS.txt' DELIMITER ',' CSV;
