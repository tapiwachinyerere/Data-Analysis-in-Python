import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    ax1 = plt.gca()
    ax1.scatter(y=df['CSIRO Adjusted Sea Level'], x=df['Year'], color='blue')
    
    # Add labels and title
    ax1.set_title('Rise in Sea Level')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Sea Level (inches)')
    plt.show()

    # Create first line of best fit
    ax2 = plt.gca()
    b1, b0, _, _, _ = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    future_year = 2050
    future_sea_level = b1*future_year+b0

    ax2.scatter(y=df['CSIRO Adjusted Sea Level'], x=df['Year'], color='blue')
    ax2.scatter(future_year, future_sea_level, color='red')

    x_fit = np.linspace(min(df['Year']), future_year + 1, 100)

    y_fit = b1 * x_fit + b0

    ax2.plot(x_fit, y_fit, color='purple')
    
    # Add labels and title
    ax2.set_title('Rise in Sea Level')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Sea Level (inches)')
    plt.show()

    # Create second line of best fit
    start_date = 2000

    df_new = df[df['Year'] >= start_date]

    b1_1, b0_1, _, _, _ = linregress(x=df_new['Year'], y=df_new['CSIRO Adjusted Sea Level'])

    ax3 = plt.gca()
    ax3.scatter(y=df_new['CSIRO Adjusted Sea Level'], x=df_new['Year'])

    future_year_1 = 2050
    future_sea_level_1 = b1_1*future_year_1+b0_1

    ax3.scatter(future_year_1, future_sea_level_1, color='blue')

    x_fit_1 = np.linspace(start_date, future_year_1 + 1, 100)

    y_fit_1 = b1_1 * x_fit_1 + b0_1

    ax3.plot(x_fit_1, y_fit_1, color='red')

    # Add labels and title
    ax3.set_title('Rise in Sea Level')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Sea Level (inches)')
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()