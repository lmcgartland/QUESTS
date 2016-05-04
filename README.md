# QUESTS
Mission

The goal of this project is to explore the quantified self data and derive meaningful insights to help optimize our lives. Techonology has enabled greater quantitative data collection about people than ever before, but this data never gets used by the people who generate it. This project allows users to use their own data and create unique visualizations and put their data to work for them. QUESTS stands for Quantified User Easy Self Tracking System.

Methodology

QUESTS allows users to input data from a variety of sources and consolidate the data into a database organized by date and activitiy. Currently supported sources include Selfstats, Microsoft Health, Last FM, and internet enabled scales. This raw data is processed by a python script into the organized database. The script extracts stats for each day from the raw data and then places them into a JSON object for that day. A collection of JSON files make up the database.

For that database, a web based API was built using Django as a framework. This allows the site to specifically query different date ranges and activities and get that data specifically from the database in a JSON format. The API can even filter by weekday. Django not only powers the backend for the API, but also powers the website pages.

The webpages were built using web libraries such as JQuery and D3. JQuery powers the interactive elements of the pages while D3 is used to generate the visualizations.

Sources

QUESTS uses a variety of sources, and will be adding more. Currently application usage from personal computers is obtained through Selfstats. Sleep, steps, exercise, and calorie data is obtained through Microsoft Health. Weight data is through an internet connected Wii Balance Board with a custom script attached. Song data is through Last FM.
