echo "Stopping Laravel"

# Start Laravel
cd laravel9_app && ./vendor/bin/sail down && cd ..

echo "Starting Microservices"
docker-compose -f docker-compose-api.yml down -d

echo "Starting UIs"
docker-compose -f docker-compose-ui.yml down -d