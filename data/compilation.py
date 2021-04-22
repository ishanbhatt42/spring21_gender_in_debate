"""
Main Data Compilation Script

"""

from scraper import tournament_scrape
import pandas as pd

tournament_list = []

# 2020-2021 Season

toc21 = tournament_scrape("TOC", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=16714&result_id=183469", "Z")
tournament_list.append(toc21)

harvard21 = tournament_scrape("Harvard", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=16776&result_id=166103", "Z")
tournament_list.append(harvard21)

berkeley21 = tournament_scrape("Berkeley", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=16917&result_id=166166", "Z2")
tournament_list.append(berkeley21)

hot21 = tournament_scrape("Heart of Texas", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=16679&result_id=170440", "Z -1HL")
tournament_list.append(hot21)

bf21 = tournament_scrape("Emory", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=16030&result_id=160506", "Z")
tournament_list.append(bf21)

hw21 = tournament_scrape("Harvard-Westlake", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=18127&result_id=156949", "Z2")
tournament_list.append(hw21)

gbx21 = tournament_scrape("Glenbrooks", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=14991&result_id=146747", "Z")
tournament_list.append(gbx21)

av21 = tournament_scrape("Apple Valley", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=16856&result_id=141519", "Z2")
tournament_list.append(av21)

mac21 = tournament_scrape("Valley", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=16799&result_id=133667", "Z2")
tournament_list.append(mac21)

ny21 = tournament_scrape("Bronx", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=15710&result_id=137120", "Z")
tournament_list.append(ny21)

gh21 = tournament_scrape("Greenhill", 2021, "https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=16788&result_id=132929", "Z2")
tournament_list.append(gh21)

# 2019-2020 Season

# 2018-2019 Season

# 2017-2018 Season

# Concatenate the data!

main = pd.concat(tournament_list, axis = 0)

print(main)
