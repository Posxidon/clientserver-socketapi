import socket
import sys
import os
import argparse
import pathlib

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Simple file client')
parser.add_argument('hostname', type=str, help='name of the server host')
parser.add_argument('filename', type=str, help='name of the file to be retrieved')
parser.add_argument('--port', type=int, default=38735, help='port number to connect to (default: 38735)')
args = parser.parse_args()

# Get the path of the file to be retrieved
file_path = pathlib.Path("output_file") / args.filename

# Check if the file already exists
if file_path.is_file():
    while True:
        choice = input(f"File '{args.filename}' already exists. Do you want to overwrite it? (y/n): ").lower()
        if choice == "y":
            break
        elif choice == "n":
            sys.exit(0)
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Connect to the server and retrieve the file
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((args.hostname, args.port))
    except ConnectionRefusedError as e:
        print(f"Error: Failed to connect to server '{args.hostname}:{args.port}'. {e}")
        sys.exit(1)
    print(f"Connected to {args.hostname} on port {args.port}")
    
    try:
        with open(file_path, 'wb') as f:
            while True:
                data = s.recv(80)
                if not data:
                    break
                f.write(data)
    except OSError as e:
        print(f"Error: Failed to write to file '{args.filename}'. {e}")
        sys.exit(1)

print(f"File '{args.filename}' was successfully retrieved from '{args.hostname}' and saved as '{file_path}'")
print("To continue using the server, go to the server CLI and press 'y' to continue, or else you won't be able to connect to the server")

