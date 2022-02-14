import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd
import plots.bar_results as br


df = perd.get_merged_df('source/Semi-final-2017-20.csv')

categories=set(df[df['Year'] == 2020]['WC'])

for category in categories:
      br.bar_results("BI", df, category, 2020, save=False, test=False)
      br.bar_results("BIlk", df, category, 2020, save=False, test=False)
      br.bar_results("LC", df, category, 2020, save=False, test=False)


