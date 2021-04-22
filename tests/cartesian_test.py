import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd
import plots.median as mm
import plots.cartesian as c





df = perd.get_df()

c.draw_cartesian(df, 63, 2020)
c.draw_cartesian(df, 68, 2020)
c.draw_cartesian(df, 73, 2020)
c.draw_cartesian(df, 85, 2020)
c.draw_cartesian(df, 999, 2020)
