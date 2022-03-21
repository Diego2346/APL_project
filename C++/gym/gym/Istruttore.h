#pragma once
#ifndef ISTRUTTORE_H_
#define ISTRUTTORE_H_

#include <string>


class Istruttore{
public:
	Istruttore(int instructorId, std::string name, std::string surname);
	Istruttore(std::string name, std::string surname);
	~Istruttore();

	bool operator==(const Istruttore& other);
	bool operator!=(const Istruttore& other);

	int getInstructorId() const;
	std::string getName() const;
	std::string getSurname() const;

	void setInstructorId(int instructorId);
	void setName(std::string name);
	void setSurname(std::string surname);


private:
	int m_instructorId;
	std::string m_name;
	std::string m_surname;
};

#endif
