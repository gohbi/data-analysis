import pandas as pd
myDF = pd.read_csv("/anvil/projects/tdm/data/flights/subset/airports.csv")
myDF.head(5)

#Question2:
#Load the tail of the DataFrame. 
#This solution was what I was able to guess based on previous experience with python
# The tail of a dataframe is the last five data points
myDF = pd.read_csv("/anvil/projects/tdm/data/flights/subset/airports.csv")
myDF.tail()

#Loading the shape of airports.csv based on the sample code that was given
# This was on the project1 information page
# I found this to be straight forward and didn't have to seek extra information

myDF = pd.read_csv("/anvil/projects/tdm/data/flights/subset/airports.csv")
myDF.shape

# Select rows of the data frame that meer certain conditions
# Extract the airports located in New York City:
myDF[(myDF['city'] == 'New York') & (myDF['state'] == 'NY')]

# I copied the solution for the NY airport problem and changed the code as needed
# Display the airports located in Indianapolis, IN
myDF[(myDF['city'] == 'Indianapolis') & (myDF['state'] == 'IN')]

#This was also solved by pasting the previous code and changing the city and state variables as needed
# Display the airports located in Houston, TX
myDF[(myDF['city'] == 'Houston') & (myDF['state'] == 'TX')]



#Question3:
# I just used the code from the previous questions to solve this problem
# I also used the example code given form this problem

# Which state has the largest number of airports? 
# How many airports are located in that state? 
# Below we can see just how many airports there are per state
#We can extract (only) the states from each airport by writing:
myDF['state'].value_counts()

# I just used the code from the previous questions to solve this problem
# I also used the example code given form this problem

# Which state has the largest number of airports? 
# How many airports are located in that state? 
# Below we can see just how many airports there are per state
#We can extract (only) the states from each airport by writing:
myDF['state'].value_counts()

#Following the video instruction I was able to visualize the to five states that have the most airports
# I am ploting the first five states by aiport amount
# I watched the course video to learn how to make the below bar chart
import matplotlib.pyplot as plt
counts = myDF['state'].value_counts().head()
plt.bar(counts.index, counts)

# Here I just really wanted to see the data in a scatter plot because I like scatterplots
# I could only do the first 10 because the plot looked messy with all of the states present
counts2 = myDF['state'].value_counts().head(10)
plt.scatter(counts2.index, counts2)



#Question4:
import pandas as pd
newDF = pd.read_csv("/anvil/projects/tdm/data/icecream/combined/products.csv")
newDF.head(5)

#Here is how many rows is dedicated to each brand 
newDF['brand'].value_counts()

#The next part was to use the same tactics to view the "review.csv"
#I just copied from the previous question and modified the code as needed
#I used the video tutorials as needed
nextDF = pd.read_csv("/anvil/projects/tdm/data/icecream/combined/reviews.csv")
nextDF.head()

#Here is how many occurances of each brand there is in the reviews data source
# I just used what I learned from the previous problems to get the below solutions
nextDF = pd.read_csv("/anvil/projects/tdm/data/icecream/combined/reviews.csv")
nextDF['brand'].value_counts()

# I wanted to see the brands in a bar chart
# I did this because I was curious about what the data would look like 
# Luckily this is a solution to a later question
# I just copied "plt.bar" from the previous plot problem and changed it as needed
count2 = nextDF['brand'].value_counts()
plt.bar(count2.index, count2)







#Question5:
# using matplotlib to display value_counts
# desided to use a scatter plot first (because they are cool)
import matplotlib.pyplot as plt
newcounts = nextDF['brand'].value_counts()
plt.scatter(newcounts.index, newcounts)

# heres a bar chart of the reviews per brand
# I just copied some of my work from previous question and changed the dataframe and variable names
import matplotlib.pyplot as plt
newcounts = nextDF['brand'].value_counts()
plt.bar(newcounts.index, newcounts)

opcounts = newDF['brand'].value_counts()
plt.bar(opcounts.index, opcounts)



















