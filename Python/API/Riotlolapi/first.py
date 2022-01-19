from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
api_key = 'RGAPI-f02cc4ed-2fd5-4c35-b0cb-c8dedafced7a'
watcher = LolWatcher(api_key)
my_region = 'EUW1'

me = watcher.summoner.by_name(my_region, 'Rud0lf2001')
""" print(me) """

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
""" print(my_ranked_stats) """
print(type(my_ranked_stats))
print (my_ranked_stats[0])