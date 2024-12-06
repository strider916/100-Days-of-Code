# with open("weather_data.csv", mode="r") as data:
#      my_list = data.readlines()
# print(my_list)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# print(data["temp"].mean())
# print(data["temp"].max())

# # Get data in columns
# print(data["condition"])

# Get data in row
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32)


# Create dataframe from scratch
# data_dict = {
#     "students": ["Angela", "Nick", "James"],
#     "scores": [30, 25, 28]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)

import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241203.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")

