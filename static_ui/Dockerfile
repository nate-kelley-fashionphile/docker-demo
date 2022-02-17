#FROM node:latest as build-stage
#WORKDIR /app
#COPY package*.json ./
#RUN yarn

#RUN yarn build

FROM nginx:latest as production-stage
COPY . ./app/
COPY nginx.conf /etc/nginx/nginx.conf