import os
import csv

csvpath = os.path.join("./","budget_data.csv")

# Open the csv file budget_data using handle csvreader
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read and omit the header row
    csv_header = next(csvreader)
    
    # Intitilizes the variables used in the loop
    number_of_months = 0
    net_total_amount = 0
    previous_month_revenue = 0
    change_count = 0
    change_in_revenue = 0
    total_change_in_revenue = 0
    month = []
    change = []

    for row in csvreader:
        number_of_months = number_of_months + 1
        net_total_amount = net_total_amount + int(row[1])

        if change_count == 0:
            change_count = 1 # Only for the first row we do not do any calculation because there is no previous month to compare
        else:
            change_in_revenue = int(row[1]) - previous_month_revenue
            month.append(row[0])  # Add the value to a separate list to use later
            change.append(int(change_in_revenue)) # Add the change to a separate list to use later for min and max
            total_change_in_revenue = total_change_in_revenue + change_in_revenue
            
        previous_month_revenue = float(row[1]) # Set the current row's profit/loss value to be used in the the loop next time.
        
    
    max_increase_value = max(change)
    max_decrease_value = min(change)

    max_increase_month = month[change.index(max_increase_value)]
    max_decrease_month = month[change.index(max_decrease_value)]
    
    # Print the results found so far
    print("Financial Analysis")
    print("----------------------------")
    print("Number of Months", number_of_months)
    print("Net Total Amount", net_total_amount)
    print("Averange Change:", "{:.2f}".format(total_change_in_revenue /(number_of_months-1)))
    print(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})")
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})")


    
