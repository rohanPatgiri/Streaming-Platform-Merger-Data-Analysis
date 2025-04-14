import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import o2subscriberAnalysis as o2
import o3inactivityAnalysis as o3
import o4consumptionBehaviour as o4

#st.set_page_config(layout="wide")

# Load your data
LioCinemaContents = pd.read_csv ("LioCinema CSV files/contents.csv")
jotstarContents = pd.read_csv ("Jotstar CSV files/contents.csv")

#Label the platform
jotstarContents['platform'] = "Jotstar"
LioCinemaContents['platform'] = "LioCinema"

st.title ("📊 Streaming Platform Merger Data Analysis")
st.subheader("1. Content Library Analysis")

# Combine both the data frames
combined_contents = pd.concat([LioCinemaContents, jotstarContents], ignore_index = "True")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

#1.1
content_type_counts = combined_contents.groupby(['platform','content_type']).size().unstack()
# Display grouped data
content_type_counts.plot(kind='bar', ax=axes[0], rot=0)
axes[0].set_title('Content Type Distribution')
axes[0].set_xlabel("Platforms")
axes[0].set_ylabel('Count')
#plt.tight_layout()
#st.pyplot(fig)

#1.2
language_type_counts = combined_contents.groupby(['platform','language']).size().unstack()
# Display
language_type_counts.plot(kind='bar', ax=axes[1], rot=0)
axes[1].set_title('Language Type Distribution')
axes[1].set_xlabel("Platforms")
axes[1].set_ylabel('Count')
#plt.tight_layout()
st.pyplot(fig)
#..
fig12, axes12 = plt.subplots(1, 2, figsize=(16, 6))

#1.3 
genre_type_counts = combined_contents.groupby(['platform','genre']).size().unstack()
#Display
genre_type_counts.plot(kind='bar', ax=axes12[0], rot=0)
axes12[0].set_title('Genre Type Distribution')
axes12[0].set_xlabel("Platforms")
axes12[0].set_ylabel('Count')
plt.tight_layout()
#st.pyplot(fig)


#1.4
run_time_counts = combined_contents.groupby(['platform','run_time']).size().unstack()
#Display
run_time_counts.plot(kind='bar', ax=axes12[1], rot=0)
axes12[1].set_title('Run Time Counts')
axes12[1].set_xlabel("Platforms")
axes12[1].set_ylabel('Minutes')
plt.tight_layout()
st.pyplot(fig12)


#................................................................
#2. Subscriber Data Analysis
st.subheader("2. Subscriber Data Analysis")

o2.monthlySubscriberGrowth()
o2.platformWise()


#...............................
#3. 
st.subheader("3. Inactivity Analysis")
o3.inactivityViz()

#..................
# 4. Content Consumption Behavior Analysis
st.subheader("4. Content Consumption Behavior Analysis") 
o4.viz()
