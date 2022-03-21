#pragma once
#ifndef ADMIN_H_
#define ADMIN_H_
#include "User.h"

class Admin : public User {
public:
	Admin(std::string nome, std::string cognome, char gender, std::string indirizzo, std::string dataNascita, std::string email, std::string username, std::string password, bool isAdmin);
	Admin(int userId, std::string nome, std::string cognome, char gender, std::string indirizzo, std::string dataNascita, std::string email, std::string username, std::string password, std::string dataIscrizione, bool isAdmin);
	~Admin();

	bool operator==(const Admin& other);
	bool operator!=(const Admin& other);

	void setIsAdmin(bool isAdmin);
	bool getIsAdmin() const;

private:
	bool m_isAdmin;
};

#endif