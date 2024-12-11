import pandas as pd
import analysis as an
import viz


def main():
    # Load the data
    data: pd.DataFrame = pd.read_csv("/home/lewiscs/PycharmProjects/google-da-capstone/data/202411-divvy-tripdata.csv")

    # Pre clean the data, removing missing and duplicate values
    data_clean: pd.DataFrame = data.dropna().drop_duplicates()

    # Select the relevant columns
    data_relevant: pd.DataFrame = data_clean[
        ['rideable_type', 'started_at', 'ended_at', 'start_lat', 'start_lng', 'end_lat', 'end_lng',
         'member_casual']]

    # Compute duration and distance
    data_relevant['duration'] = data_relevant.apply(an.compute_duration, axis=1)
    data_relevant['distance'] = data_relevant.apply(an.compute_distance, axis=1)

    membership_type_analysis = an.group_by_member_type(data_relevant)
    rideable_type_analysis = an.group_by_rideable_type(data_relevant)

    membership_type_analysis.to_csv(
        "/home/lewiscs/PycharmProjects/google-da-capstone/data/membership_type_analysis.csv")
    rideable_type_analysis.to_csv("/home/lewiscs/PycharmProjects/google-da-capstone/data/rideable_type_analysis.csv")

    # Print the first few rows of the cleaned data
    print(data_relevant[['duration', 'distance']].head())

    # count the number of members and casuals
    print(data_relevant['member_casual'].value_counts())

    # Plot the data
    viz.plot_data(membership_type_analysis, 'Distance and Duration by Membership Type')


main()
