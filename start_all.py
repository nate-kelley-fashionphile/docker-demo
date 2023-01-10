import subprocess

# Update
process = subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE)
process.wait()
print("Done Pulling Changes" + str(process.returncode))

# Start Laravel
print("Starting Laravel")
process = subprocess.Popen(
    "cd laravel9_app && ./vendor/bin/sail up -d && cd ..", shell=True, stdout=subprocess.PIPE)
process.wait()

# Start Microservices
print("Starting Microservices")
process = subprocess.Popen(
    "docker-compose -f docker-compose-api.yml up -d --build", shell=True, stdout=subprocess.PIPE)
process.wait()

# Start UIs
print("Starting UIs")
process = subprocess.Popen(
    "docker-compose -f docker-compose-ui.yml up -d --build", shell=True, stdout=subprocess.PIPE)
process.wait()
