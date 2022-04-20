import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
   

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    years_extended = np.arange(1880, 2051)
    linear_reg = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    y2 = [linear_reg.intercept + linear_reg.slope*xi for xi in years_extended]
    plt.plot(years_extended,y2, color = 'red')
    # Create second line of best fit
    
    years_recent = np.arange(2000, 2051)
    df_recent = df[df['Year']>= 2000]
    
    linear_reg_rec = linregress(x=df_recent['Year'], y = df_recent['CSIRO Adjusted Sea Level'])
    y3 = [linear_reg_rec.intercept + linear_reg_rec.slope * xr for xr in years_recent]
    plt.plot(years_recent, y3, color = 'blue')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()