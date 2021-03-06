import matplotlib.pyplot as plt
import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd
import plots.median as mm


df = perd.get_merged_df('source/RC_LC_2017-20.csv')

years = [2017, 2018, 2019, 2020]
disciplines = ['Сумма дв-рья', 'JerkLC', 'Jerk', 'Snatch']


def draw_median_test():
    for i in range(4):
        for j in range(len(disciplines)):
            mm.draw_median(df, discipline=disciplines[j], year=years[i], test=False)


def draw_three_medians_test():
    for discipline in disciplines: 
        mm.draw_three_medians(df, discipline=discipline, years=[2018, 2019, 2020],  test=False)


# draw_median_test()
# draw_three_medians_test()



mm.draw_median(df, "Jerk", 2020, test=False)
