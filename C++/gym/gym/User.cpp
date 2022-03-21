#include "pch.h"
#include "User.h"


User::User(int userId, std::string nome, std::string cognome, char gender, std::string indirizzo, std::string dataNascita, std::string email, std::string username, std::string password, std::string dataIscrizione) : m_userId(userId), m_nome(nome), m_cognome(cognome), m_gender(gender), m_indirizzo(indirizzo), m_dataNascita(dataNascita), m_email(email), m_username(username), m_password(password), m_dataIscrizione(dataIscrizione){
}
User::User(std::string nome, std::string cognome, char gender, std::string indirizzo, std::string dataNascita, std::string email, std::string username, std::string password) : m_nome(nome), m_cognome(cognome), m_gender(gender), m_indirizzo(indirizzo), m_dataNascita(dataNascita), m_email(email), m_username(username), m_password(password){
	m_userId = -1;
}
User::~User() {}

bool User::operator==(const User& other) { return false; }
bool User::operator!=(const User& other) { return false; }

int User::getUserId() const {
	return m_userId;
}

std::string User::getEmail() const {
	return m_email;
}

std::string User::getCognome() const {
	return m_cognome;
}

std::string User::getIndirizzo() const {
	return m_indirizzo;
}

std::string User::getDataNascita() const {
	return m_dataNascita;
}

std::string User::getUsername() const {
	return m_username;
}

std::string User::getNome() const {
	return m_nome;
}

std::string User::getPassword() const {
	return m_password;
}

std::string User::getDataIscrizione() const {
	return m_dataIscrizione;
}

std::string User::getAttivazione() const {
	return m_attivazione;
}


char User::getGender() const {
	return m_gender;
}

void User::setUserId(int userId) {
	m_userId = userId;
}
void User::setCognome(std::string cognome) {
	m_cognome = cognome;
}

void User::setIndirizzo(std::string indirizzo) {
	m_indirizzo = indirizzo;
}
void User::setDataNascita(std::string dataNascita) {
	m_dataNascita = dataNascita;
}

void User::setUsername(std::string username) {
	m_username = username;
}

void User::setEmail(std::string email) {
	m_email = email;
}

void User::setNome(std::string nome) {
	m_nome = nome;
}

void User::setPassword(std::string password) {
	m_password = password;
}

void User::setDataIscrizione(std::string dataIscrizione) {
	m_dataIscrizione = dataIscrizione;
}

void User::setAttivazione(std::string attivazione) {
	m_attivazione = attivazione;
}

void User::setGender(char gender) {
	m_gender = gender;
}