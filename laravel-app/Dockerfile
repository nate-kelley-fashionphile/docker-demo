# FROM laravelsail/php81-composer:latest as laravel
FROM ubuntu:latest

# WORKDIR /app
RUN apt-get update
RUN apt install docker.io



#Install Dependancies
COPY . .
#RUN composer update
#RUN composer install

#Additional commands can go here



#COPY --from=laravel /app /app
#WORKDIR /app

#RUN docker -h
#RUN apk add bash

#Start Application
#CMD ["./vendor/bin/sail", "up"]
# #CMD ['ls']
#CMD ['docker -h']


