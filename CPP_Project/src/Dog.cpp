#include "Dog.h"

Dog::Dog(int age, int weight, std::string name, int id) : Animal(age, weight, name, id) {}
void Dog::bark() {
    std::cout << "Woof!" << std::endl;
    return;
}
void Dog::wagTail() {
    std::cout << "Wagging tail..." << std::endl;
    return;
}
