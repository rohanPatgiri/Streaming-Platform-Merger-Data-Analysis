import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def load_data():
    lio_subs = pd.read_csv('LioCinema CSV files/subscribers.csv')
    jotstar_subs = pd.read_csv('Jotstar CSV files/subscribers.csv')

    # Add a identifer
    lio_subs['platform'] = "LioCinema"
    jotstar_subs['platform'] = "Jotstar"

    # combine the datasets
    combined_subscribers_df = pd.concat([lio_subs, jotstar_subs], ignore_index=True)
    return combined_subscribers_df
    
def inactivityViz():
    combined_subscribers_df = load_data()
    # Convert dates to datetime
    from datetime import datetime, timedelta
    combined_subscribers_df['last_active_date'] = pd.to_datetime(combined_subscribers_df['last_active_date'])
    current_date = pd.to_datetime('2024-11-30') 
    combined_subscribers_df['is_inactive'] = (current_date - combined_subscribers_df['last_active_date']) > timedelta(days = 90)

    fig, axes = plt.subplots(1,3, figsize=(20,6))
    # 3.2 This Chart shows the inactivity rate for different age groups for each platform.
    age_inactivity = combined_subscribers_df.groupby(['platform', 'age_group'])['is_inactive'].mean(). unstack()*100
    age_inactivity.plot(kind = "bar", ax = axes[0],rot = 0)
    axes[0].set_title('Inactivity Rate by Age Group')
    # 3.3 This Chart shows the inactivity rate for different city tier for each platform.
    city_inactivity = combined_subscribers_df.groupby(['platform', 'city_tier'])['is_inactive'].mean(). unstack()*100
    city_inactivity.plot(kind = "bar", ax = axes[1],rot = 0)
    axes[1].set_title('Inactivity Rate by City Tier')

    # 3.4 This Chart shows the inactivity rate for Subscription Plans for each platform.
    plan_inactivity = combined_subscribers_df.groupby(['platform', 'subscription_plan'])['is_inactive'].mean(). unstack()*100
    city_inactivity.plot(kind = "bar", ax = axes[2],rot = 0)
    axes[2].set_title('Inactivity Rate by Subscription Plan')

    st.pyplot(fig)



    