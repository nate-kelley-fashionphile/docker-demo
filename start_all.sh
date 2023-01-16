

# Update
echo "Pulling changes"
git pull


echo "Starting Laravel"

# Start Laravel
cd laravel9_app && ./vendor/bin/sail up -d && cd ..


echo "Starting Microservices"
docker-compose -f docker-compose-api.yml up -d --build

echo "Starting UIs"
docker-compose -f docker-compose-ui.yml up -d --build


