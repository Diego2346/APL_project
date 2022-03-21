#include "pch.h"
#include "Corso.h"

Corso::Corso(std::string courseName, std::string days, double monthlyCost, int instructorId) : m_courseName(courseName), m_days(days), m_monthlyCost(monthlyCost), m_instructorId(instructorId) {}
Corso::~Corso() {}

bool Corso::operator==(const Corso& other) { return false; }
bool Corso::operator!=(const Corso& other) { return false; }

std::string Corso::getCourseName() const {
	return m_courseName;
}
std::string Corso::getDays() const {
	return m_days;
}
double Corso::getMonthlyCost() const {
	return m_monthlyCost;
}
int Corso::getInstructorId() const {
	return m_instructorId;
}

void Corso::setCourseName(std::string courseName) {
	m_courseName = courseName;
}
void Corso::setDays(std::string days) {
	m_days = days;
}
void Corso::setMonthlyCost(double monthlyCost) {
	m_monthlyCost = monthlyCost;
}
void Corso::setInstructorId(int instructorId) {
	m_instructorId = instructorId;
}