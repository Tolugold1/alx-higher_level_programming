-- Create a user account and grant all permission.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1_pwd';
GRANT ALL FROM *.* TO user_0d_1;
FLUSH PRIVILEGES;
