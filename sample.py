print("Hello from Docker container!")

docker build -t python-web-app .
docker run -p 5020:5020 python-web-app
