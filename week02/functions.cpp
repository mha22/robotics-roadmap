#include <iostream>

double average(double a, double b) {
    return (a + b) / 2.0;
}

void printStatus(int speed) {
    if (speed > 0) {
        std::cout << "Moving at " << speed << " m/s" << std::endl;
    } else {
        std::cout << "Stopped" << std::endl;
    }
}

int main() {
    double avg = average(10.0, 20.0);
    std::cout << "Average: " << avg << std::endl;

    printStatus(5);
    printStatus(0);

    return 0;
}
