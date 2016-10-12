__author__ = 'BrianAguirre'


import twitter #EXAMPLE 1
import json #EXAMPLE 3



"""
/------------------------------------------------------------------/
Example 1.  Authorizing an application to access Twitter account data
/------------------------------------------------------------------/
"""
# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'FhHscKtfWvJABDMCTs9wmkp8r'
CONSUMER_SECRET = '0uw60iFAjbK5DOa6QNApikpMZmdvtgIN8LnzlufvpqUjRrJilW'
OAUTH_TOKEN = '50769348-Jv1xeWVfvEV9FyTk0YZExTaZc8bOKHPAMR6Ni8O2T'
OAUTH_TOKEN_SECRET = 'AxdxZBzecKdmawZ95AJSNKQsufPBkcOzVxTXJ7YsLRNzN'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable


print(twitter_api)

"""
/------------------------------------------------------------------/
Example 2.  Retrieving trends
/------------------------------------------------------------------/
"""

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)


#print(world_trends)
#print
#print(us_trends)


"""
/------------------------------------------------------------------/
Example 3. Displaying API responses as pretty-printed JSON

/------------------------------------------------------------------/
"""

#print(json.dumps(world_trends, indent=1))
print
#print(json.dumps(us_trends, indent=1))



"""
/------------------------------------------------------------------/
Example 4. Computing the intersection of two sets of trends
/------------------------------------------------------------------/
"""

print
print

world_trends_set = set([trend['name']
                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name']
                     for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

#print("COMMON THINGS:")
#print
#print(common_trends)


"""
/------------------------------------------------------------------/
Example 5. Collecting search results
/------------------------------------------------------------------/
"""

# XXX: Set this variable to a trending topic,
# or anything else for that matter. The example query below
# was a trending topic when this content was being developed
# and is used throughout the remainder of this chapter.

q = '#DonaldTrump'

count = 10000

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']


# Iterate through 5 more batches of results by following the cursor

for _ in range(1000):
    print("Length of statuses", len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError as e: # No more results when next_results doesn't exist
        break

# Create a dictionary from next_results, which has the following form:
# ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# Show one sample search result by slicing the list...
print(json.dumps(statuses, indent=2))
