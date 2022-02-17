FROM node:17-alpine as build-stage

WORKDIR /app

# install project dependencies
COPY package*.json ./
RUN npm install

# build app for production with minification
COPY . .
RUN npm run build

# Create Server And Serve App
RUN npm install -g http-server
EXPOSE 8080
CMD [ "http-server", "dist" ]

# FROM nginx as production-stage
# RUN mkdir /app
# COPY --from=build-stage /app/dist /app
# COPY nginx.conf /etc/nginx/nginx.conf