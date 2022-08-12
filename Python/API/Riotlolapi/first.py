import json
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import json


# golbal variables
api_key = 'RGAPI-0e7b792a-d8a8-4417-979e-f51a334c5815'
watcher = LolWatcher(api_key)
my_region = 'EUW1'

me = watcher.summoner.by_name(my_region, 'Rud0lf2001')
print(me)
print(type(me))
print(me['id'])

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
""" print(my_ranked_stats)
print(type(my_ranked_stats))
print(my_ranked_stats[1])  """

jsontest =json.loads(jsoninput)

