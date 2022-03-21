#include "pch.h"
#include "Admin.h"

Admin::Admin(std::string nome, std::string cognome, char gender, std::string indirizzo, std::string dataNascita, std::string email, std::string username, std::string password, bool isAdmin) : User(nome, cognome, gender, indirizzo, dataNascita, email, username, password), m_isAdmin(isAdmin) {
	m_userId = -1;
}
Admin::Admin(int userId, std::string nome, std::string cognome, char gender, std::string indirizzo, std::string dataNascita, std::string email, std::string username, std::string password, std::string dataIscrizione, bool isAdmin) : User(userId, nome, cognome, gender, indirizzo, dataNascita, email, username, password, dataIscrizione), m_isAdmin(isAdmin) {}
Admin::~Admin() {}

bool Admin::operator==(const Admin& other) { return false; }
bool Admin::operator!=(const Admin& other) { return false; }

void Admin::setIsAdmin(bool isAdmin) {
	m_isAdmin = isAdmin;
}

bool Admin::getIsAdmin() const {
	return m_isAdmin;
}