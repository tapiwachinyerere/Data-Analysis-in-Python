import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
def target_func(height, weight):
    if weight/(height/100)**2 > 25:
        return 1
    else:
        return 0
    
df['overweight'] = df.apply(lambda df: target_func(weight=df['weight'], height=df['height']), axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'].mask(df['cholesterol'] == 1, 0, inplace=True)
df['cholesterol'].mask(df['cholesterol'] > 1, 1, inplace=True)

df['gluc'].mask(df['gluc'] == 1, 0, inplace=True)
df['gluc'].mask(df['gluc'] > 1, 1, inplace=True)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count', height=6, aspect=1.2, order=sorted(df_cat['variable'].unique()))
    g.set_axis_labels('variable', 'total')
    g.set_titles('cardio = {col_name}')
    g.set_xticklabels(rotation=0)
    plt.legend(title='value')

    plt.tight_layout()
    plt.show()
    
    # Get the figure for the output
    fig = g

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_pressure = df['ap_lo'] <= df['ap_hi']
    low_h, high_h = df['height'].quantile([0.025, 0.975])
    df_height = df['height'].between(low_h, high_h)
    low_w, high_w = df['weight'].quantile([0.025, 0.975])
    df_weight = df['weight'].between(low_w, high_w)

    df_heat = df[df_pressure & df_height & df_weight]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9, 6))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f', linewidth=.5, mask=mask, ax=ax)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
