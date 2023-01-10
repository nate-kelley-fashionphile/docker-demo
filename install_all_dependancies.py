import subprocess

# Update
process = subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE)
process.wait()
print("Done Pulling Changes" + str(process.returncode))

# node 16
print("Install node 16")
process = subprocess.Popen(
    "cd node_16_api && npm i && cd ..", shell=True, stdout=subprocess.PIPE)
process.wait()

# node 17
print("Install node 17")
process = subprocess.Popen(
    "cd node_17_api_typescript && npm i && cd ..", shell=True, stdout=subprocess.PIPE)
process.wait()

# react
print("Install react")
process = subprocess.Popen(
    "cd react_ui && npm i && cd ..", shell=True, stdout=subprocess.PIPE)
process.wait()

# vue3
print("Install vue3")
process = subprocess.Popen(
    "cd vue3_ui && npm i && cd ..", shell=True, stdout=subprocess.PIPE)
process.wait()
