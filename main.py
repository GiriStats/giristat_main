import data_processing.prepare_merged_data as perd
import plots.median as mm



df = perd.get_merged_df('source/RC_LC_2017-21.csv', 'source/RC_BI_2017-21.csv')


# mm.draw_median(df, discipline='Сумма дв-рья', year=2017,  save=True, dpi=80)

# mm.draw_median(df, discipline='Сумма дв-рья', year=2018,  save=True, dpi=80)

# mm.draw_median(df=df, discipline='Сумма дв-рья', year=2021,  save=True, dpi=80)

# mm.draw_three_medians(df=df, discipline='Сумма дв-рья', years=[2019,2020,2021],  save=True, dpi=80)

# mm.draw_three_medians(df, discipline='Толчок ДЦ', years=[2019,2020,2021],  save=False, dpi=80)

mm.draw_median_and_mean(df, discipline='Толчок', year=2021,  save=False, dpi=100)

# mm.draw_median_and_mean(df, discipline='Рывок (сумма)', year=2020,  save=False, dpi=100)

