import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        city=input("Enter name of the city to analyze:")
        if city.lower() in CITY_DATA:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    months=["all", "january", "february","march","april","may","june"
            ,"july","august","september","october","november","december"]
    while True:
        month=input("name of the month to filter by, or 'all' to apply no month filter:")
        if month.lower() in months :
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dat_of_week=["all", "monday","tuesday","wednesday"	,
                 "thursday","friday","saturday","sunday"]
    while True:
        day=input("Enter name of day of week (all, monday, tuesday, ... sunday):")
        if day.lower() in dat_of_week:
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
    df=pd.read_csv(CITY_DATA[city.lower()])
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["month"]=df["Start Time"].dt.month_name()
    df["day"]=df["Start Time"].dt.day_name()
    if month.lower()!="all":
           df= df[df["month"]==month.title()]
    if day.lower()!="all":
            df=df[df["day"]==day.title()]
    show_Data=input("if you want to see first 5 rows of Data write yes: ")
    if show_Data.lower()=="yes":
        print(df.head(5))


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month: ",df["month"].mode()[0])


    # TO DO: display the most common day of week
    print("the most common day of week: ",df["day"].mode()[0])


    # TO DO: display the most common start hour
    print("the most common start hour: ",df["Start Time"].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station: ",df["Start Station"].mode()[0])


    # TO DO: display most commonly used end station
    print("most commonly used end station: ",df["End Station"].mode()[0])



    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "," + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split(",")))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time: ",df["Trip Duration"].sum())

    # TO DO: display mean travel time
    print("mean travel time: ",df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types:\n ",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print("counts of Gender:\n ",df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("earliest year: {}, most recent: {} and most common year of birth: {} "
          .format(df["Birth Year"].min(),df["Birth Year"].max(),df["Birth Year"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
