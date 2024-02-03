import pandas as pd
import plotly.express as px

from data_processing.latlon_shifts import random_adjust_deg


if __name__ == '__main__':
  # Define the range of latitude and longitude
  latitude_range = range(-90, 91, 5)  # from -90 to 90 degrees
  longitude_range = range(-180, 179, 5)  # from -180 to 180 degrees

  # Create a list of tuples representing all combinations of latitude and longitude
  grid_points = [(lat, lon) for lat in latitude_range for lon in longitude_range]

  # Create a DataFrame from the list of tuples
  df = pd.DataFrame(grid_points, columns=['Latitude', 'Longitude'])

  df_shifted = df.apply(lambda row: pd.Series(random_adjust_deg(row['Latitude'], row['Longitude'])), axis=1)
  df_shifted.columns = ['Latitude', 'Longitude']

  # Assuming 'df' is your DataFrame with 'Latitude' and 'Longitude' columns
  fig = px.scatter_geo(df, 
                      lat='Latitude', 
                      lon='Longitude',
                      color_discrete_sequence=['red'],
                      title='Grid of Evenly Spaced Data Points',
                      )

  # Add another trace for the second set of points
  fig.add_trace(px.scatter_geo(df_shifted, 
                              lat='Latitude', 
                              lon='Longitude', 
                              color_discrete_sequence=['blue'],  # Color for the second set of points
                              ).data[0])

  # Show the plot
  fig.write_html('img.html')
