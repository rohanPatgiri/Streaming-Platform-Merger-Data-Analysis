# Streaming Platform Merger Data Analysis

## Problem Statement

Lio, a leading telecommunications provider in India, is planning a strategic merger with 
Jotstar, one of the country’s most prominent streaming platforms. This potential partnership aims to combine LioCinema’s expansive subscriber base and Jotstar’s diverse content library to revolutionize digital streaming in India. 

As part of the merger preparation, the management team at Lio wants to analyse the performance and user behavior of both platforms—LioCinema and Jotstar—over the past one year (January to November 2024). The goal is to gain insights into individual platform performance, content consumption patterns, subscriber growth, Inactivity behavior, upgrade and downgrade trends. The insights derived from this study will help the management make  informed decisions and optimize content strategies post-merger, with the ultimate goal of establishing Lio-Jotstar as the leading OTT platform in India. 

**My Objective**
- To analyze the data provided to find valuable insights and present it to the management team, along with actionable recommendations that they can use to achieve their goal of establishing Lio-Jotstar as the leading OTT platform in India.  

## Analysis Process

- The code that I used to analyze the datasets is available in the following GitHub repository: https://github.com/rohanPatgiri/Streaming-Platform-Merger-Data-Analysis/tree/main
- I also made a Video series where I demonstarte my analysis process. It is available in the following YouTube playlist: https://youtube.com/playlist?list=PLHH8hpjyiibG0L_672gVvT3y8UL0xziYp&si=A1fc5W2-mQxymrb_



## Dashboard

- A dashboard, visualizing the important netrics and data points, is available here: 

## Final Report

This report presents a comparative analysis of the content libraries of two prominent streaming platforms: Jotstar and LioCinema. By examining key content attributes such as content type, language diversity, genre distribution, and runtime patterns, the report aims to uncover platform-specific strategies and audience targeting approaches. The insights derived from this analysis can inform content acquisition, production focus, and regional market expansion efforts.

### A. Content Library Analysis

 1. **Content Type Distribution**

- **Jotstar** has a total of **1000+ items**, all of which are **Movies**. No series content is currently hosted.
- **LioCinema** has a slightly smaller library than Jotstar, but with more diversity: it includes a **significant number of Series** along with Movies.
- This suggests **Jotstar is focused solely on film content**, while **LioCinema is expanding into episodic content**, possibly to capture binge-watchers.

---

2. **Language Type Distribution**

- **Jotstar**’s content is dominated by:
    - **English**
    - **Hindi**
    - **Telugu**
    - Also notable are **Kannada**, **Tamil**, and **Punjabi**.
- **LioCinema** shows:
    - **Even stronger presence in Hindi**
    - High numbers in **Tamil** and **Telugu**, suggesting a tilt toward South Indian regional content.
    - Moderate representation across **English**, **Malayalam**, **Punjabi**, and others.
- **Key Insight:** Jotstar’s strength lies in **multilingual diversity**, while LioCinema **focuses heavily on Hindi and South Indian languages**.

---

3. **Genre Distribution**

- **Jotstar:**
    - Top genres include **Drama**, **Action**, **Comedy**, and **Thriller**.
    - **Family** and **Romance** genres also show decent representation.
- **LioCinema:**
    - Heavily focused on **Drama** and **Romance**.
    - Also strong in **Action**, **Thriller**, and **Comedy**.
- **Key Insight:** Both platforms serve popular tastes, but Jotstar leans a bit more into **variety**, while LioCinema has a **strong emotional/dramatic tone** in its catalog.

---

4. **Run Time Analysis**

- **Jotstar:**
    - Most content is concentrated around **120 minutes**, a standard movie duration.
    - Other popular runtimes include **90**, **135**, and **150 minutes**.
- **LioCinema:**
    - Similar trend with **120 minutes** being the most common.
    - Slightly more content in the **30-90 min range**, suggesting a growing **short-form or episodic library**.
- **Key Insight:** Both platforms cater primarily to full-length movie content, with LioCinema possibly experimenting with shorter formats.

---

### B. Subscriber Analysis

1. Subscriber Growth Trends

**Insight**:

- **LioCinema** shows strong **upward subscriber growth**, especially from **July 2024 onwards**, peaking in December 2024.
- **Jotstar** maintains a relatively **stable subscriber base** but shows **stagnation and mild decline** after August 2024.

**Recommendation**:

- Double down on LioCinema’s recent successful strategies—possibly content, pricing, or marketing efforts.
- For Jotstar, **reassess marketing campaigns and retention plans**, especially post-August.

---

2. Age Group Distribution

**Insight**:

- Both platforms dominate among **18–34-year-olds**, especially:
    - **LioCinema** has more **18–24** users.
    - **Jotstar** leads slightly in **25–34**.
- Minimal presence among **45+ users** on both platforms.

**Recommendation**:

- Tailor content and promotions for the **18–34 demographic**, focusing on mobile-first, short-form, and genre-specific content.
- Explore marketing strategies for **older demographics**, like family-oriented content or simplified UX.

---

3. City Tier Insights

**Insight**:

- **Jotstar** has a **strong Tier-1 user base**, while **LioCinema** excels in **Tier-2 and Tier-3 cities**.

**Recommendation**:

- Jotstar: Invest in **premium urban content**, faster servers, and urban influencer tie-ups.
- LioCinema: Continue investing in **regional language content**, **offline-friendly experiences**, and local partnerships to retain Tier-2/3 dominance.

---

4. Subscription Plan Preferences

**Insight**:

- **Jotstar** attracts more **Premium and VIP users**, suggesting better perceived value or brand loyalty.
- **LioCinema** has a high share of **Free plan users**, indicating wider reach but **lower monetization**.

**Recommendation**:

- Jotstar: Capitalize on high-paying user base by offering **exclusive experiences**, early access, and loyalty perks.
- LioCinema: Launch **upsell campaigns** to convert free users, possibly using freemium models or reward-based unlocks.

---

### C. Inactivity Analysis

1. Inactivity by Age Group

**Insight**:

- **LioCinema** has significantly **higher inactivity rates across all age groups**, especially among the **18–24 segment (~19%)**.
- **Jotstar** maintains **low inactivity**, especially among **35–44** and **45+** age groups.

**Concern**:

- LioCinema’s younger users are not engaging post-subscription—likely due to mismatch in content, app experience, or pricing expectations.

**Recommendation**:

- Conduct user research to uncover reasons for drop-off among young users.
- Improve onboarding, notifications, and personalized content delivery.
- Consider gamification or loyalty rewards for continued usage.

---

2. Inactivity by City Tier

**Insight**:

- Inactivity rises sharply from Tier 1 to Tier 3 for **both platforms**.
- LioCinema’s **Tier 3** inactivity hits **~19%**, suggesting **poor retention** in semi-urban/rural markets.

**Recommendation**:

- LioCinema should optimize for low-bandwidth environments, improve regional content targeting, and ensure the app works well on budget smartphones.
- Jotstar can capitalize on its stronger Tier 1 and Tier 2 engagement with hyperlocal influencer campaigns and exclusive urban perks.

---

3. Inactivity by Subscription Plan

**Note**: Labels in the last plot incorrectly show "city_tier" in the legend—this likely represents **subscription plans**.

**Insight**:

- **LioCinema’s inactivity rate spikes with cheaper plans**, reaching nearly **19%** in the likely "Free" or "Basic" tier.
- Jotstar maintains low inactivity across plans, with slightly higher inactivity in mid-tier plans.

**Recommendation**:

- LioCinema must **rethink its free plan**: it's acquiring users who don’t convert or stay.
- Introduce **time-based freemium models** (e.g., 14-day free, then must engage/pay).
- Educate users on value-added features in higher tiers through tutorials or tooltips.

---

### D. Content Consumption Behavior Analysis

1. Watch Time Distribution by Platform

**Insight**:

- **Jotstar significantly outperforms LioCinema** in total watch time, both in median and upper quartile values.
- Jotstar’s upper bound crosses **27,000 minutes**, while LioCinema struggles to cross **10,000**.

**Interpretation**:

- Jotstar users are far more engaged over time, suggesting superior **content stickiness**, **UX**, or **user targeting**.
- LioCinema’s user base is either less active or not watching for long sessions.

**Recommendation**:

- LioCinema should run **A/B testing** on UI/UX flows, assess **content completion rates**, and invest in **high-retention content formats** (e.g., mini-series, regional hits).
- Consider integrating **"Continue Watching"**, binge prompts, and personalized recommendations.

---

2. Watch Time by Age Group

**Insight**:

- Across all age groups, **Jotstar dominates in watch time**.
- Most striking gap: **18–24 and 35–44** users show a major preference for Jotstar.
- Only in the **45+** group does LioCinema show some relative parity, but still trails.

**Interpretation**:

- Jotstar appeals more to young and mid-age viewers—possibly through modern, relatable content.
- LioCinema may not be effectively targeting or retaining younger audiences.

**Recommendation**:

- LioCinema should commission or acquire **Gen Z-friendly content** (short-form, trend-driven).
- Launch targeted campaigns toward **35–44** users, leveraging nostalgia or family-friendly series.
- Bundle content by life stage (e.g., parenting tips, career boosts, etc.).

---

3. Watch Time by City Tier

**Insight**:

- Jotstar’s **Tier 1** and **Tier 2** cities drive high watch times, with **Tier 1** reaching extreme upper bounds (~27,000 mins).
- LioCinema’s watch times remain **clustered and low** across all tiers.
- In **Tier 3**, both platforms underperform—but LioCinema especially suffers.

**Interpretation**:

- Jotstar leverages its **premium urban audience** and probably has stronger bandwidth-optimized, high-quality content.
- LioCinema likely lacks appeal or accessibility in lower-tier cities.

**Recommendation**:

- LioCinema must develop **regional tiered content**, dubbed versions, and low-bandwidth streaming options.
- Partner with regional creators and promote **Tier 2–3 influencer marketing**.
- Experiment with **progressive web apps (PWA)** to reduce download friction.



  
