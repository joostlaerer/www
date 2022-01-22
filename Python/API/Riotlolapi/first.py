from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
api_key = 'RGAPI-22f9a7a6-7147-4961-8b17-13a0cd35b232'
watcher = LolWatcher(api_key)
my_region = 'EUW1'

me = watcher.summoner.by_name(my_region, 'Rud0lf2001')
""" print(me) """

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)
print(type(my_ranked_stats))
print (my_ranked_stats[0])