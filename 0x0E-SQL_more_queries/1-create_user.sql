-- Script that creates the MySQL server user user_0d_1.
-- GRANT statement to grant privileges to user accounts.
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
FLUSH PRIVILEGES;
