# Remote Administration Tool

## Overview

The Remote Administration Tool is a Python-based client-server application designed to facilitate secure and efficient remote management of systems. This tool allows administrators to execute commands, transfer files, and retrieve system information from a remote machine, providing a comprehensive solution for remote system administration.

## Features

- **Command Execution**: Allows administrators to remotely execute commands on the target system.
- **Directory Navigation**: Change the working directory on the client machine.
- **File Download**: Download files from the client to the server.
- **File Upload**: Upload files from the server to the client.
- **System Information Retrieval**: Retrieves detailed system information such as hardware specifications.
- **Process List Retrieval**: Retrieves the list of running processes on the client machine.
- **Connection Termination**: Safely disconnects the client from the server.

## Prerequisites

- Python
- Necessary Python libraries: `socket`, `json`, `os`, `subprocess`, `platform`, `psutil` (for system information)

## Installation

1. Download both the files client and server
2. Place the client file on the client machine and server file on the server machine(admin)
   ** NOTE: This tool only works for windows(client) , serevr can be of any OS and both client and serevr machines should be connected to same network **
3. Now copy the ip address of server(admin) machine and paste the ip address into client and server python files and then save it
4. Now on the client machine open the client.py directory in cmd and type this command : pyinstaller client.py --onefile --noconsole and hit enter
5. This creates some folders and now find the client.exe executable file rest of the other folders and files can be deleted

## Usage

### Server

1. Open the cmd or any other interface and run the server.py file and wait for the client to connect
2. After successful connection you can enter the commands as below shown in example commands

### Client

1. Run the client.exe file by just double clicking it

## Example Commands

- `quit`: Disconnects the client from the server.
- `clear`: Clears the client's terminal screen.
- `cd <directory>`: Changes the directory on the client machine.
- `download <filename>`: Downloads a file from the client to the server.
- `upload <filename>`: Uploads a file from the server to the client.
- `systeminfo`: Retrieves system information from the client machine.
- `processes`: Retrieves the list of running processes on the client machine.

## Terminating the tool
 hit exit on the server cli and the tools terminates
