import json

with open("foundationDownload.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data[:2])  # Print the first two items to check the structure