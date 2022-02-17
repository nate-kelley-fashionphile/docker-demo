FROM golang:1.16-alpine

WORKDIR /app

# Download necessary Go modules
COPY go.mod ./
COPY go.sum ./
RUN go mod download

#Build the Go application
COPY *.go ./
RUN go build -o /golang_api

#Run the Go application
EXPOSE 8080
CMD [ "/golang_api" ]
