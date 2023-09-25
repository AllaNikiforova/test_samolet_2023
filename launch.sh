#!/bin/bash

docker build -t fastapi-app .

docker run -d -p 8000:8000 fastapi-app

sleep 5

curl http://localhost:8000/
