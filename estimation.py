import csv
import matplotlib.pyplot as plt

# Read the file
with open('Data.csv', mode='r') as file:
    data = csv.reader(file)
    data_2021 = []
    for row in data:
        if row[0] == "Month":
            last_months = row[-6:]  # Get the last 6-month names
        elif row[0] == "2021":
            data_2021 = row  # Add the data values for 2021 in a list
            sales_2021 = sum([int(x) for x in row[1:7]])  # Calculate the sum of the first 6 months 2021
        elif row[0] == "2022":
            sales_2022 = sum([int(x) for x in row[1:7]])  # Calculate the sum of the first 6 months 2022

    sales_growth_rate = (sales_2022 - sales_2021) / sales_2022

    estimated_values = []  # Initialize a list for the estimated values

    i = 0  # Counter for months
    # Loop through values in the 2021 list for the last 6 months
    for month_value_2021 in [int(x) for x in data_2021[-6:]]:
        month_value_2022 = month_value_2021 + month_value_2021 * sales_growth_rate  # Get the 2022 estimated values
        estimated_values.append(month_value_2022)

        with open('stats.txt', mode='a') as stats:
            stats.write(f"{last_months[i]}: {month_value_2022}\n")  # Append the values in the existing stats file
        i += 1

# Horizontal Bar Plot
x = last_months  # x values to be months
y = estimated_values  # y values to be the estimated values

plt.figure(1)
plt.barh(x, y)

plt.title("Estimated sales for 2022")
plt.xlabel("Month")
plt.ylabel("Estimated sales")
plt.grid()                  # Showing grids on the plot

plt.show()
