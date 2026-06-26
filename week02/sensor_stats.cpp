#include <iostream>

void analyze(double data[], int size, double& maxVal, double& minVal, double& avg) {
    maxVal = data[0];
    minVal = data[0];
    double sum = 0.0;

    for (int i = 0; i < size; i++) {
        if (data[i] > maxVal) {
            maxVal = data[i];
        }
        if (data[i] < minVal) {
            minVal = data[i];
        }
        sum += data[i];
    }

    avg = sum / size;
}

int main() {
    double readings[] = {12.5, 9.0, 15.2, 7.8, 20.1, 11.3, 18.6, 8.4};
    int size = 8;

    double maxVal, minVal, avg;
    analyze(readings, size, maxVal, minVal, avg);

    std::cout << "Max: " << maxVal << std::endl;
    std::cout << "Min: " << minVal << std::endl;
    std::cout << "Average: " << avg << std::endl;

    return 0;
}
