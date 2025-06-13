import requests

with open("key.key", "r") as f:
    key = f.read()

url = f"http://api.weatherapi.com/v1/current.json"


def feach_weather(city):
    parameters = {
        "key":key,
        "q":city
    }

    try:
        response = requests.get(url, parameters)
        data = response.json()
    except:
        print("Failed to feach data from source please check your wifi connection and city name")

    return data

def main():
    city = input("Enter city which you want to check weater: ")

    weather = feach_weather(city)

    name = weather["location"]["name"]
    country = weather["location"]["country"]
    date_time = weather["location"]["localtime"]
    temperature = weather["current"]["temp_c"]
    current_weather = weather["current"]["condition"]["text"]

    # print(name, country, date_time, temperature, current_weather)
    print(f"\nIn {country} city {name} at {date_time} Temperature is {temperature} and Weather is {current_weather}")
    print(f"\nMain Details:\n\t Current Time: {date_time}\n\t Temperature: {temperature}\n\t Weather: {current_weather}\n")

if __name__ == "__main__":
    main()
