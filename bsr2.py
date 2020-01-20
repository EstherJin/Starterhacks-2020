import pandas as pd
data = pd.read_csv("ks-projects-201801.csv")
just3columns = data.filter(['category', 'state'])
unique_categories_in_array = just3columns.category.unique()
category_rankings = []

loops = 0

for category in unique_categories_in_array:
    
    #loops += 1
    #if loops > 10:
    #    break
        
    filter_category = just3columns.category.str.contains(f"{category}")
    projects_in_category = len(just3columns[filter_category]) # number of hits in category
    
    filter_success = just3columns[filter_category].state.str.contains('successful')
    successes_in_category = len(just3columns[filter_category][filter_success]) # successes in category
    
    success_rate = successes_in_category / projects_in_category
    
    new_category_data = {'category':category, 'successrate': success_rate, 'successes':successes_in_category, 'projects':projects_in_category}
    category_rankings.append(new_category_data)
    
    
#print(category_rankings)
    
#this point of the code works

newlist = sorted(category_rankings, key=lambda k: k['successrate'], reverse=True) 

ranking = 0
for category_data in newlist:
    ranking += 1
    print(f"{ranking}. {category_data['category']} with a success rate of {category_data['successrate']}.",
              f"with {category_data['successes']} from {category_data['projects']} attempts.")