# Client-Server File Transfer using Socket API

This project implements a client-server application that allows the transfer of a text file from the server to the client using a connection-based byte stream. The server can handle multiple client connections simultaneously.

## Specification

In this project, you will develop software to transfer a text file using connection-based byte streams from a server to a client. A command-line argument to the server specifies the file name, and the server must deliver this file to each client that contacts it, possibly sending concurrently to several clients. Each client receives the encoded data and interprets it appropriately to recreate an exact copy of the original file, again using a file name specified on the command line. The file may contain any number of lines, and each line is terminated by a single linefeed. The total number of characters, including the linefeed at the end, can be no more than eighty.

## Usage

### Server

To start the server, use the following command:
python server.py <input_file>

- `<input_file>`: Name of the file to be sent to clients.

### Client

To start the client, use the following command:

python client.py <server> <output_file>
  
  - `<server>`: Name of the server.
- `<output_file>`: Name of the file to be saved by the client.

**Note:** Ensure that the `input_file` and `output_file` directories exist before running the server and client, respectively.

## Folder Structure

- `input_file`: Place the file to be served to clients in this folder.
- `output_file`: The client will save the retrieved file in this folder.

## Termination and Continuation

To terminate the server, press `Ctrl+C` in the terminal where the server is running. After the server is closed, you will be prompted to either continue listening or exit.

## Limitations

- The file size should not exceed 80 bytes, including the linefeed character at the end of each line.
- The server and client must be executed on the same network or reachable network addresses.

