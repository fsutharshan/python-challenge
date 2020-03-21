import os
import csv

csvpath = os.path.join("./","budget_data.csv")

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)
     
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
            change_count = 1
            #previous_month_revenue =  float(row[1])
        else:
            change_in_revenue = int(row[1]) - previous_month_revenue
            month.append(row[0])
            change.append(int(change_in_revenue))
            total_change_in_revenue = total_change_in_revenue + change_in_revenue
            
        previous_month_revenue = float(row[1])
        
    print("Number of Months", number_of_months)
    print("Net Total Amount", net_total_amount)
    print("Averange Change:", "{:.2f}".format(total_change_in_revenue /(number_of_months-1)))

    max_increase_value = max(change)
    max_decrease_value = min(change)

    max_increase_month = month[change.index(max_increase_value) + 1]
    max_decrease_month = month[change.index(max_decrease_value) + 1]
    
    print(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})")
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})")


    
