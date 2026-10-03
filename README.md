# Total War: WARHAMMER III Player Review and Activity Analysis

I became interested in Total War: WARHAMMER III after a major update brought the game back into conversation among several of my friends. I had not played much of the game myself, but I was curious about the amount of player activity, discussion, and feedback surrounding its updates.

That made it an interesting dataset to explore. I wanted to see how player sentiment and activity changed around patches, content releases, and developer announcements, and whether those changes could be measured beyond the overall Steam review score.

This project uses Steam reviews, historical player activity, and developer release data to explore those patterns with Python and Power BI.

![Player Activity with Releases](docs/player_activity_overview.png)

## Project Questions

I focused the analysis around a few questions:

- How does player sentiment differ across common review topics?
- How does sentiment change around developer announcements and updates?
- How does player activity change around patches and content releases?
- What recurring patterns appear in player activity over time?

## Tools

- Power BI
- Python
- DAX

## Data

- Steam player reviews from 2024 through 2026
- Historical player activity data from games-popularity.com
- Developer announcements and release information from SteamDB
- Review topics created from recurring themes in player feedback

## Workflow

- Collected Steam review and player activity data
- Cleaned and transformed the datasets
- Used an LLM-assisted process to identify and organize recurring themes across more than 50,000 review texts
- Connected review topics with relevant developer announcements
- Built measures for sentiment, review volume, and player activity
- Created an interactive Power BI report
- Compared review sentiment and player activity around selected releases

### Player Review

I built the Player Review dashboard to look beyond the overall Steam rating and examine what players were actually discussing.

The dashboard allows me to:

- Filter reviews by topic and date
- Compare review volume with positive recommendation percentage
- View developer announcements alongside review activity
- Compare sentiment before and after selected updates

![Player Sentiment](docs/player_reviews_overview.png)

One example is Hotfix 6.3.2 when filtering for Campaign and AI related reviews.

- Positive recommendations in the previous 7 days: 5.37%
- Positive recommendations in the following 7 days: 52.97%

![Player Sentiment](docs/player_reviews_campaign_ai.png)

### Player Activity

I also wanted to understand whether major updates and announcements were associated with changes in player engagement.

The dashboard includes:

- Daily player activity
- Daily highs and lows
- 7-day averages
- 30-day averages
- Announcement and release filters
- Comparisons between release dates and surrounding activity

![Player Engagement](docs/player_activity_overview.png)

An example focusing on a tighter time span showing a periodic cycle for the week.

![Player Engagement](docs/player_activity_periodic_content.png)

## Key Findings

A few patterns stood out during the analysis:

- Player activity follows a clear weekly cycle, with stronger activity around weekends
- Some content releases coincide with short-term changes from the normal weekly activity pattern
- Higher review volume does not always correspond with more positive sentiment
- Promotional periods can increase the number of reviews while sentiment remains mixed
- Breaking reviews into specific topics provides more useful context than looking only at the overall review score

The project reinforced something I find important in data analysis: a single metric rarely tells the full story. Review volume, sentiment, player activity, and release timing all provide different pieces of the same picture.

## Limitations

There are several limitations I would consider when interpreting the results:

- The analysis is observational and does not prove that releases caused changes in sentiment or player activity
- Promotions, seasonal effects, weekends, and unrelated events may also influence the results
- LLM-assisted topic classification can introduce inconsistent or ambiguous labels
- Steam reviewers may not represent the full player population
- Short analysis windows can overlap with other announcements or releases
