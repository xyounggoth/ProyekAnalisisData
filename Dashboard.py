import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

#Dashboard title
st.title('Bike Sharing Dashboard')

#Load data
st.header("Data Frame Bike Rented by Day")
day_df = pd.read_csv('https://raw.githubusercontent.com/xyounggoth/ProyekAnalisisData/refs/heads/main/day.csv')
st.dataframe(day_df)

st.header("Data Frame Bike Rented by Hour")
hour_df = pd.read_csv("https://raw.githubusercontent.com/xyounggoth/ProyekAnalisisData/refs/heads/main/hour.csv")
st.dataframe(hour_df)

#Counting the total days and hours
st.subheader("Total Days and Hours")

# Display the text
st.markdown("Total Days:")
st.markdown("731")
st.markdown("Total Hours:")
st.markdown("17379")

# Question 1
st.header("Question 1: Which particular hour of the day sees the biggest utilization of bike rentals?")

# Answer question 1
hour_grouped = hour_df.groupby(by="hr").cnt.nunique()

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
ax.plot(hour_grouped.index, hour_grouped.values, marker='o', linestyle='-', color='b')

# Set the plot title and labels
ax.set_title('Total Bike Rentals per Hour', fontsize=16)
ax.set_xlabel('Hour', fontsize=12)
ax.set_ylabel('Total', fontsize=12)

# Set x-axis ticks
ax.set_xticks(range(24))

# Add a grid
ax.grid(True)

# Display the figure in Streamlit
st.pyplot(fig)

#Figure explanation
st.subheader("Figure Explanation")

# Insight 1: Peak Time
st.write("#### **Peak Time**")
st.write("""
The first significant peak happens at eight in the morning, probably in time for the morning commute.
Around 6:00 PM, during the evening rush, there is another peak.
""")

# Insight 2: Periods of Low Activity
st.markdown("#### **Periods of Low Activity**")
st.write("""
The lowest activity is between 4 and 6 AM, which makes sense given that it's early in the morning 
and most people aren't riding bikes. Bicycle rentals sharply decrease after 8 PM, 
suggesting a decrease in demand during the evening.
""")

# Insight 3: Midday Uniformity
st.markdown("#### **Midday Uniformity**")
st.write("""
Bicycle rentals remain consistent between 12 and 3 PM, indicating a moderate amount of use during lunch 
or other midday activities.
""")

# Insight 4: General Trend
st.markdown("#### **General Trend**")
st.write("""
With lower counts in the early morning, a surge throughout commute hours, and another fall 
as the day draws to a close, the rents exhibit a U-shaped pattern.
""")



# Question 2
st.header("Question 2: What impact does the weather situation have on bike rentals?")

# Answer question 2
weather_mapping = {
    1: "Clear, Few clouds, Partly cloudy, Partly cloudy",
    2: "Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist",
    3: "Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds",
    4: "Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"
}

day_df['weathersit'] = day_df['weathersit'].map(weather_mapping)

#Showing the figure
weather_counts = day_df.groupby(by="weathersit").cnt.nunique().sort_values(ascending=False)

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the pie chart
ax.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=90,
       colors=['skyblue', 'lightgray', 'lightsteelblue', 'slategray'], wedgeprops=dict(width=0.4))

# Set the title and labels
ax.set_title('Number of Bike Rentals by Weather Situation')
ax.axis('equal')  # Equal aspect ratio ensures a circular pie chart
ax.set_ylabel('')  # Remove default y-axis label

# Display the figure in Streamlit
st.pyplot(fig)


#Figure explanation
st.subheader("Figure Explanation")

# Insight
st.markdown("#### **Weather That Is Mostly Clear or Partly Cloudy:**")
st.write(
    """Favorable weather, such as 'Clear, Few clouds, Partly cloudy, Partly cloudy,' 
    was experienced for 63.1% of bike rentals. This indicates that most bike riders would rather rent when the weather is nice."""
)

st.markdown("#### **Weather Conditions with Mist and Clouds:**")
st.write(
    """Thirty-four percent of rentals took place in 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist.' 
    This suggests that, despite being less favorable, overcast or misty weather does not greatly discourage people from renting bikes."""
)

st.markdown("#### **Unfavorable Weather:**")
st.write(
    """Bicycle rentals happened in just 2.9% of cases when the weather was like 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds.' 
    It is evident that bad weather significantly lowers the amount of bike rentals."""
)

st.markdown("#### **In Case of Severe Weather, No Rentals:**")
st.write(
    """Notably, no rentals were available during periods of intense rain, ice pellets, thunderstorms, mist, snow, and fog. 
    Since this weather category has a value of 0, the figure does not show it. 
    Bicycle rentals are particularly vulnerable to inclement weather, as evidenced by the lack of rentals during these extreme conditions, which riders absolutely shun."""
)

st.header("Conclusion")
st.write("""The time of day and the weather have a big impact on bike rentals. Early morning and late evening are the least active times,
          whereas commuting hours (8 AM and 6 PM) see the most utilization. Good weather, such as partly overcast or bright skies, 
          is necessary for large bike rental numbers. Cloudy or misty weather does, however, nonetheless permit a sizable percentage of rentals. 
         However, bad weather results in a substantial drop in bike rentals, and extremely bad weather results in no activity at all. 
         This suggests that although renting bikes is a common way to get around in nice weather, bad weather greatly discourages people from using them.
""")