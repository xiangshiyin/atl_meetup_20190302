-- create database
CREATE DATABASE adhoc;

-- create table
DROP TABLE IF EXISTS adhoc.word_count;
CREATE TABLE adhoc.word_count (
    word VARCHAR(255) NOT NULL,
    freq INT NOT NULL,
    PRIMARY KEY (word)
);

-- load data
--------need config in /usr/local/etc/my.cnf on mac osx
LOAD DATA INFILE '/Users/xyin/Documents/self/atl_meetup_20190302/data/word_count_out.csv' 
INTO TABLE adhoc.word_count
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 0 ROWS;


