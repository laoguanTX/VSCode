#ifndef _ANIMAL_H
#define _ANIMAL_H

#include <iostream>
#include <string>

class Animal {
    public:
        int age, weight;
        std::string name;
        Animal(int age, int weight, std::string name, int id);
        void eat();
        void sleep();
        void move();
        void harm();

    protected:
        int health;

    private:
        int id;
};

#endif // _ANIMAL_H