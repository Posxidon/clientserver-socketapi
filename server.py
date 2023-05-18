import socket
import sys
import os
import argparse
import pathlib

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Simple file server')
parser.add_argument('filename', type=str, help='name of the file to be served')
parser.add_argument('--port', type=int, default=38735, help='port number to listen on (default: 38735)')
args = parser.parse_args()

# Verify the existence of the file to be served
file_path = pathlib.Path("input_file") / args.filename
if not file_path.is_file():
    print(f"Error: File '{args.filename}' not found.")
    sys.exit(1)

# Verify the validity of the port number
if args.port <= 1024 or args.port > 65535:
    print(f"Error: Invalid port number '{args.port}'. Port number must be between 1024 and 65535.")
    sys.exit(1)

# Start the server and listen for incoming connections
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('', args.port))
            s.listen()
            print(f"Server started, listening on port {args.port}")
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            with open(file_path, 'rb') as f:
                file_size = os.path.getsize(file_path)
                if file_size > 80:
                    print("Error: File size exceeds 80 bytes. Connection terminated.")
                    conn.close()
                    continue
                while True:
                    data = f.read(80)
                    if not data:
                        break
                    conn.send(data)
            print(f"File '{args.filename}' sent successfully from '{file_path.resolve()}'")
            conn.close()
        except OSError as e:
            print(f"Error: Failed to start server. {e}")
            sys.exit(1)

    # Prompt user to terminate server or continue listening
    while True:
        print("Server closed. Do you want to continue listening? (y/n): ")
        choice = input().lower()
        if choice == "y":
            break
        elif choice == "n":
            sys.exit(0)
        else:
            print("Error: Invalid choice. Please enter 'y' to continue listening or 'n' to terminate the server.")
