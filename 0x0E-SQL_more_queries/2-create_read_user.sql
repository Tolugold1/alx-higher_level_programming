-- create a database and table and give only select permission
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = PASSWORD('user_0d_2_pwd');
GRANT SELECT ON user_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
