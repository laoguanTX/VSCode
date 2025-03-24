#include "Animal.h"

Animal::Animal(int age, int weight, std::string name, int id) {
    this->age = age;
    this->weight = weight;
    this->name = name;
    this->id = id;
    this->health = 50;
}
void Animal::eat() {
    weight++;
    health += 10;
}
void Animal::sleep() {
    age++;
    health += 5;
}
void Animal::move() {
    weight--;
    health -= 5;
}
void Animal::harm() {
    health -= 10;
}