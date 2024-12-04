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
data.rename(columns={"Primary Fur Color": "fur_color"}, inplace=True)

print(data.fur_color == "Gray")
