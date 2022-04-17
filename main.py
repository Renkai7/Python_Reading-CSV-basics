import csv
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# # Finding the average
# temp_avg = data["temp"].mean()
# print(temp_avg)
#
# # Find the Max
# temp_max = data["temp"].max()
# print(temp_max)
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# # Get row with day is Monday
# print(data[data.day == "Monday"])
# # Get row with max temperature
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Squirrel project
# Get data - count
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
total_gray = (squirrel_data["Primary Fur Color"] == "Gray").sum()
total_red = (squirrel_data["Primary Fur Color"] == "Cinnamon").sum()
total_black = (squirrel_data["Primary Fur Color"] == "Black").sum()

print(f"{total_gray}, {total_red}, {total_black}")
# Create dataframe: squirrel_count
squirrel_data_dict = {
    "Fur color": ["grey", "red", "black"],
    "Count": [total_gray, total_red, total_black]
}
data = pandas.DataFrame(squirrel_data_dict)
data.to_csv("squirrel_count.csv")
