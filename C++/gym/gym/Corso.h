#pragma once

#ifndef CORSO_H_
#define CORSO_H_

#include <string>

class Corso{
public:
	Corso(std::string courseName, std::string days, double monthlyCost, int instructorId);
	~Corso();

	bool operator==(const Corso& other);
	bool operator!=(const Corso& other);

	std::string getCourseName() const;
	std::string getDays() const;
	double getMonthlyCost() const;
	int getInstructorId() const;

	void setCourseName(std::string courseName);
	void setDays(std::string days);
	void setMonthlyCost(double monthlyCost);
	void setInstructorId(int instructorId);

private:

	std::string m_courseName;
	std::string m_days;
	double m_monthlyCost;
	int m_instructorId;

};

#endif