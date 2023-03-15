-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY(id), state_id FOREIGN KEY(state_id) REFERENCES states(id) NOT NULL, name VARCHAR (256) NOT NULL);