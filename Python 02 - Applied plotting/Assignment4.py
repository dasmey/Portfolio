
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **weather phenomena** (see below) for the region of **Nice, Alpes-Maritimes, France**, or **France** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Nice, Alpes-Maritimes, France** to Ann Arbor, USA. In that case at least one source file must be about **Nice, Alpes-Maritimes, France**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Nice, Alpes-Maritimes, France** and **weather phenomena**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **weather phenomena**?  For this category you might want to consider seasonal changes, natural disasters, or historical trends.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[78]:

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from scipy.stats import ttest_ind

def weather_phenomena_france():
    
    Nice = pd.read_csv('weather_nice.csv', sep =';', parse_dates = [0], usecols = [1,7])
    Mars = pd.read_csv('weather_mars.csv', sep = ';', parse_dates = [0], usecols = [1,7])
    Paris = pd.read_csv('weather_paris.csv', sep = ';', parse_dates = [0], usecols = [1,7])
    Lille = pd.read_csv('weather_lille.csv', sep = ';', parse_dates = [0], usecols = [1,7])
    Toulouse = pd.read_csv('weather_toulouse.csv', sep = ';', parse_dates = [0], usecols = [1,7])
    Lyon = pd.read_csv('weather_lyon.csv', sep = ';', parse_dates = [0], usecols = [1,7])
    
    
    Nice['Date'] = Nice['Date'].dt.strftime('%m%d')
    Nice = Nice.groupby('Date').mean()
    Nice['Température'] = Nice['Température'] - 273.15
    
    Mars['Date'] = Mars['Date'].dt.strftime('%m%d')
    Mars = Mars.groupby('Date').mean()
    Mars['Température'] = Mars['Température'] - 273.15
    
    Paris['Date'] = Paris['Date'].dt.strftime('%m%d')
    Paris = Paris.groupby('Date').mean()
    Paris['Température'] = Paris['Température'] - 273.15
    
    Lille['Date'] = Lille['Date'].dt.strftime('%m%d')
    Lille = Lille.groupby('Date').mean()
    Lille['Température'] = Lille['Température'] - 273.15
    
    Toulouse['Date'] = Toulouse['Date'].dt.strftime('%m%d')
    Toulouse = Toulouse.groupby('Date').mean()
    Toulouse['Température'] = Toulouse['Température'] - 273.15
    
    Lyon['Date'] = Lyon['Date'].dt.strftime('%m%d')
    Lyon = Lyon.groupby('Date').mean()
    Lyon['Température'] = Lyon['Température'] - 273.15
    
    
    temp = pd.merge(Nice, Mars, how='inner', left_index = True, right_index = True)
    temp = pd.merge(temp, Paris, how = 'inner', left_index = True, right_index = True)
    temp = temp.rename(columns ={'Température_x':'Nice', 'Température_y':'Marseille', 'Température' : 'Paris'})
    temp = pd.merge(temp, Lille, how = 'inner', left_index = True, right_index = True)
    temp = temp.rename(columns ={'Température' : 'Lille'})
    temp = pd.merge(temp, Toulouse, how = 'inner', left_index = True, right_index = True)
    temp = temp.rename(columns ={'Température' : 'Toulouse'})
    temp = pd.merge(temp, Lyon, how = 'inner', left_index = True, right_index = True)
    temp = temp.rename(columns ={'Température' : 'Lyon'})
    temp = temp[temp.index != '0229']
    # independency test between nice and marseille
    Nice_Marseille = ttest_ind(temp['Nice'],temp['Marseille'])
    # mean for france and south of france
    temp['France'] = (temp['Paris'] + temp['Lille'] + temp['Lyon'] + temp['Toulouse'])/4
    temp['South East France'] = (temp['Marseille']+temp['Nice'])/2
    # independency test between South east of france and rest of France
    Southfrance_vs_France = ttest_ind(temp['France'],temp['South East France'])
    
    columns_to_keep = ['South East France','France']
    temp = temp[columns_to_keep]
    temp = temp.reset_index()
    temp['Date'] = pd.to_datetime(temp['Date'], format = '%m%d')
    
    fig = plt.figure(figsize = (12,8))
    plt.xlabel('Month')
    plt.ylabel('Temperature (Celsius)')
    plt.title('Comparing Average temperatures for the 2010-2018 period between France and South East of France')
    plt.style.use('seaborn-colorblind')
    plt.plot(temp['Date'], temp['France'], color = 'green', lw = 1, label = 'Paris, Lille, Toulouse, Lyon')
    plt.plot(temp['Date'], temp['South East France'], color = 'blue', lw = 1, label = 'Nice, Marseille')
    plt.tick_params(top = 'off', bottom = 'off', left = 'off', right = 'off', labelleft = 'on', labelbottom = 'on')
    
    ax = plt.gca()
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
    ax.xaxis.set_major_locator(dates.MonthLocator())
    
    plt.legend(loc = 'best')
    
    plt.show()
    fig.savefig('assignment4.Png', format = 'png')
    
    return Nice_Marseille[1], Southfrance_vs_France[1]
    
weather_phenomena_france()


# In[ ]:



