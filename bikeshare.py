import calendar
import time
from datetime import datetime as dt
import pandas as pd

CITY_DATA = { 'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'New York': 'new_york_city.csv',
             'Washington': 'washington.csv' }

city_list = ['Chicago', 'New York City', 'New York', 'Washington']

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'All']

day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWould you like to see data for Chicago, New York City or Washington?\n").title()
        if city not in city_list:
            print("\nInvalid input. Please enter a valid city name:\nValid entries: Chicago, New York City or Washington. ")
        else:
            break

    # Get user input for month (all, January, February, ... , June)
    while True:
        month = input("\nWhat month would you like to look for?\n").title()
        if month not in month_list:
            print("Invalid input. Please enter 'all' or a month. Valid entries: all, January, February, March, April, May or June.\n")
        else:
            break

    # Get user input for day of week (all, Monday, Tuesday, ... Sunday)
    while True:
        day = input("\nWhat day of the week would you like to look for?\n").title()
        if day not in day_list:
            print("Invalid input. Please enter 'all' or a day of the week. Valid entries: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n")
        else:
            break

        print('-'*40)

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
 
    return df

    def month_converter(month):
        months = ['January', 'February', 'March', 'April', 'May', 'June']
    
    return months.index(month) + 1    

def time_stats(df):
    """Generates statistics on the most frequent times of travel: most common month, most common day of the week and most common start hour"""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    common_month = calendar.month_name[common_month]
    print('Most popular month: ', common_month)

    # Display the most common day of week
    common_day = df['day_of_week'].mode()[0] 
    print('Most popular day of the week: ', common_day)
    
    # Display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most popular start hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Generates statistics on the most popular stations and trip: most commonly used start and end stations, and most frequent trips."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
   # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most popular start station: ', common_start_station)
    
    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most popular end station: ', common_end_station)
    
    # Display most frequent combination of start station and end station trip
    end_to_end_trips = df['Start Station'] + " - " + df['End Station']
    common_trip = end_to_end_trips.mode()[0]
    print('Most popular trip: ', common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Generates total travel time and mean travel time in days, hours, minutes and seconds for best readability
    
    INPUT: 
    Time duration in seconds
    
    OUTPUT:
    Time duration in days, hours, minutes and seconds. We first calculate the number of seconds in a day, an hour, a minute and a second. Then we perform operations including floor divisions to display our input in the easiest format to understand for the user. Since the mean travel time is potentially a small number, we make sure that we only display useful information.
    """
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    seconds_in_second = 1
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    days = total_travel_time // seconds_in_day
    hours = (total_travel_time - (days * seconds_in_day)) // seconds_in_hour
    minutes = (total_travel_time - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
    seconds = (total_travel_time - (days * seconds_in_day) - (hours * seconds_in_hour)) - (minutes * seconds_in_minute) // seconds_in_second

    print('Total travel time: ', days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds')
    
    # Displaying mean travel time
    """
    Below, we will 
    """
    mean_travel_time = df['Trip Duration'].mean()
    int_mean_travel_time = int(mean_travel_time)
    mean_days = int_mean_travel_time // seconds_in_day
    mean_hours = (int_mean_travel_time - (mean_days * seconds_in_day)) // seconds_in_hour
    mean_minutes = (int_mean_travel_time - (mean_days * seconds_in_day) - (mean_hours * seconds_in_hour)) // seconds_in_minute
    mean_seconds = (int_mean_travel_time - (mean_days * seconds_in_day) - (mean_hours * seconds_in_hour)) - (mean_minutes * seconds_in_minute) // seconds_in_second
    
    if mean_travel_time < 60:
        print('Average travel time: ', mean_seconds, 'seconds')
    elif mean_travel_time < 3600:
        print('Average travel time: ', mean_minutes, 'minutes', mean_seconds, 'seconds')
    elif mean_travel_time < 86400:
        print('Average travel time: ', mean_hours, 'hours', mean_minutes, 'minutes', mean_seconds, 'seconds')
    else:
        print('Average travel time: ', mean_days, 'days', mean_hours, 'hours', mean_minutes, 'minutes', mean_seconds, 'seconds')
 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def user_stats(df):
    """Generates statistics on bikeshare users: counts of user types and genders, as well as earliest, most recent, and most common year of birth when information is available."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    
    # Displaying counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User types:\n', user_type_count, '\n')
    
    # Displaying counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Gender:\n', gender_count, '\n')
    except:
        print('Missing data for gender count\n')
    
    # Displaying earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()
        
        print('Oldest birth year on file:', int(earliest_year_of_birth))
        print('Most recent birth year on file:', int(most_recent_year_of_birth))
        print('Most common birth year among users:', int(most_common_year_of_birth))
    except:
        print('Missing data for year of birth')
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Generates 5 rows of raw data if the user is interested. Prompts a question and generates row data according to the answer of the user."""
    i = 0
    while True:
        show_data = input('\nWould you like to see 5 lines of raw data?\n')
    
        if show_data.lower() == 'yes':
            five_rows = df.iloc[i:i+5]
            print(five_rows)
            i += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
