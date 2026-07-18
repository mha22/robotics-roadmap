# ROS 2 Services Practice

A small ROS 2 practice project for learning service based communication using Python and custom interfaces.

This project demonstrates how to create a custom service interface, implement a service server, implement a service client, and test the service from the ROS 2 command line.

## Goal

The goal of this project is to understand the difference between topics and services in ROS 2.

Topics are used for continuous one way data flow.

Services are used for request response communication, similar to calling a remote function.

This project uses a simple `AddTwoInts` service. The client sends two integer values, and the server returns their sum.

## Concepts Covered

- ROS 2 Python packages
- Custom service interfaces
- Service server
- Service client
- Asynchronous service calls
- `colcon` build workflow
- ROS 2 command line testing

## Project Structure
```text
ros2-service-practice/
├── custom_interfaces/
│   ├── srv/
│   │   └── AddTwoInts.srv
│   ├── CMakeLists.txt
│   └── package.xml
├── py_pubsub/
│   ├── py_pubsub/
│   │   ├── add_server.py
│   │   └── add_client.py
│   ├── setup.py
│   └── package.xml
└── README.md
```

## Service Interface

The custom service is defined in:

```text
custom_interfaces/srv/AddTwoInts.srv
```
Service definition:

```srv
int64 a
int64 b
---
int64 sum
```
The fields above `---` are the request fields.

The fields below `---` are the response fields.

## Build

From the ROS 2 workspace root:

```bash
cd ~/ros2_ws
colcon build
```
Source the workspace:

```bash
source install/setup.zsh
```
If you use bash:

```bash
source install/setup.bash
```
## Build Only The Interface Package

```bash
cd ~/ros2_ws
colcon build --packages-select custom_interfaces
source install/setup.zsh
```
Check the service interface:

```bash
ros2 interface show custom_interfaces/srv/AddTwoInts
```
Expected output:

```text
int64 a
int64 b
---
int64 sum
```
## Build The Python Package

```bash
cd ~/ros2_ws
colcon build --packages-select py_pubsub
source install/setup.zsh
```
## Run The Service Server

Open a terminal and run:

```bash
ros2 run py_pubsub add_server
```
Expected output:

```text
[INFO] [add_server]: Server is ready.
```
## Run The Service Client

Open another terminal and run:

```bash
ros2 run py_pubsub add_client 5 7
```
Expected output:

```text
[INFO] [add_client]: Result: 5 + 7 = 12
```
## Test With ROS 2 CLI

The service can also be called without the Python client:

```bash
ros2 service call /add_two_ints custom_interfaces/srv/AddTwoInts "{a: 10, b: 20}"
```
Expected response:

```text
sum: 30
```
List active services:

```bash
ros2 service list
```
## How It Works

The server creates a service named `add_two_ints`.

The client waits until the service is available.

The client sends two integer values in a request.

The server receives the request, calculates the sum, and sends the result back as a response.

The client uses `call_async()` to send the request asynchronously.

Then `spin_until_future_complete()` waits until the response is received.

## Example Commands

Terminal 1:

```bash
source ~/ros2_ws/install/setup.zsh
ros2 run py_pubsub add_server
```
Terminal 2:

```bash
source ~/ros2_ws/install/setup.zsh
ros2 run py_pubsub add_client 15 25
```
Expected result:

```text
Result: 15 + 25 = 40
```
## What I Learned

In this project, I practiced:

- creating a custom ROS 2 service
- generating interfaces with `rosidl`
- writing a Python service server
- writing a Python service client
- using asynchronous service calls
- testing services with the ROS 2 CLI
- building ROS 2 packages with `colcon`

## Next Steps

Possible improvements:

1. Add input validation to the client
2. Add more custom services
3. Add launch files
4. Add ROS 2 actions
5. Add screenshots or terminal output examples
6. Add GitHub Actions for basic build checks

## Notes

This repository is part of my ROS 2 learning path.

The goal is to build a clear learning history and demonstrate practical understanding of ROS 2 communication patterns.
