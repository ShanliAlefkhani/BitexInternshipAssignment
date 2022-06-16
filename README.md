# Bitex Internship Assignment

## How to run
```shell
docker-compose up
```

## APIS
To see list of apis you can visit [this url](http://127.0.0.1:8000/docs).

## Client
First run this command:
```shell
cp .env.example .env
```
Then you can use these commands:
```shell
python client.py set "key" "value"
python client.py get "key"
python client.py history "key"
```