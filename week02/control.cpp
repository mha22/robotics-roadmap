#include <iostream>

int main() {
    for (int i = 0; i < 5; i++) {
        std::cout << "Sample " << i << std::endl;
    }

    int battery = 100;
    while (battery > 20) {
        std::cout << "Battery: " << battery << "%" << std::endl;
        battery -= 30;  
    }

    // شرط
    if (battery <= 20) {
        std::cout << "Warning: low battery!" << std::endl;
    } else {
        std::cout << "Battery OK" << std::endl;
    }

    return 0;
}
