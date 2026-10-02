# Total War: WARHAMMER III — Review Analysis with Power BI

Analysis of Steam review sentiment, review topics and player response
to game updates using Python and Microsoft Power BI.

- Steam API data collection
- Review topic classification
- Power Query data transformation
- DAX measures for analytics and visuals
- Release analysis for player Sentiment and Engagement

![Player Activity with Releases](docs/player_activity_overview.png)

## ANALYSIS

This project examines Steam player reviews from 2024-2026. It compares player sentiment and engagement around developer announcements for releases.

The project focuses on two findings:

- Reviews with topic prevalence and player positive recommendation
- Player activity before and after game updates by type

Steam provided public data accessible through an API used by steam_review_api.py, for historical data of the 2024-2026 daily activity was provided from games-popularity.com with player_count_api.py and steamdb.com provided developer announcement information.

For Topic Classification, ChatGPT Plus ingested a CSV file containing 50k+ text reviews and Developer Announcements to organize into common topics.

Power BI powered Data Transforms, Modeling, Measures, and Visualization.

## DASHBOARD

### Review Topic Analysis

This dashboard contains a slicer to sort by topic, 4 cards presenting larger data points about selected topic, the main line graph showing announcement markets in relation to reviews, and a table for a list of announcements related to the topic for more details.

![Engagement vs. Satisfaction](docs/player_reviews_overview.png)

The dashboard itself allows adjustment to the X-axis timeline, and presents details when hovering over a data point.

![Engagement vs. Satisfaction](docs/player_reviews_tooltip.png)

### Engagement vs. Satisfaction

The four quadrant scatterplot starts by identifying announcements that can be filtered by type. It shows player interactions within a time period of the announcement either as a positive or negative for Player Engagement and Satisfaction.  Player's Engagement measures activity with the game, and player's Satisfaction uses player review metrics.

![Engagement vs. Satisfaction](docs/player_activity_overview.png)

Examining a data point in detail shows a tooltip that highlights the values for Engagement/Satisfaction, while also expanding upon metrics 7 days before/after the specific announcement as a table.

![Engagement vs. Satisfaction](docs/player_activity_tooltips.png)

## KEY FINDINGS

- A strong correlation of announcements with free + paid content, and increased player negative reviews, while also accounting for higher player activity
- Announcements for Patches moved the least amount of Engagement, while only marginally affecting player's review recommendation
- Some developer releases, such as those involving Balance, closely follows player negativity either as a peak (likely resolving negativity), or a valley (likely a causal factor to negativity)
