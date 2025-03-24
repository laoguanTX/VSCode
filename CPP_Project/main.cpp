#include <iostream>
#include <string>
#include <windows.h>
#include "Animal.h"
#include "Dog.h"

int main() {
    Dog dog(5, 10, "Dog", 1);
    dog.eat();
    dog.sleep();
    std::cout << dog.name << std::endl;
    std::cout << dog.age << " " << dog.weight << std::endl;
    dog.bark();
    dog.wagTail();
    return 0;
}