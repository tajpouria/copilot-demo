# Convert military time to standard time
#
# The time is in the format HHMMSS.
# Convert it to the format HH:MM:SS.
#
# Example:
#
# Input:
# The time is 124523
#
# Output:
# The time is 12:45:23
#


def convert_time(time):
    hour = time[0:2]
    minute = time[2:4]
    second = time[4:6]
    return hour + ":" + minute + ":" + second


def print_random_animal():
    import random

    animals = ["cat", "dog", "bird", "fish", "lizard", "snake", "turtle"]
    print(random.choice(animals))


def yaml_to_array(yaml_file):
    import yaml

    with open(yaml_file) as f:
        data = yaml.load(f)
    return data


def json_to_yaml(json_file):
    import json

    with open(json_file) as f:
        data = json.load(f)
    return data


def do_http_request(url, method, data=None):
    import requests

    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url, data=data)
    elif method == "PUT":
        response = requests.put(url, data=data)
    elif method == "DELETE":
        response = requests.delete(url)
    return response
