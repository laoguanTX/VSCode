#ifndef _DOG_H
#define _DOG_H

#include <iostream>
#include <string>
#include "Animal.h"

class Dog : public Animal {
    public:
        Dog(int age, int weight, std::string name, int id);
        void bark();
        void wagTail();
};

#endif // _DOG_H