import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd
import plots.cartesian as c


df = perd.get_merged_df('source/RC_LC_2017-20.csv')

c.draw_cartesian(df, 63, 2020, True)
c.draw_cartesian(df, 68, 2020, True)
c.draw_cartesian(df, 73, 2020, True)
c.draw_cartesian(df, 85, 2020, True)
c.draw_cartesian(df, 999, 2020, True)
