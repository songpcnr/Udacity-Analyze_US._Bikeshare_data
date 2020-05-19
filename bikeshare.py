# Import packages as needed
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
       city = input('Which city do you want to see the data? Please type chicago, new york or washington (all in lower case) \n* Note that there is no gender and birth year statistics for washington \n> ').lower()
       if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
       month = input('Which month do you want to filter the data by? Please type only first 6 months of the year (january, february, march, april, may, june: typed in lower case) or "all" to apply no month filter \n> ').lower()
       if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input('Which day do you want to filter the data by? Please type day of the week in lower case or "all" to apply no day filter \n> ').lower()
        if day in days:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    else:
        df = df

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    else:
        df = df

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day:", most_common_day)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour:", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station:", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station:", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}".format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time (in seconds):", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time (in seconds):", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
     
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types are as below:\n")
    user_type_count = df['User Type'].value_counts()
    print(user_type_count)
    
    # TO DO: Display counts of gender
    try:
        print("\n")
        print("Counts of gender statistics are as below:\n")
        gender_type_count = df['Gender'].value_counts()
        print(gender_type_count)
    
    # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
    
    # the most common birth year
        print("\n")
        print("Counts of birth year statistics are as below:\n")
        most_common_birth_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_birth_year)
    
    # the most recent birth year
        most_recent_birth_year = birth_year.max()
        print("The most recent birth year:", most_recent_birth_year)
    
    # the most earliest birth year
        earliest_birth_year = birth_year.min()
        print("The most earliest birth year:", earliest_birth_year)
    except:
        print("There is no gender and birth year statistics for washington.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """Displays raw data as requested from users."""
    see_data = input("\nWould you like to see some examples of raw data used to compute all the statistics? Please type 'yes' or 'no' \n> ").lower()
    row_index = 0
    
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\n Would you like to see more examples of raw data used to compute all the statistics? Please type 'yes' or 'no' \n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
