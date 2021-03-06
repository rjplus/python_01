import Pandas as pd
#DataFrames
pd.DataFrame({'Bob' :'I liked it', 'It was awful'','Sue':['Pretty awful','Bland']},index=['Product A', 'Product B'],name='products')
pd.DataFrame({'Yes' :[50, 21], 'No':[31,2]})
pd.DataFrame({"Bob":[11,23,44],"Matt":[45,11,56]})
pd.DataFrame({
'Bob' :['I liked it', 'It was awful''],
'Sue':['Pretty awful','Bland']},
index=['Product A', 'Product B']
name='Products')
pd.DataFrame({"Bob":[125,56,234],"Ken":[147,14,78]})
fruit_sales = pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]},index=["2017 Sales","2018 Sales"])
animals.to_csv("cows_and_goats.csv")
#series        
pd.Series([1, 2, 3, 4, 5])
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
#Think of a DataFrame as actually being just a bunch of Series "glued together". We'll see more of this in the next section of this tutorial.
items = ["Flour","Milk","Eggs","Spam"]
quantities = ["4 cups", "1 cup","2 large","1 can"]
recipe = pd.Series(quantities, index=items, name="Dinner")

#CSV
#A real dataset looks like when we read it into a DataFrame. We'll use the pd.read_csv() function to read the data into a DataFrame
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

#We can use the shape attribute to check how large the resulting DataFrame is:
wine_reviews.shape  #output:(129971, 14)
#new DataFrame has 130,000 records split across 14 different columns. That's almost 2 million entries!
#examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:
wine_reviews.head()

#The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. 
#For example, you can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically. 
#To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

#next - Kaggle - Pandas Course - Chapter 2 Indexing, Selecting & Assigning

