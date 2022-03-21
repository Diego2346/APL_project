#pragma once
#ifndef DB_H_
#define DB_H_

#include <string>
#include <mysql.h>
#include <vector>
#include <iostream>
#include <exception>

typedef std::vector<std::string> lista;

class db {

public:

	db();

	~db();

	void setConn(MYSQL* conn);
	void setResult(MYSQL_RES* result);
	void setRow(MYSQL_ROW row);

	MYSQL* getConn();
	MYSQL_RES* getResult();
	MYSQL_ROW getRow();



	//first init
	//void init();
	void close(MYSQL* conn);

	//connect without db already created
	void connect(MYSQL* conn, std::string host, std::string user, std::string password, int port);
	//connect if db already created
	void connect(MYSQL* conn, std::string host, std::string user, std::string password, int port, std::string db);
	//optional create a db
	void createDB(MYSQL* conn, std::string db);

	//query without retruning
	void queryDB(MYSQL* conn, std::string query);

	//query with returning values from db
	std::vector<lista> queryDB(MYSQL* conn, std::string query, bool insert);


	MYSQL* m_conn;
	MYSQL_RES* m_result;
	MYSQL_ROW m_row;
};

#endif