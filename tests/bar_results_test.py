import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd

import plots.bar_results as br





df = perd.get_df()


# br.bar_results(df, 63, 2020, save=True)

categories=set(df[df['Год']==2020]['в/к'])

for category in categories:
    br.bar_results(df, category, 2020, save=True, test=True)


