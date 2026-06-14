CREATE TABLE users(id TEXT PRIMARY KEY,name TEXT,email TEXT);
CREATE TABLE investments(id TEXT PRIMARY KEY,user_id TEXT,ticker TEXT,quantity REAL);
CREATE TABLE passengers(id TEXT PRIMARY KEY,user_id TEXT,passenger_name TEXT);
