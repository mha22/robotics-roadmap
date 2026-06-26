#include <iostream>

void doubleSpeed(int& speed) {
    speed = speed * 2;   
}

void doubleCopy(int speed) {
    speed = speed * 2;  
}

int main() {
    int x = 5;

    int& ref = x;       
    ref = 10;
    std::cout << "x after ref: " << x << std::endl;  

    int* ptr = &x;       
    std::cout << "Address of x: " << ptr << std::endl;
    std::cout << "Value via ptr: " << *ptr << std::endl;  
    *ptr = 20;          
    std::cout << "x after ptr: " << x << std::endl;  

    int speed = 100;
    doubleCopy(speed);
    std::cout << "After doubleCopy: " << speed << std::endl;  
    doubleSpeed(speed);
    std::cout << "After doubleSpeed: " << speed << std::endl; 

    return 0;
}
