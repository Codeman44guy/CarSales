import csv
import matplotlib.pyplot as plt

with open('Data.csv', mode='r') as file:
    data = csv.reader(file)
    next(data)  # Skip the header column
    years = []
    sales = []

    for row in data:
        year = row.pop(0)  # Remove the year from the sales
        years.append(year)  # create a list containing the years

        total_sales = 0  # Initialize the total_sales as 0
        for item in row:
            total_sales += int(item)  # add all the sales by converting them to integers
        sales.append(total_sales)  # create a list containing the total sales per year

        with open('stats.txt', mode='a') as stats:  # Write the year and total using append
            stats.write(f"{year}: {total_sales}\n")  # add newline after each

# Plotting values for each year
x = years
y = sales

plt.figure(1)
plt.bar(x, y)

plt.title("Car sales from 2012 to 2022")  # Writing plot title
plt.xlabel("Years")      # Writing x-axis label
plt.ylabel("Total Sales")  # Writing y-axis label

plt.show()
