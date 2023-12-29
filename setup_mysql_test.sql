-- This script prepares a MySQL server for the project
-- Create project defining database with the name : sacco_test_db
CREATE DATABASE IF NOT EXISTS sacco_test_db ;

-- Create a new user named : sacco_test with all priveledges on the db sacco_test_db
-- with the password : sacco_test_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'sacco_test'@'localhost' IDENTIFIED BY 'sacco_test_pwd';

-- Granting all priviledges to the new user
GRANT ALL PRIVILEGES ON sacco_test_db.* TO 'sacco_test'@'localhost';
FLUSH PRIVILEGES;

-- Granting the SELECT priviledge for the user sacco_test in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'sacco_test'@'localhost';
FLUSH PRIVILEGES;
