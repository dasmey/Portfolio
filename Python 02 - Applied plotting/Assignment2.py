
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d100/a038810ba239d153cf423971ec9b5a4a6ea220e4bcaf0426b615fd8f.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Nice, Alpes-Maritimes, France**, and the stations the data comes from are shown on the map below.

# In[1]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))
    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(100,'a038810ba239d153cf423971ec9b5a4a6ea220e4bcaf0426b615fd8f')


# In[3]:

import matplotlib.pyplot as plt
import pandas as pd
import datetime
import matplotlib.dates as dates

def convert_data_to_plot() :
    
    # get data
    df = pd.read_csv('data/C2A2_data/BinnedCsvs_d100/a038810ba239d153cf423971ec9b5a4a6ea220e4bcaf0426b615fd8f.csv', parse_dates=[1])
    df['Month-day'] = df['Date'].dt.strftime('%m/%d')
    df['Year'] = df['Date'].dt.year
    # Drop 02/29 values
    df2 = df[df['Month-day'] != '02/29']
    df2['Month-day'] = pd.to_datetime(df2['Month-day'], format='%m/%d')
    df2 = df2.sort_values('Date')
    
    # filtering rows, grouping by month-day, mutating data_value and droping unnecessary columns
    df_min = df2[(df2['Element'] == 'TMIN') & (df2['Year'] >= 2005) & (df2['Year'] <= 2014)]
    df_min = df_min.groupby(['Month-day']).min().reset_index()
    df_min['Temperature'] = df_min['Data_Value'] / 10
    df_min = df_min.drop(['Year', 'ID','Date', 'Element', 'Data_Value'], axis = 1)
    
    df_max = df2[(df2['Element'] == 'TMAX') & (df2['Year'] >= 2005) & (df2['Year'] <= 2014)]
    df_max = df_max.groupby(['Month-day']).max().reset_index()
    df_max['Temperature'] = df_max['Data_Value'] / 10
    df_max = df_max.drop(['Year', 'ID','Date', 'Element', 'Data_Value'], axis = 1)
    
    df_min_2015 = df2[(df2['Element'] == 'TMIN') & (df2['Year'] == 2015)]
    df_min_2015 = df_min_2015.groupby(['Month-day']).min().reset_index()
    df_min_2015['Temperature'] = df_min_2015['Data_Value'] / 10
    df_min_2015 = df_min_2015.drop(['Year', 'ID','Date', 'Element', 'Data_Value'], axis = 1)
    df_min_2015 = df_min_2015[df_min_2015['Temperature'] < df_min['Temperature']]
     
    df_max_2015 = df2[(df2['Element'] == 'TMAX') & (df2['Year'] == 2015)]
    df_max_2015 = df_max_2015.groupby(['Month-day']).max().reset_index()
    df_max_2015['Temperature'] = df_max_2015['Data_Value'] / 10
    df_max_2015 = df_max_2015.drop(['Year', 'ID','Date', 'Element', 'Data_Value'], axis = 1)
    df_max_2015 = df_max_2015[df_max_2015['Temperature'] > df_max['Temperature']]
    
    # we'll need to convert our datetime column in order to fill_between spaces later:
    data = df_min['Month-day'].values
    
    #plot, we'll begin with titling and setting up the size
    fig = plt.figure(figsize=(12,8))
    plt.xlabel('Month')
    plt.ylabel('Temperature in Celsius')
    plt.title('Temperature Records for the 2005-2014 period in South East of France')
    # we now insert all data
    plt.plot(df_min['Month-day'], df_min['Temperature'], color = 'blue', lw=0.5, label='Low records')
    plt.plot(df_max['Month-day'], df_max['Temperature'], color = 'red', lw=0.5, label='High records')
    plt.plot(df_min_2015['Month-day'], df_min_2015['Temperature'],'+', color = 'black', label = '')
    plt.plot(df_max_2015['Month-day'], df_max_2015['Temperature'],'+', color = 'black', label = 'Record broken in 2015')
    
    # we add a legend
    plt.legend(loc = 'best')
    
    
    # then remove ticks
    plt.tick_params(top = 'off', bottom = 'off', left = 'on', right = 'off', labelleft = 'on', labelbottom = 'on')

    # and change our axis
    ax = plt.gca()
    ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
    ax.xaxis.set_major_locator(dates.MonthLocator())
    
    # rotate our axis labels
    bx = plt.gca().xaxis
    for item in bx.get_ticklabels():
        item.set_rotation(90)
    
    # remove frame
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    # adding a grid
    plt.grid()
    ax.xaxis.grid(False)
    
    # filling area between max and low temperatures
    ax.fill_between(x = data, y1 = df_min['Temperature'],y2 = df_max['Temperature'],
                          facecolor = 'green',
                          alpha = 0.15)
    # We extend the bottom limit to be able to save the plot to avoid xlabel cropping
    plt.subplots_adjust(bottom=0.15)
    
    # finally we save and display the plot
    fig.savefig('assignment2.png', format='png')
    plt.show()
    
    return df_min.dtypes

convert_data_to_plot()    


# In[ ]:




# In[ ]:



