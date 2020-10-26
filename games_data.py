#!/usr/bin/env python
# coding: utf-8

# In[404]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[405]:


# Upload data games
df=pd.read_csv('vgsales.csv')


# ## Assessing data

# In[406]:


df.head(20)


# In[407]:


#check for any null values in each column
list_col=list(df.columns)
for col in list_col:
    n=df[col].isnull().sum()
    print(str(col)+':'+str(n))


# In[408]:


df.shape


# In[409]:


df.dtypes


# In[410]:


df.duplicated().sum()


# In[411]:


name_df=df.Name.duplicated().sum()
name_df


# In[412]:


# total unique games
df.shape[0]-name_df


# ## Cleaning time

# In[413]:


# make sure that global sales is sum of those columns
condition=(df.Global_Sales==df.NA_Sales +df.EU_Sales +df.JP_Sales)
if condition.any():
    df.Global_Sales=df.NA_Sales +df.EU_Sales +df.JP_Sales 


# In[414]:


# test the code
condition=(df.Global_Sales==df.NA_Sales +df.EU_Sales +df.JP_Sales)
condition


# In[415]:


# to convert year column to int type , first i have to deal with all nan values which contain that column.
# will replace NAN values with 0
df.Year=df.Year.fillna(0)


# In[416]:


# convert year column type from float to int.
df.Year=pd.to_numeric(df.Year)
df.Year=df.Year.astype(int)


# In[417]:


#to test the code
df.dtypes


# ## Analysis time
# * __Questions__
# * Total sales for each platform [the top three , and the lowest one]
# * Line chart for the top platform to show the distribution of years for sales
# * for each platform the most popular genre and it's total sales
# * the top genre in total sales
# * _IN GENERAL_ top and lowest year in sales
# * the most popular game
# * the order of games 
# * for each year the most popular game

# In[418]:


df.head(2)


# ##  Total sales for each platform [the top three , and the lowest one]
# 

# In[419]:


# Total sales for each platform [the top three , and the lowest one]
df_total=df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)
df_total


# ### Top three are [PS2, X360 ,Wii]
# ### Lowest one is [PCFX]

# ## ____________________________________________________________________
# ## second:
# ## scatter chart for the top platform to show the distribution of years for sales
# 

# In[420]:


df_ps2=df[df['Platform']== 'PS2']
ps2=df_ps2.groupby('Year')['Global_Sales'].sum()
ps2


# In[421]:


ps2=pd.DataFrame(ps2.reset_index())
ps2


# In[422]:


ps2.plot(x ='Year', y='Global_Sales', kind = 'scatter')
#plt.xticks(ps2.Year)
#plt.yticks(ps2.Global_Sales)
plt.grid(True)
plt.title("Distribution of the total sales for years for PS2")


# ## 3- for each paltform the most popular genre and the total sales for it

# In[423]:


# for each paltform the most popular genre and the total sales for it
platform_genre=df.groupby(['Platform','Genre'])['Global_Sales'].sum()
platform_genre=pd.DataFrame(platform_genre.reset_index())
platform_genre


# In[424]:


# From this query we see the most popular genre for each platform according to the total sales from it .
highest_in=platform_genre.groupby('Platform')['Genre','Global_Sales'].max()
highest_in=pd.DataFrame(highest_in.reset_index())
highest_in


# ##  4-The top genre in total global sales 

# In[425]:


# The top genre in total global sales 
general_top_genre=df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
general_top_genre


# In[426]:


# top Genre [action, sports, shooter]
# the lowest [strategy]
general_top_genre.plot()


# ## 5-top year and lowest one in sales

# In[427]:


# top year and lowest one
# top year in sales [2008]
# the lowest two years in sales [2020 , 2017]
df.groupby('Year')['Global_Sales'].sum().sort_values(ascending=False)


# ## 6-the most popular game
# ## 7-the order of games

# In[428]:


#the most popular game
#the order of games
df.head(2)


# In[429]:


popular_games=df.groupby('Name')['Global_Sales'].sum()
popular_games=pd.DataFrame(popular_games.reset_index())
popular_games=df.groupby('Name')['Global_Sales'].max().sort_values(ascending=False)
popular_games=pd.DataFrame(popular_games.reset_index())
popular_games.head(5)


# ## 8-for each year the most popular game

# In[430]:


# for each year the most popular game
year_data=df[df['Year']!=0]
game_for_year=year_data.groupby('Year')['Name','Global_Sales'].max()

game_for_year=pd.DataFrame(game_for_year.reset_index())
game_for_year


# # The End
