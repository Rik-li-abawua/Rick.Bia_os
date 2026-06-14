CREATE TABLE conversation_memory(id TEXT PRIMARY KEY,user_id TEXT,content TEXT,created_at TIMESTAMP);
CREATE TABLE user_preferences(id TEXT PRIMARY KEY,user_id TEXT,key TEXT,value TEXT);
CREATE TABLE agent_history(id TEXT PRIMARY KEY,agent_name TEXT,input TEXT,output TEXT,created_at TIMESTAMP);
