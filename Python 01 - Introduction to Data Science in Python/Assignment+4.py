
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.1** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 4 - Hypothesis Testing
# This assignment requires more individual learning than previous assignments - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.
# 
# Definitions:
# * A _quarter_ is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
# * A _recession_ is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
# * A _recession bottom_ is the quarter within a recession which had the lowest GDP.
# * A _university town_ is a city which has a high percentage of university students compared to the total population of the city.
# 
# **Hypothesis**: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (`price_ratio=quarter_before_recession/recession_bottom`)
# 
# The following data files are available for this assignment:
# * From the [Zillow research data site](http://www.zillow.com/research/data/) there is housing data for the United States. In particular the datafile for [all homes at a city level](http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv), ```City_Zhvi_AllHomes.csv```, has median home sale prices at a fine grained level.
# * From the Wikipedia page on college towns is a list of [university towns in the United States](https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States) which has been copy and pasted into the file ```university_towns.txt```.
# * From Bureau of Economic Analysis, US Department of Commerce, the [GDP over time](http://www.bea.gov/national/index.htm#gdp) of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file ```gdplev.xls```. For this assignment, only look at GDP data from the first quarter of 2000 onward.
# 
# Each function in this assignment below is worth 10%, with the exception of ```run_ttest()```, which is worth 50%.

# In[9]:

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

def get_City_Zhvi_AllHomes():
    
    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
    file = 'City_Zhvi_AllHomes.csv'
    housing = pd.read_csv(file)
    housing.replace({'State':states}, inplace = True)
    housing = housing.sort_values(by = ['State','RegionName'], ascending=[True,True])
    return housing

get_City_Zhvi_AllHomes()


# In[10]:

def get_gdplev():
    
    file2 = 'gdplev.xls'
    xls = pd.ExcelFile(file2)
    GDP = xls.parse(0, skiprows = 220, header = None)
    GDP = GDP.drop(GDP.columns[[0,1,2,3,6,7]], axis = 1)
    GDP.rename(columns = {4:'Quarters',5:'GDP'}, inplace = True)
    return GDP

get_gdplev()


# In[11]:

def get_list_of_university_towns():
    
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    
    fhand = open('university_towns.txt') 
    university = pd.read_table('university_towns.txt', sep="\n",names=["States"])
    university['State'] = university.States.str.extract('(.*)\[edit\]', expand=False).ffill()
    university['RegionName'] = university.States.str.replace(r'\s+\(.+$', '')
    university = university[~university.States.str.contains('\[edit\]')].reset_index(drop=True).drop('States', axis=1)
    return university

get_list_of_university_towns()


# In[12]:

def join_tables():
    
        inner = pd.merge(get_list_of_university_towns(), get_City_Zhvi_AllHomes(), how = "inner", left_on = ['RegionName','State'], right_on = ['RegionName','State'])
        return inner.head()
    
join_tables()


# In[13]:

def get_recession_start():

    GDP = get_gdplev()
    quarter = []
    for i in range(len(GDP) -2):
        if (GDP.iloc[i]['GDP'] > GDP.iloc[i+1]['GDP']) & (GDP.iloc[i+1]['GDP'] > GDP.iloc[i+2]['GDP']):
            quarter.append(GDP.iloc[i]['Quarters'])
    return quarter[0]
    
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''

get_recession_start()


# In[57]:

def get_recession_end():
    
    GDP = get_gdplev()
    quarter = []
    for i in range(len(GDP) -4):
        if (GDP.iloc[i]['GDP'] > GDP.iloc[i+1]['GDP']) & (GDP.iloc[i+1]['GDP'] > GDP.iloc[i+2]['GDP']) & (GDP.iloc[i+2]['GDP'] < GDP.iloc[i+3]['GDP']) & (GDP.iloc[i+3]['GDP'] < GDP.iloc[i+4]['GDP']):
            quarter.append(GDP.iloc[i+4]['Quarters'])
    return quarter[0]

    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
       
get_recession_end()


# In[58]:

def get_recession_bottom():
    
    GDP = get_gdplev()
    quarter = []
    for i in range(len(GDP) -3):
        if (GDP.iloc[i]['GDP'] >= GDP.iloc[i+1]['GDP']):
            quarter.append(GDP.iloc[i+1])
    return quarter[3][0]

    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    
get_recession_bottom()


# In[59]:

#def plot_01():
    #import matplotlib as plt
    #%matplotlib inline
    
    #GDP = get_gdplev()
    #GDP.plot(x = 'Quarters', y = 'GDP', kind = "line")
    
#plot_01()


# In[60]:

from datetime import datetime
from dateutil.parser import parse
import pandas as pd

def convert_housing_data_to_quarters():
    
    housing = get_City_Zhvi_AllHomes()
    GDP = get_gdplev()
    housing = housing.iloc[:, [2,1] + list(range(51, 251))]
    columns_name = []
    columns_values = []
    housing = housing.reset_index().drop('index', axis=1)
    housing = housing.set_index(['State','RegionName'])
    housing.columns = pd.to_datetime(housing.columns)
    housing = housing.resample('Q',axis=1).mean()
    housing = housing.rename(columns=lambda x: str(x.to_period('Q')).lower())
    return housing.head()
    
    
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    
convert_housing_data_to_quarters()


# In[61]:

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
def run_ttest():
    new_data = convert_housing_data_to_quarters().copy()
    university = get_list_of_university_towns()
    university = university.set_index(['State','RegionName'])
    university = university.index.tolist()
    new_data = new_data.loc[:,'2008q2':'2009q2']
    new_data['ratio'] = (new_data['2008q2'] - new_data['2009q2'])/new_data['2008q2']
    group_Utown = new_data.loc[university]
    group_town = new_data.loc[-new_data.index.isin(university)]
    # possible d'ajouter .dropna(how = 'all')
    ttest = ttest_ind(group_Utown['ratio'], group_town['ratio'], nan_policy = 'omit')
        
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    
    return (True, ttest[1], 'university town')

run_ttest()

