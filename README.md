# gRPC CRUD Application in Python

## Overview

This is a simple gRPC-based CRUD (Create, Read, Update, Delete) application built in Python. It demonstrates how to implement a gRPC service that performs CRUD operations on in-memory data. The application includes server and client implementations, and provides Docker support for easier deployment.

## Folder Structure
**
grpc-crud-app/
│
├── crud/
│   ├── __init__.py
│   ├── crud_pb2.py          # Generated from .proto file
│   ├── crud_pb2_grpc.py     # Generated from .proto file
│   ├── crud.proto           # Proto file defining service and messages
│
├── server/
│   ├── __init__.py
│   ├── server.py            # gRPC server code
│   └── db.py                # In-memory database or DB logic
│
├── client/
│   ├── __init__.py
│   └── client.py            # gRPC client code
│
├── scripts/
│   ├── generate_proto.sh     # Script to generate Python files from proto
│
├── tests/
│   ├── __init__.py
│   └── test_grpc.py          # Unit tests for gRPC service
│
├── Dockerfile                # Docker configuration for the project
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
**




## Prerequisites

- **Python 3.7+**
- **gRPC tools** (`grpcio`, `grpcio-tools`, and `protobuf`)
- **Docker** (optional, for containerization)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/grpc-crud-app.git
cd grpc-crud-app


pip install -r requirements.txt
./scripts/generate_proto.sh

Terminal 1:
        python server/server.py
Terminal 2:
        python client/client.py
      

            The client will perform the following operations:
            Create an item
            Read the created item
            Update the item
            List all items
            Delete the item

Docker Support
---------------

To run the application in a Docker container, follow these steps:
Build the Docker image:

bash

docker build -t grpc-crud-app .
Run the container:

bash

docker run -p 50051:50051 grpc-crud-app
This will start the gRPC server inside a Docker container, listening on port 50051.



File Details
------------

crud/crud.proto: The protocol buffer definition that defines the gRPC service and message formats.
server/server.py: The gRPC server implementation, which handles CRUD operations.
client/client.py: The client-side implementation for testing CRUD operations.
tests/test_grpc.py: Unit tests for the gRPC server.
Dockerfile: A Docker configuration file to containerize the gRPC server.
requirements.txt: Lists the Python dependencies.


License
This project is licensed under the MIT License.


-----   No  ----------

### Let me know if you'd like to add any more sections or details to the `README.md` file!







proto file creating 
#!/bin/bash

python -m grpc_tools.protoc -I=./crud --python_out=./crud --grpc_python_out=./crud crud/crud.proto
