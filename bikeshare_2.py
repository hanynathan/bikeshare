import time
import pandas as pd
import numpy as np

CITY_DATA = { '1': 'chicago.csv',
              '2': 'new_york_city.csv',
              '3': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('select city to continu with (\n 1 for chicago\n 2 for new york city\n 3 for washington\n): ').lower()
        if(city not in CITY_DATA):
            print('invalid city name *****\n')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month_name = input('Enter month Name as in [all, january, february, march, april, may, june]: ').lower()
        if(month_name not in months):
            print('Invalid month name *****\n')
        else:
            break
    
    month = months.index(month_name)
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
    while True:
        day = input('whiche day of the month [all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ').title()
        if(day not in days):
            print('\nInvalid day *****')
        else:
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
    data = pd.read_csv(CITY_DATA[city])
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    # data.insert(2, 'month', data['Start Time'].dt.month)
    # data.insert(3, 'day', data['Start Time'].dt.day)
    data['month'] = data['Start Time'].dt.month
    data['day'] = data['Start Time'].dt.day_name()
    # print('month\n', data['month'], 'day\n', data['day'])
    # print(data.head(50))

    if(month == 0 and day == 'All'):
        df = data
    elif(month == 0 and day != 'All'):
        df = data[(data['day'] == day)]
    elif(month != 0 and day == 'All'):
        df = data[(data['month'] == month)]
    else:
        df = data[(data['month'] == month) & (data['day'] == day)]
    
    # print('filterd df\n', df.head(10))
    # print('filterd df2\n', df[4:10])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month: {}'.format(df['month'].mode()))

    # display the most common day of week
    print('the most common day of week: {}'.format(df['day'].mode()))

    # display the most common start hour
    print('the most common start hour: {}'.format(df['Start Time'].dt.hour.mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('most commonly used start station: {}'.format(df['Start Station'].mode()))

    # display most commonly used end station
    print('most commonly used end station: {}'.format(df['End Station'].mode()))

    # display most frequent combination of start station and end station trip
    comm_start_end = df.groupby(['Start Station', 'End Station'])
    print('most frequent combination of start station and end station: {}'.format(comm_start_end.size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time: {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('mean travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_groupby = df['User Type'].groupby(df['User Type'])
    print('counts of user types: {}'.format(user_type_groupby.count()))

    # Display counts of gender
    try:
        gender_count = df['Gender'].groupby(df['Gender'])
        print('counts of gender: {}'.format(gender_count.count()))
    except KeyError as err:
        print('Gender data not available')

    # Display earliest, most recent, and most common year of birth
    try:
        print('earliest year of birth: {}'.format(df['Birth Year'].min()))
        print('most recent year of birth: {}'.format(df['Birth Year'].max()))
        print('most common year of birth: {}'.format(df['Birth Year'].mode()))
    except KeyError as err:
        print('Birth year data not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Display chunks of raw data for user as his request
    arguments:
    df -- DataFrame that contains data the user is interested abuot
    """
    start = 0
    end = 6
    action = input('To View the availbale data in chuncks of 5 rows type: Yes or No\n').lower()
    while action == 'yes':
        print(df[start:end])
        action = input('Do you want to display 5 more rows: Yes or No\n').lower()
        if(action == 'yes'):
            start = end
            end += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # print('head 20\n', df.head(20))

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
