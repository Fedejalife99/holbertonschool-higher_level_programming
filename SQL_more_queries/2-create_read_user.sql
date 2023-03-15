--  create a database named hbtn_od_2, create an user and give him READ the privileges 
CREATE DATABASE hbtn_0d_2 IF NOT EXISTS;
CREATE USER IF NOT EXISTS 'user_0d_2'@'hbtn_od_2' IDENTIFIED BY 'user_0d_2_pwd';
GRANT READ PRIVILEGES ON *.* TO 'user_0d_2'@'hbtn_0d_2';