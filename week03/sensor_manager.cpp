#include <string>
#include <iostream>

class SensorBase {
protected:
    std::string name_;
    int id_;

public:
    SensorBase(int id, std::string name) : id_(id), name_(name) {
        std::cout << "Sensor " << name_ << " created\n";
    }

    virtual double read() const = 0;

    virtual void print() const {
        std::cout << "Sensor ID: " << id_
        << ", Name: " << name_
        << "\n";
    }

    virtual ~SensorBase() {
        std::cout << "Sensor " << name_ << " destroyed\n";
    }
};

class LaserSensor : public SensorBase {
public:
    LaserSensor(int id) : SensorBase(id, "Laser") {}

    double read() const override {
        return 2.5;
    }
};

class IMUSensor : public SensorBase {
public:
    IMUSensor(int id) : SensorBase(id, "IMU") {}

    double read() const override {
        return 9.8;
    }
};


int main() {

    SensorBase *sensors[2];
    sensors[0] = new LaserSensor(54);
    sensors[1] = new IMUSensor(12);

    for (auto sensor : sensors) {
        sensor->print();
        std::cout << "Reading: " << sensor->read() << "\n";
    }

    for (auto sensor : sensors) {
        delete sensor;
    }
    return 0;
}
