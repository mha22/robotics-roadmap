#include <iostream>
#include <string>

int main() {
    int speed = 10;
    double voltage = 3.7;
    char grade = 'A';
    bool active = true;
    std::string name = "AGV-1";

    std::cout << "Robot: " << name << std::endl;
    std::cout << "Speed: " << speed << " m/s" << std::endl;
    std::cout << "Voltage: " << voltage << " V" << std::endl;

    int newSpeed;
    std::cout << "Enter new speed:";
    std::cin >> newSpeed;
    std::cout << "New speed set to " << newSpeed << " m/s" << std::endl;

    return 0;
}

