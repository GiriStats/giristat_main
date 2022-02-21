import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd
import plots.bar_results as br


df = perd.get_merged_df('source/RC_LC_2017-21.csv', 'source/RC_BI_2017-21.csv')

year = 2021

categories=set(df[df['Year'] == year]['WC'])

# br.bar_results("BI", df, 63, year, save=False, test=False)

for category in categories:
    br.bar_results("BI", df, category, year, save=True, test=False)
#     br.bar_results("BIlk", df, category, 2020, save=False, test=False)
#     br.bar_results("LC", df, category, 2020, save=False, test=False)


# br.bar_result_weightLC(df, 63, 2020, save=False, test=False)



# df = perd.get_df('source/All-RC-2017-20.csv')
# categories=set(df[df['Year'] == 2020]['WC'])

# for category in categories:
    # br.bar_results("LC", df, category, 2020, save=False, test=False)

# df = perd.get_df('./../source/All-RC-2017-20.csv')

# perd.get_dataentries(df)
