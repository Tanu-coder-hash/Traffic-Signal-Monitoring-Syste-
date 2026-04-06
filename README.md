Smart Traffic Monitoring System

A multi-client smart traffic monitoring system built using Python and TCP socket programming. The system simulates real-time traffic conditions and suggests optimal routes based on congestion levels.

📌 Overview

This project implements a client–server architecture where multiple clients (vehicles/users) connect to a central server. Each client provides a source and destination, and the server:

Analyzes traffic conditions
Detects congestion using threshold logic
Suggests alternate routes when needed

It demonstrates key concepts of computer networks, multithreading, and real-time systems.

⚙️ Features
✅ Supports multiple clients simultaneously
✅ Uses multithreading for concurrency
✅ Real-time traffic simulation
✅ Dynamic traffic updates
✅ Congestion detection
✅ Alternate route suggestions
✅ Input validation




🧠 How It Works
Client sends:
Source (e.g., NORTH)
Destination (e.g., WEST)
Server:
Checks traffic data
Compares vehicle count with threshold
Decides:
✅ Clear Route
❌ Heavy Traffic + Alternate Route
Server sends response to client
Traffic data updates dynamically



🏗️ Tech Stack
Language: Python
Networking: TCP Socket Programming
Concurrency: Multithreading



How to Run
Install Python (3.x)
Download/clone the project
Open terminal → go to project folder
Run server: python server.py
Open 2–3 new terminals
Run client in each: python client.py
Enter source and destination
View server response
Type n to exit client
Press Ctrl + C to stop server
