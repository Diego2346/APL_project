#include "pch.h"
#include "Istruttore.h"

Istruttore::Istruttore(int instructorId, std::string name, std::string surname) : m_instructorId(instructorId), m_name(name), m_surname(surname) {}
Istruttore::Istruttore(std::string name, std::string surname) : m_name(name), m_surname(surname) {
	m_instructorId = -1;
}
Istruttore::~Istruttore() {}

bool Istruttore::operator==(const Istruttore& other) { return false; }
bool Istruttore::operator!=(const Istruttore& other) { return false; }

int Istruttore::getInstructorId() const {
	return m_instructorId;
}
std::string Istruttore::getName() const {
	return m_name;
}
std::string Istruttore::getSurname() const {
	return m_surname;
}

void Istruttore::setInstructorId(int instructorId) {
	m_instructorId = instructorId;
}
void Istruttore::setName(std::string name) {
	m_name = name;
}
void Istruttore::setSurname(std::string surname) {
	m_surname = surname;
}