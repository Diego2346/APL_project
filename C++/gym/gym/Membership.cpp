#include "pch.h"
#include "Membership.h"

Membership::Membership(std::string courseName, int userId) : m_courseName(courseName), m_userId(userId) {}
Membership::~Membership() {}

bool Membership::operator==(const Membership& other) { return false; }
bool Membership::operator!=(const Membership& other) { return false; }

std::string Membership::getCourseName() const {
	return m_courseName;
}

int Membership::getUserId() const {
	return m_userId;
}

void Membership::setCourseName(std::string courseName) {
	m_courseName = courseName;
}
void Membership::setUserId(int userId) {
	m_userId = userId;
}
