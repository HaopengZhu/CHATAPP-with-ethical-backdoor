# CHATAPP with Educational Backdoors

## Overview

Hi everyone, here is group 13 with our group members: Haopeng Zhu(a1901635) and Zeyu Liu(a1903617). This is the chat application with some ethical backdoors. This repository contains a Python-based secure chat application designed to demonstrate various security concepts, including the implementation and identification of backdoors within a system. The application uses WebSockets for real-time communication and includes deliberate backdoors for educational purposes.

## Disclaimer

**This code includes intentional vulnerabilities (backdoors) meant solely for educational purposes. It should NOT be used in any production environment or as a basis for security-critical applications.**

## Table of Contents

- Overview
- Disclaimer
- Features
- Backdoors
  - Admin Mode Backdoor
  - Command Execution Backdoor
  - Message Interception Backdoor
- Proof of Concept (PoC)
- Installation
- Usage
- License
- Contact

## Features

- **Real-time messaging** using WebSockets.
- **RSA encryption** for secure message and file transfer.
- **User presence updates**.

## Backdoors

### 1. Admin Mode Backdoor

**Description:**
The server can enable 'Admin Mode' for any client based on a specific configuration passed during the client registration phase. This mode gives elevated privileges to the client.

**Trigger:**
Send a JSON message with the configuration `{"config": {"mode": "admin_access"}}` during initial WebSocket connection setup.

**PoC:**
1. Connect to the server using a WebSocket client.
2. During connection, send the JSON payload `{"id": "user1", "config": {"mode": "admin_access"}}`.
3. The server logs will indicate that admin mode has been enabled.

### 2. Command Execution Backdoor

**Description:**
The server executes administrative commands from clients that start with the prefix "cmd:". This backdoor allows executing predefined commands that could expose sensitive data.

**Trigger:**
Send a message with the prefix "cmd:" followed by the command name.

**PoC:**
1. Connect to the server and authenticate.
2. Send the command `{"info": "cmd:fetch", "from": "admin_user"}`.
3. Server responds with sensitive data from the file `data/admin_data.txt`.

### 3. Message Interception Backdoor

**Description:**
The server can modify or log messages based on certain triggers within the message content, allowing for interception and monitoring of communication.

**Trigger:**
Include the keyword "alert" in any message content.

**PoC:**
1. Send a message with the content `{"info": "Hello everyone! alert", "from": "user1"}`.
2. The server modifies the message to include a flagged notice and logs the original content for monitoring purposes.

## Installation

1. Clone this repository.
2. Install dependencies: `pip install websockets cryptography`.
3. Start the server: `python chat_server.py`.
4. Connect using any WebSocket client.

## Usage

Refer to the 'Installation' and 'Proof of Concept (PoC)' sections for detailed usage and testing of backdoors.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Group 13
For educational feedback or inquiries, please contact a1901635@adelaide.edu.au 

