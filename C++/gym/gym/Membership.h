#pragma once
#ifndef MEMBERSHIP_H_
#define MEMBERSHIP_H_
#include <string>


class Membership
{
public:
	Membership(std::string courseName, int userId);
	~Membership();

	bool operator==(const Membership& other);
	bool operator!=(const Membership& other);

	std::string getCourseName() const;
	int getUserId() const;

	void setCourseName(std::string courseName);
	void setUserId(int userId);
private:
	std::string m_courseName;
	int m_userId;
};

#endif