import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('max_rows', 5)
reviews.country   #column name
reviews['country'] 
reviews['country'][0] #Italy
reviews.iloc[0]  #select first row
reviews.iloc[:, 0] #to get a column
reviews.iloc[:3, 0] select the country column from just the first, second, and third row
reviews.iloc[1:3, 0] #to select just the second and third entries
reviews.iloc[[0, 1, 2], 0] #pass a list
reviews.iloc[-5:]  #negative numbers can be used in selection. This will start counting forwards from the end of the value
reviews.loc[0, 'country'] #first entry in reviews
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
reviews.set_index("title") #set_index to the title field
reviews.country == 'Italy' #checking if each wine is Italian
reviews.loc[reviews.country == 'Italy']
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)] #use the ampersand (&) to bring the two questions together
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]  #using "|" means "or"
reviews.loc[reviews.country.isin(['Italy', 'France'])] #isin is lets you select data whose value "is in" a list of values
reviews.loc[reviews.price.notnull()] # highlight values which are (or are not) empty (NaN)
reviews['critic'] = 'everyone' #assigns a constant value
reviews['index_backwards'] = range(len(reviews), 0, -1)   #assigns an iterble of values
