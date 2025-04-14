# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style for plots
plt.style.use('seaborn')

def load_data():
    # Load data 
    lio_consumption = pd.read_csv('LioCinema CSV files/content_consumption.csv')
    jotstar_consumption = pd.read_csv('Jotstar CSV files/content_consumption.csv')
    lio_subs = pd.read_csv('LioCinema CSV files/subscribers.csv')
    jotstar_subs = pd.read_csv('Jotstar CSV files/subscribers.csv')

    # Add platform identifiers and merge
    lio_consumption['platform'] = 'LioCinema'
    jotstar_consumption['platform'] = 'Jotstar'
    combined_consumption = pd.concat([lio_consumption, jotstar_consumption])


    lio_subs['platform'] = 'LioCinema'
    jotstar_subs['platform'] = 'Jotstar'
    # Merge with subscriber data
    combined_data = pd.merge(
        pd.concat([lio_subs, jotstar_subs]),
        combined_consumption,
        on=['user_id', 'platform'],
        how='left'
    )

    return combined_data

def viz():
    combined_data = load_data()

    # Visualization
    plt.figure(figsize=(10, 5))
    

    # 5.1 Platform comparison
    plt.subplot(1, 3, 1)
    sns.boxplot(data=combined_data, x='platform', y='total_watch_time_mins')
    plt.title('Watch Time Distribution by Platform')
    plt.ylabel('Total Watch Time (mins)')
    plt.xlabel('')

    # 5.2 Age group comparison
    plt.subplot(1, 3, 2)
    sns.boxplot(data=combined_data, x='age_group', y='total_watch_time_mins', hue='platform')
    plt.title('Watch Time by Age Group')
    plt.ylabel('')
    plt.xlabel('Age Group')

    # 5.3 City tier comparison
    plt.subplot(1, 3, 3)
    sns.boxplot(data=combined_data, x='city_tier', y='total_watch_time_mins', hue='platform')
    plt.title('Watch Time by City Tier')
    plt.ylabel('')
    plt.xlabel('City Tier')

    plt.tight_layout()

    st.pyplot (plt)

