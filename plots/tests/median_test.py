import matplotlib.pyplot as plt
PACKAGE_PARENT = '../data_processing'
from prepere_merged_file import get_df 
import data_processing.prepare_merged_data as perd
# import plots.median as mm



df = perd.get_df()

years = [2017, 2018, 2019, 2020]
disciplines=['Сумма дв-рья', 'Толчок ДЦ', 'Толчок', 'Рывок (сумма)']


mm.draw_median(df, discipline='Сумма дв-рья', year=years[0],  save=False, dpi=10)
mm.draw_median(df, discipline='Сумма дв-рья', year=years[1],  save=False, dpi=10)
mm.draw_median(df, discipline='Сумма дв-рья', year=years[2],  save=False, dpi=10)
mm.draw_median(df, discipline='Сумма дв-рья', year=years[3],  save=False, dpi=10)

plt.close('all')

# mm.draw_median(df, discipline='Сумма дв-рья', year=2018,  save=True, dpi=80)

# mm.draw_median(df, discipline='Сумма дв-рья', year=2019,  save=True, dpi=80)

# mm.draw_three_medians(df, discipline='Сумма дв-рья', years=[2018,2019,2020],  save=True, dpi=80)

# mm.draw_three_medians(df, discipline='Толчок ДЦ', year=[2018,2019,2020],  save=False, dpi=80)

# mm.draw_median_and_mean(df, discipline='Толчок', year=2020,  save=False, dpi=100)

# mm.draw_median_and_mean(df, discipline='Рывок (сумма)', year=2020,  save=False, dpi=100)