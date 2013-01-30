China has seen varying levels of PM2.5 toxicity that have occasionally 
reached levels that are extremely harmful to humans. These levels are recorded
by four Chinese officials and reported on an hourly basis through the following
Twitter accounts:

* https://twitter.com/BeijingAir
* https://twitter.com/CGShanghaiAir
* https://twitter.com/CGChengduAir
* https://twitter.com/Guangzhou_Air

# What does china_air_monitor do?

I've constructed a way to parse the json information retreived by Twitter developers
when using a cURL request to extract the PM2.5 toxicty level for each tweet. Rather than
visualizing this information, as other github projects already do, we take the information
and construct a table (csv) that can be used for manipulation in various other environments.

# Example tweet "text"

    01-30-2013 05:00; PM2.5; 52.0; 128; Unhealthy for Sensitive Groups (at 24-hour exposure at this level)

### We are interested in...

    date_time = "01-30-2013 05:00"
    pm_25 = "52.0"
    locale = "Guangzhou"

# Why?

I am particularly interested in exploring the spatial-temporal aspect of this PM2.5 toxicity data.
By examing the four Chinese cities, their hourly reports, and the spread of PM2.5 particulate matter,
we can construct a geovisual analyses to better understand how particulate matter is distributed over
China's developed regions over time (throughout the day and night).

# TODO

* make it easy for others to use china_air_monitor (submit module to pip)
* implement access to Twitter search API within china_air_monitor ecosystem
