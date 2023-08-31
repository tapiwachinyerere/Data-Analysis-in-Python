import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts(['race'])

    # What is the average age of men?
    average_age_men = round(df.groupby(['sex']).mean(['age'])['age']['Male'],1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df['education'].value_counts()/len(df)*100,1)['Bachelors']

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(round(df[df['salary'] == '>50K'].value_counts(['education']),2)['Bachelors'] +round(df[df['salary'] == '>50K'].value_counts(['education']),2)['Masters'] + round(df[df['salary'] == '>50K'].value_counts(['education']),2)['Doctorate'],1)
    lower_education = len(df[df['salary'] == '>50K']) - round(round(df[df['salary'] == '>50K'].value_counts(['education']),2)['Bachelors'] +round(df[df['salary'] == '>50K'].value_counts(['education']),2)['Masters'] + round(df[df['salary'] == '>50K'].value_counts(['education']),2)['Doctorate'],1)

    # percentage with salary >50K
    higher_education_rich = round((df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')].value_counts(['salary'])['>50K']/len(df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')])*100),1)
    lower_education_rich = 100-higher_education_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == 1])

    rich_percentage = round(df[df['salary'] == '>50K'].value_counts(['hours-per-week'])[1]/len(df[df['hours-per-week'] == 1])*100,1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = round(df[df['salary'] == '>50K'].value_counts(['native-country'])/len(df[df['salary'] == '>50K'])*100,1).idxmax()
    highest_earning_country_percentage = round(df[df['salary'] == '>50K'].value_counts(['native-country'])/len(df[df['salary'] == '>50K'])*100,1)['United-States']

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].value_counts(['occupation']).idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
