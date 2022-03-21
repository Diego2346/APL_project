// dllmain.cpp : Definisce il punto di ingresso per l'applicazione DLL.
#include "pch.h"
#include <iostream>
#include <list>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include <boost/python/return_internal_reference.hpp>
#include <mysql.h>
#include "db.h"
#include "User.h"
#include "Admin.h"
#include "Istruttore.h"
#include "Membership.h"
#include "Corso.h"




using namespace std;

User* validateUser(db DB, string username, string password) {
    string query = "select * from users where username = '" + username + "' and password = '" + password + "' and users.user_id NOT IN (SELECT admin_id FROM admins)";
    vector<lista> listUser = DB.queryDB(DB.getConn(), query, true);
    if (listUser.empty())
        return nullptr;

    lista list = listUser[0];
    User* user = new User(stoi(list[0]), list[1], list[2], list[3][0], list[4], list[5], list[6], list[7], list[8], list[9]);
    return user;
}

Admin* validateAdmin(db DB, string username, string password) {
    string query = "select * from users,admins where username = '" + username + "' and password = '" + password + "'and users.user_id = admins.admin_id ";
    vector<lista> listAdmin = DB.queryDB(DB.getConn(), query, true);
    if (listAdmin.empty())
        return nullptr;

    lista list = listAdmin[0];

    Admin* admin = new Admin(stoi(list[0]), list[1], list[2], list[3][0], list[4], list[5], list[6], list[7], list[8], list[9], true);
    return admin;
}

vector<User> getAllUsers(db DB) {
    string query = "select * from users where users.user_id NOT IN (SELECT admin_id FROM admins)";
    vector<lista> list = DB.queryDB(DB.getConn(), query, true);
    vector<User> userList;
    for (auto it = list.begin(); it != list.end(); ++it) {
        User* user = new User(stoi((*it)[0]), (*it)[1], (*it)[2], (*it)[3][0], (*it)[4], (*it)[5], (*it)[6], (*it)[7], (*it)[8], (*it)[9]);
        userList.push_back(*user);
    }
    return userList;
}

void createAdmin(Admin admin, db DB) {
    string nome(admin.getNome());
    string cognome(admin.getCognome());
    string email(admin.getEmail());
    string indirizzo(admin.getIndirizzo());
    string dataNascita(admin.getDataNascita());
    string password(admin.getPassword());
    string username(admin.getUsername());
    string gender(1, admin.getGender());
    string query = "INSERT INTO users (name, surname, gender, address, birth_date, email, username, password) VALUES('" + nome + "', '" +
        cognome + "', '" + gender + "', '" + indirizzo + "', '" + dataNascita + "', '" + email + "', '" + username + "', '" + password + "')";
    DB.queryDB(DB.getConn(), query);
    query = "INSERT INTO admins (admin_id)  SELECT MAX(user_id) FROM users";
    DB.queryDB(DB.getConn(), query);
}


void createUser(User user, db DB) {
    string query = "SELECT * FROM users";
    lista list = DB.queryDB(DB.getConn(), query, true).back();

    string nome(user.getNome());
    string cognome(user.getCognome());
    string email(user.getEmail());
    string indirizzo(user.getIndirizzo());
    string dataNascita(user.getDataNascita());
    string password(user.getPassword());
    string username(user.getUsername());
    string gender(1, user.getGender());
    query = "INSERT INTO users (name, surname, gender, address, birth_date, email, username, password) VALUES('" + nome + "', '" +
        cognome + "', '" + gender + "', '" + indirizzo + "', '" + dataNascita + "', '" + email + "', '" + username + "', '" + password + "')";
    DB.queryDB(DB.getConn(), query);
}

void removeUser(int userId, db DB) {
    string query = "DELETE FROM users WHERE user_id = " + to_string(userId);
    DB.queryDB(DB.getConn(), query);

}

void modifyUser(int userId, string email, string username, string password, db DB) {
    string query = "UPDATE users SET email = '" + email + "',username = '" + username + "', password = '" + password + "' WHERE user_id = " + to_string(userId) + "";
    DB.queryDB(DB.getConn(), query);

}

void createInstructor(Istruttore istruttore, db DB) {
    string name = istruttore.getName();
    string surname = istruttore.getSurname();
    string query = "INSERT INTO instructors(name, surname) VALUES('" + name + "', '" + surname + "')";
    DB.queryDB(DB.getConn(), query);
}

void removeInstructor(int instructorId, db DB) {
    string instructorID = to_string(instructorId);
    string query = "DELETE FROM instructors WHERE instructor_id = " + instructorID;
    DB.queryDB(DB.getConn(), query);

}

vector<Istruttore> getAllInstructors(db DB) {
    string query = "select * from instructors";
    vector<lista> list = DB.queryDB(DB.getConn(), query, true);
    vector<Istruttore> instructorList;
    for (auto it = list.begin(); it != list.end(); ++it) {
        Istruttore* istruttore = new Istruttore(stoi((*it)[0]), (*it)[1], (*it)[2]);
        instructorList.push_back(*istruttore);
    }
    return instructorList;
}

void removeCourse(string courseName, db DB) {
    string query = "DELETE FROM courses WHERE course_name = '" + courseName + "'";
    DB.queryDB(DB.getConn(), query);
}

void createCourse(Corso corso, db DB) {
    string courseName = corso.getCourseName();
    string days = corso.getDays();
    string monthlyCost = to_string(corso.getMonthlyCost());
    string instructorId = to_string(corso.getInstructorId());
    string query = "INSERT INTO courses(course_name, days, monthly_cost, instructor_id) VALUES('" + courseName + "', '" + days + "', " + monthlyCost + ", " + instructorId + ")";
    DB.queryDB(DB.getConn(), query);
}

vector<Corso> getAllCourses(db DB) {
    string query = "select * from courses";
    vector<lista> list = DB.queryDB(DB.getConn(), query, true);
    vector<Corso> courseList;
    for (auto it = list.begin(); it != list.end(); ++it) {
        Corso* corso = new Corso((*it)[0], (*it)[1], stod((*it)[2]), stoi((*it)[3]));
        courseList.push_back(*corso);
    }
    return courseList;
}

void createMembership(Membership membership, db DB) {
    string courseName = membership.getCourseName();
    string userId = to_string(membership.getUserId());
    string query = "INSERT INTO membership(user_id, course_name) VALUES('" + userId + "', '" + courseName + "')";
    DB.queryDB(DB.getConn(), query);
}

void removeMembership(int userId, string courseName, db DB) {
    string query = "DELETE FROM membership WHERE course_name = '" + courseName + "'and user_id='" + (to_string(userId)) + "'";
    DB.queryDB(DB.getConn(), query);
}

vector<Membership> getAllMemberships(db DB) {
    string query = "select * from membership";
    vector<lista> list = DB.queryDB(DB.getConn(), query, true);
    vector<Membership> membershipList;
    for (auto it = list.begin(); it != list.end(); ++it) {
        Membership* membership = new Membership(((*it)[0]), stoi((*it)[1]));
        membershipList.push_back(*membership);
    }
    return membershipList;

}



using namespace boost::python;
BOOST_PYTHON_MODULE(gym) {

    class_<lista>("lista").def(vector_indexing_suite<lista>());
    class_<vector<User>>("userList").def(vector_indexing_suite<vector<User>>());
    class_<vector<Corso>>("courseList").def(vector_indexing_suite<vector<Corso>>());
    class_<vector<Istruttore>>("instructorList").def(vector_indexing_suite<vector<Istruttore>>());
    class_<vector<Membership>>("membershipList").def(vector_indexing_suite<vector<Membership>>());
    class_<MYSQL>("MYSQL");

    def("validateUser", validateUser, return_internal_reference<>());
    def("validateAdmin", validateAdmin, return_internal_reference<>());
    def("createUser", createUser);
    def("createAdmin", createAdmin);
    def("createInstructor", createInstructor);
    def("createCourse", createCourse);
    def("createMembership", createMembership);
    def("removeUser", removeUser);
    def("removeInstructor", removeInstructor);
    def("removeCourse", removeCourse);
    def("removeMembership", removeMembership);
    def("modifyUser", modifyUser);
    def("getAllUsers", getAllUsers);
    def("getAllInstructors", getAllInstructors);
    def("getAllCourses", getAllCourses);
    def("getAllMemberships", getAllMemberships);

    class_<Admin, boost::noncopyable>("Admin", init<string, string, char, string, string, string, string, string, bool>())
        .add_property("userId", &Admin::getUserId, &Admin::setUserId)
        .add_property("nome", &Admin::getNome, &Admin::setNome)
        .add_property("cognome", &Admin::getCognome, &Admin::setCognome)
        .add_property("email", &Admin::getEmail, &Admin::setEmail)
        .add_property("indirizzo", &Admin::getIndirizzo, &Admin::setIndirizzo)
        .add_property("username", &Admin::getUsername, &Admin::setUsername)
        .add_property("password", &Admin::getPassword, &Admin::setPassword)
        .add_property("dataDiNascita", &Admin::getDataNascita, &Admin::setDataNascita)
        .add_property("isAdmin", &Admin::getIsAdmin, &Admin::setIsAdmin)
        .add_property("dataIscrizione", &Admin::getDataIscrizione, &Admin::setDataIscrizione)
        .add_property("gender", &Admin::getGender, &Admin::setGender);

    class_<db, boost::noncopyable>("db")
        .def(init<>())
        .def("close", &db::close)
        .def<void (db::*)(MYSQL*, string, string, string, int)>("connectHost", &db::connect)
        .def<void (db::*)(MYSQL*, string, string, string, int, string)>("connectDB", &db::connect)
        .def("createDB", &db::createDB)
        .def<void (db::*)(MYSQL*, string)>("insertDB", &db::queryDB)
        .def<vector<lista>(db::*)(MYSQL*, string, bool)>("queryDB", &db::queryDB)
        .def("getConn", &db::getConn, return_internal_reference<>())
        .def("getResult", &db::getResult, return_internal_reference<>())
        .def("setRow", &db::setRow)
        .def("setResult", &db::setResult);

    class_<User, boost::noncopyable>("User", init<string, string, char, string, string, string, string, string>())
        .add_property("userId", &User::getUserId, &User::setUserId)
        .add_property("nome", &User::getNome, &User::setNome)
        .add_property("cognome", &User::getCognome, &User::setCognome)
        .add_property("email", &User::getEmail, &User::setEmail)
        .add_property("indirizzo", &User::getIndirizzo, &User::setIndirizzo)
        .add_property("username", &User::getUsername, &User::setUsername)
        .add_property("password", &User::getPassword, &User::setPassword)
        .add_property("dataDiNascita", &User::getDataNascita, &User::setDataNascita)
        .add_property("dataIscrizione", &User::getDataIscrizione, &User::setDataIscrizione)
        .add_property("gender", &User::getGender, &User::setGender);

    class_<Istruttore, boost::noncopyable>("Istruttore", init<string, string>())
        .add_property("instructorId", &Istruttore::getInstructorId, &Istruttore::setInstructorId)
        .add_property("name", &Istruttore::getName, &Istruttore::setName)
        .add_property("surname", &Istruttore::getSurname, &Istruttore::setSurname);

    class_<Corso, boost::noncopyable>("Corso", init<string, string, double, int>())
        .add_property("courseName", &Corso::getCourseName, &Corso::setCourseName)
        .add_property("days", &Corso::getDays, &Corso::setDays)
        .add_property("monthlyCost", &Corso::getMonthlyCost, &Corso::setMonthlyCost)
        .add_property("instructorId", &Corso::getInstructorId, &Corso::setInstructorId);

    class_<Membership, boost::noncopyable>("Membership", init<string, int>())
        .add_property("courseName", &Membership::getCourseName, &Membership::setCourseName)
        .add_property("userId", &Membership::getUserId, &Membership::setUserId);
}