import json

with open("./config.json", "r") as file:
  data = json.load(file)

proxy_format = data["proxy_format"]
proxy_type = data["proxy_type"]
num_threads = data["num_threads"]
