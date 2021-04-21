import data_processing.prepare_merged_data as perd
import plots.median_mean as mm



df = perd.get_df()


mm.draw_median(df, discipline='Сумма дв-рья', year=2017,  save=True, dpi=80)

mm.draw_median(df, discipline='Сумма дв-рья', year=2018,  save=True, dpi=80)

mm.draw_median(df, discipline='Сумма дв-рья', year=2019,  save=True, dpi=80)

mm.draw_median(df, discipline='Сумма дв-рья', year=2020,  save=True, dpi=80)

# mm.draw_median_and_mean(df, discipline='Толчок', year=2020,  save=False, dpi=100)

# mm.draw_median_and_mean(df, discipline='Рывок (сумма)', year=2020,  save=False, dpi=100)

