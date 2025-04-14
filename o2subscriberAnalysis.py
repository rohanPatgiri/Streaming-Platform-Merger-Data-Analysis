import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    lio_subs = pd.read_csv('LioCinema CSV files/subscribers.csv')
    jotstar_subs = pd.read_csv('Jotstar CSV files/subscribers.csv')

    # Add a identifer
    lio_subs['platform'] = "LioCinema"
    jotstar_subs['platform'] = "Jotstar"

    # combine the datasets
    combined_subscribers_df = pd.concat([lio_subs, jotstar_subs], ignore_index=True)
    return combined_subscribers_df

def monthlySubscriberGrowth():
    
    
    combined_subscribers_df = load_data()
    # convert the subscription_date Column to datetime
    combined_subscribers_df['subscription_date'] = pd.to_datetime(combined_subscribers_df['subscription_date'])

    # 2.1 Monthly Subscribers Growth
    plt.figure (figsize = (12,6))

    for platform, df in combined_subscribers_df.groupby('platform'):
        monthly = df.set_index ('subscription_date').resample('M').size()
        #print (monthly)
        plt.plot (monthly.index, monthly.values, label = platform, marker = 'o')

    plt.title ("Monthly Subscriber Growth")
    plt.xlabel('Month')
    plt.ylabel ('New Subscribers')
    plt.legend()
    plt.grid(True)
    #plt.show()
    st.pyplot(plt) # this line is needed to siaply graph on streamlit

def platformWise():
    combined_subscribers_df = load_data()
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    # 2.2
    age_dist = combined_subscribers_df.groupby(['platform', 'age_group']).size().unstack()
    age_dist.plot (kind = "bar", ax=axes[0], rot=0)
    axes[0].set_title('No. of Subscribers by Age Group')

    # 2.3 No of Subscribers by By Age Group for each Platform
    city_dist = combined_subscribers_df.groupby(['platform', 'city_tier']).size().unstack()
    city_dist.plot (kind = "bar", ax=axes[1], rot=0)
    axes[1].set_title('No. of Subscribers by City Tier')

    # 2.4 No of Subscribers by By Subscription Plan for each Platform
    city_dist = combined_subscribers_df.groupby(['platform', 'subscription_plan']).size().unstack()
    city_dist.plot (kind = "bar", ax=axes[2], rot=0)
    axes[2].set_title('No. of Subscribers by Subscription Plan')

    st.pyplot(fig)
