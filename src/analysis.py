from geopy import distance
import pandas as pd


def compute_duration(row: pd.Series) -> float:
    """
    Compute the duration of a trip
    :param row: a row of data containing the start and end times of a trip
    :return: the duration of the trip in minutes of float type
    """
    return (pd.to_datetime(row['ended_at']) - pd.to_datetime(row['started_at'])).seconds / 60


def compute_distance(row: pd.Series) -> float:
    """
    Compute the distance between the start and end points of a trip
    :param row: a row of data containing the start and end points of a trip
    :return: the distance between the start and end points of the trip in kilometers of float type
    """
    return distance.distance((row['start_lat'], row['start_lng']), (row['end_lat'], row['end_lng'])).kilometers


def group_by_member_type(data: pd.DataFrame) -> pd.DataFrame:
    """
    Group the data by member type and compute the average duration and distance for each group
    :param data: the data to group
    :return: a DataFrame containing the average duration and distance for each member type
    """
    return data.groupby('member_casual').agg({'duration': 'mean', 'distance': 'mean'})


def group_by_rideable_type(data: pd.DataFrame) -> pd.DataFrame:
    """
    Group the data by rideable type and compute the number of casual and member for each group
    :param data: the data to group
    :return:
    """
    return data.groupby('rideable_type').agg({'member_casual': 'value_counts'})

print(18/11)