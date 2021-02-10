#!/usr/bin/env python
# coding: utf-8

# ### We'll use python to perform an analysis on election data.
# 
# #### The data is three fields: Voter ID; County; Candidate. And really big.

# In[1]:


#import dependencies
import csv
import os


# In[2]:


#establish the path for importing the csv data
import_data = os.path.join('Resources','election_data.csv')
print(import_data)


# In[3]:


#establish the output path for the analysis
output_data = os.path.join("Analysis","election_analysis.txt")
print(output_data)


# ### Election data parameters

#   * The total number of votes cast
# 
#   * A complete list of candidates who received votes
# 
#   * The percentage of votes each candidate won
# 
#   * The total number of votes each candidate won
# 
#   * The winner of the election based on popular vote.
# 

# In[4]:


# create variables for each of the above

#counter begins at zero and will be added to after every row iteration
vote_total = 0


# In[5]:


#empty list to populate with every unique candidate encountered
cand_list = []

#an empty dictionary will allow us to add candidates and the # of votes received
cand_total = {}


# In[6]:


#winning cadidate based on popular vote
cand_pop = ""

#winning candidate popular vote total
cand_pop_total = 0


# #### read the csv and iterate through

# In[7]:


with open(import_data) as election_data:
    reader = csv.reader(election_data)
    
    #read the header first
    header = next(reader)
    
    #iterate through the rows
    for row in reader:
        
        #each row is a vote
        vote_total +=1
        
        #id the candidate receiving vote
        cand_name = row[2]
        
        #check if the candidate is already in the list
        if cand_name not in cand_list:
            
            #if not, add it
            cand_list.append(cand_name)
            
            #and track their vote count by est. initial counter
            cand_total[cand_name] = 0
            
        #add a vote to their total
        cand_total[cand_name] +=1


# In[23]:


#we can print the results to the txt file for export
with open(output_data,"w") as txt_file:
    
    #first print to terminal
    election_results = (
        f'\n\nElection Results\n'
        f'————————————————————————\n'
        f'Total Votes: {vote_total}\n'
        f'————————————————————————\n')
    print(election_results, end = "")
    
    
    #then to txt file
    txt_file.write(election_results)
    
    #iterate through the cand_total list
    for candidate in cand_total:
        
        #calculate the number of votes per and pct
        votes = cand_total.get(candidate)
        cand_pct = round(float(votes) / float(vote_total) *100,1)
        
        
        #loop to identify the winner and vote count
        if (votes > cand_pop_total):
            
            cand_pop_total = votes
            cand_pop = candidate
            
        #print candidate vote total and pct to terminal
        voter_output = f'{candidate}: {cand_pct:.3f}% ({votes})\n'
        print(voter_output)
        
        #save each to txt file
        txt_file.write(voter_output)
        
    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {cand_pop}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
        


# In[ ]:




