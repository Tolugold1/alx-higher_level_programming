-- Create a database and grant select persion only to it's table
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXIXTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANTS SELECT ON hbtn_0d_2.* TO user_0d_2;
