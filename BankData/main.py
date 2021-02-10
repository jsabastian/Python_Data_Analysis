#!/usr/bin/env python
# coding: utf-8

# ### We are going to do a quick analysis on a company's monthly sales sheet
# #### Take a look at the data and we can see it is a simple set of two fields and 86 rows

# In[1]:


#import dependencies
import csv
import os


# In[2]:


#we'll use the os.path.join to create a variable for the paths needed
#input path
input_data = os.path.join("Resources","budget_data.csv")
#take a look
print(input_data)


# In[3]:


#we'll create an output text file to the analysis folder
output_path = os.path.join("Analysis","output_analysis.txt")
print(output_path)


# ### Financial Analysis

# * The total number of months included in the dataset
# 
# * The net total amount of "Profit/Losses" over the entire period
# 
# * The greatest increase in profits (date and amount) over the entire period
# 
# * The greatest decrease in losses (date and amount) over the entire period
# 
# * The average of the changes in "Profit/Losses" over the entire period

# In[4]:


#we can set up our variables for the above

#we'll create a month counter set to zero
total_months = 0

#list of each month populated as we iterate through the rows
month_of_change = []

#we'll keep a running tally of the total revenue over each row
total_net = 0

#empty list for the string month, and integer for the max increase from
#previous month
max_increase = ["",0]

#empty list for the string month, and integer for the max decrease from
#previous month
max_decrease = ["", 9999999999999999999]

#list of calculated changes for average calculation
net_change_list = []

#we will create the avg variable later


# In[5]:


#read the csv into a list of dictionaries using the previous path variable
with open(input_data) as financial_data:
    reader = csv.reader(financial_data)
#     print(type(reader))
    
    #use next function to read the header rows
    header = next(reader)
#     print(header)
    
    #we'll extract the first row of actual data to start the analysis
    first_row = next(reader)
#     print(first_row)

    total_months += 1
#     print(total_months)

    total_net += int(first_row[1])
#     print(total_net)

    prev_net = int(first_row[1])
#     print(prev_net)
    
    for row in reader:
        #change the months_total counter
        total_months += 1
#         print(total_months)
        
        #tally of each months revenue
        total_net += int(row[1])
#         print(total_net)

        
        #track the net change
        net_change = int(row[1]) - prev_net
#         print(net_change)

        #capture the value for comparison to the next row
        prev_net = int(row[1])
#         print(prev_net)

        net_change_list += [net_change]
#         print(net_change_list)

        month_of_change += [row[0]]
#         print(month_of_change)
        
        #calculate the greatest increase
        if net_change > max_increase[1]:
            max_increase[0] = row[0]
            max_increase[1] = net_change
#             print(max_increase)
            
        #calculate the greatest decrease
        if net_change < max_decrease[1]:
            max_decrease[0] = row[0]
            max_decrease[1] = net_change
#             print(max_decrease)


# In[10]:


#here we'll create the avg variable
net_monthly_avg = round(sum(net_change_list) / len(net_change_list),2)
# print(net_monthly_avg)


# In[11]:


#create a display summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg}\n"
    f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
    f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n")


# In[12]:


print(output)


# In[9]:


#export the results to the path created previously
with open(output_path, "w") as txt_file:
    txt_file.write(output)


# In[ ]:




