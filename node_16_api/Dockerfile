#CHOOSE WHICH ENVIRONMENT TO USE
FROM node:16-alpine

WORKDIR /node16app

#COPY INSTALLATION FILES
COPY package*.json ./

#INSTALL DEPENDENCIES
RUN npm install

#COPY CODE FILES
COPY . .

#WHICH PORT WILL BE USED
EXPOSE 3000

#START THE APPLICATION
CMD ["node", "index.js"]
