FROM node:17-alpine

WORKDIR /reactapp

# install project dependencies
COPY package*.json ./
RUN npm install

# build app for production with minification
COPY ./. ./
RUN npm run build

# Create Server And Serve App
RUN npm install -g http-server
EXPOSE 8080
CMD [ "http-server", "build" ]


# WE CAN ALSO USE NGINX INSTEAD OF http-server
# FROM nginx:stable-alpine as production-stage
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]