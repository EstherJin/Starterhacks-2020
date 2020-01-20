import pandas as pd
data = pd.read_csv("ks-projects-201801.csv")
just3columns = data.filter(['category', 'state'])
unique_categories_in_array = just3columns.category.unique()

# ms = most_successful
ms_category = ""
ms_successes = 0
ms_attempts = 0
ms_rate = 0
#ls = least_successful
ls_category = ""
ls_successes = 0
ls_attempts = 0
ls_rate = 100
loops=0

'''
for category in unique_categories_in_array: #loops through all categories
    filter_category = just3columns.category.str.contains(f"{category}")
    projects_in_category = len(just3columns[filter_category]) # number of hits in category
    
    filter_success = just3columns[filter_category].state.str.contains('successful')
    successes_in_category = len(just3columns[filter_category][filter_success]) # successes in category
    
    success_rate = successes_in_category / projects_in_category
    if success_rate > ms_rate:
        ms_category = category
        ms_successes = successes_in_category
        ms_attempts = projects_in_category
        ms_rate = success_rate
        
    elif success_rate < ls_rate:
        ls_category = category
        ls_successes = successes_in_category
        ls_attempts = projects_in_category
        ls_rate = success_rate
  
print(f"The most successful category is {ms_category} with {ms_attempts}",
          f"attempts with {ms_successes} successes, with a success rate of {ms_rate}")
print(f"The least successful category is {ls_category} with {ls_attempts}",
          f"attempts with {ls_successes} successes, with a success rate of {ls_rate}")
'''

category_request = input("Which category would you want to see the results of? ")











                         
