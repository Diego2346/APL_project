#include "pch.h"
#include "db.h"
typedef std::vector<std::string> lista;

db::db() {
	m_conn = mysql_init(NULL);
}

db::~db() {}

void db::setConn(MYSQL* conn) {
	m_conn = conn;
}
void db::setResult(MYSQL_RES* result) {
	m_result = result;
}
void db::setRow(MYSQL_ROW row) {
	m_row = row;
}

MYSQL* db::getConn() {
	return m_conn;
}
MYSQL_RES* db::getResult() {
	return m_result;
}
MYSQL_ROW db::getRow() {
	return m_row;
}



void db::close(MYSQL* conn) {
	mysql_close(conn);
}

//connect without db already created
void db::connect(MYSQL* conn, std::string host, std::string user, std::string password, int port) {
	if (mysql_real_connect(conn, host.c_str(), user.c_str(), password.c_str(), NULL, port, NULL, 0) == NULL)
	{
		throw std::runtime_error("Connection Error with the db");
		mysql_close(conn);
		exit(1);
	}
}


//connect if db already created
void db::connect(MYSQL* conn, std::string host, std::string user, std::string password, int port, std::string db) {
	if (mysql_real_connect(conn, host.c_str(), user.c_str(), password.c_str(), db.c_str(), port, NULL, 0) == NULL)
	{
		throw std::runtime_error("Connection Error with the db");
		mysql_close(conn);
		exit(1);
	}
}


//optional create a db
void db::createDB(MYSQL* conn, std::string db) {
	std::string query = "CREATE DATABASE " + db;
	if (mysql_query(conn, query.c_str()) == NULL)
	{
		std::string error = "unable to create db with name " + db;
		throw std::runtime_error(error);
		mysql_close(conn);
		exit(1);
	}
}

//query without retruning
void db::queryDB(MYSQL* conn, std::string query) {
	if (mysql_query(conn, query.c_str()))
	{
		std::string error = "unable to query db with name " + std::string(conn->db) + "; query: " + std::string(query);
		throw std::runtime_error(error);
		mysql_close(conn);
	}
}

//query with returning values from db
std::vector<lista> db::queryDB(MYSQL* conn, std::string query, bool insert) {
	if (mysql_query(conn, query.c_str()))
	{
		std::string error = "unable to query db with name " + std::string(conn->db) + "; query: " + std::string(query);
		std::cout << error << std::endl;
		throw std::runtime_error(error);
		mysql_close(conn);
		exit(1);
	}
	m_result = mysql_store_result(conn);
	unsigned int num_fields = mysql_num_fields(m_result);;
	std::vector<lista> last;
	lista fields;
	while ((m_row = mysql_fetch_row(m_result)))
	{
		for (unsigned int i = 0; i < num_fields; i++)
			fields.push_back(m_row[i]);
		last.push_back(fields);
		fields.clear();
	}
	return last;

}
