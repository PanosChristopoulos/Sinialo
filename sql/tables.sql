CREATE DATABASE sinialo;
USE sinialo;

CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    country_ISO VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE countries(
	country_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	country_ISO VARCHAR(50) NOT NULL ,
   	country_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE cities(
	city_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    	city_name VARCHAR(100) NOT NULL,
   	country_id INT NOT NULL,
CONSTRAINT cityCountry FOREIGN KEY (country_id) REFERENCES `countries`(country_id) ON DELETE CASCADE ON UPDATE CASCADE
);
