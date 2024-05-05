docker build -t perfectpick_int .
docker run --network perfectpicknetwork --name perfectpick_int -t -p 7777:7777 perfectpick_int