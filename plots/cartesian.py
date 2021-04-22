import matplotlib.pyplot as plt
import numpy as np
import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd
import plots.median as mm


df = perd.get_df()

df_bi = df[df['Вид']=='Двоеборье']

df_bi_63_2020 = df_bi[(df_bi['в/к']==63) & (df_bi['Год']==2020)]
median_snatch_63_2020 = df_bi_63_2020['Рывок (сумма)'].median()
median_jerk_63_2020 = df_bi_63_2020['Толчок'].median()

max_jerk_63_2020 = df_bi_63_2020['Толчок'].max()
min_jerk_63_2020 = df_bi_63_2020['Толчок'].min()
delta_max_63_2020 =  max_jerk_63_2020 - median_jerk_63_2020
delta_min_63_2020 = median_jerk_63_2020 - min_jerk_63_2020
if delta_max_63_2020 < delta_min_63_2020 :
    xlim_63_2020 = delta_max_63_2020
else:
    xlim_63_2020 = delta_min_63_2020


df_bi_68_2020 = df_bi[(df_bi['в/к']==68) & (df_bi['Год']==2020)]
median_snatch_68_2020 = df_bi_68_2020['Рывок (сумма)'].median()
median_jerk_68_2020 = df_bi_68_2020['Толчок'].median()

max_jerk_68_2020 = df_bi_68_2020['Толчок'].max()
min_jerk_68_2020 = df_bi_68_2020['Толчок'].min()
delta_max_68_2020 =  max_jerk_68_2020 - median_jerk_68_2020
delta_min_68_2020 = median_jerk_68_2020 - min_jerk_68_2020
if delta_max_68_2020 < delta_min_68_2020 :
    xlim_68_2020 = delta_max_68_2020
else:
    xlim_68_2020 = delta_min_68_2020



df_bi_73_2020 = df_bi[(df_bi['в/к']==73) & (df_bi['Год']==2020)]

df_bi_85_2020 = df_bi[(df_bi['в/к']==85) & (df_bi['Год']==2020)]


axis_label_size=13
axis_label_color='g'


fig, axes = plt.subplots(1,2, figsize=(20,5))

text_63 = 'median jerk = ' + str(median_jerk_63_2020) + ' median snatch = ' + str(median_snatch_63_2020)

axes[0].set_title('63 2020', size=19, color='g')
axes[0].scatter(df_bi_63_2020['Толчок'], df_bi_63_2020['Рывок (сумма)'], color='b', label=text_63)
axes[0].spines['left'].set_position('center')
axes[0].spines['right'].set_color('none')
axes[0].spines['bottom'].set_position('center')
axes[0].spines['top'].set_color('none')
axes[0].set_ylim(median_snatch_63_2020-90, median_snatch_63_2020+90)
axes[0].set_xlim(median_jerk_63_2020-90, median_jerk_63_2020+90)
axes[0].xaxis.set_ticks_position('bottom')
axes[0].set_xlabel('толчок', size=axis_label_size, color=axis_label_color)
axes[0].xaxis.set_label_coords(0.95, 0.45)
axes[0].set_ylabel('рывок', size=axis_label_size, color=axis_label_color, rotation=0)
axes[0].yaxis.set_label_coords(0.45, 0.95)

axes[0].legend()


text_68 = 'median jerk = ' + str(median_jerk_68_2020) + ' median snatch = ' + str(median_snatch_68_2020)

axes[1].set_title('68 2020')
axes[1].scatter(df_bi_68_2020['Толчок'], df_bi_68_2020['Рывок (сумма)'], label = text_68)
axes[1].spines['left'].set_position('center')
axes[1].spines['right'].set_color('none')
axes[1].spines['bottom'].set_position('center')
axes[1].spines['top'].set_color('none')
axes[1].set_ylim(median_snatch_68_2020-90, median_snatch_68_2020+90)
axes[1].set_xlim(median_jerk_68_2020-xlim_68_2020, median_jerk_68_2020+xlim_68_2020)
axes[1].xaxis.set_ticks_position('bottom')
axes[1].yaxis.set_ticks_position('left')
axes[1].legend()

# axes[2].set_title('68 2020')
# axes[2].scatter(df_bi_73_2020['Толчок'], df_bi_73_2020['Рывок (сумма)'])
# axes[2].spines['left'].set_position('center')
# axes[2].spines['right'].set_color('none')
# axes[2].spines['bottom'].set_position('center')
# axes[2].spines['top'].set_color('none')
# axes[2].xaxis.set_ticks_position('bottom')
# axes[2].yaxis.set_ticks_position('left')


# axes[3].set_title('68 2020')
# axes[3].scatter(df_bi_85_2020['Толчок'], df_bi_85_2020['Рывок (сумма)'])
# axes[3].spines['left'].set_position('center')
# axes[3].spines['right'].set_color('none')
# axes[3].spines['bottom'].set_position('center')
# axes[3].spines['top'].set_color('none')
# axes[3].xaxis.set_ticks_position('bottom')
# axes[3].yaxis.set_ticks_position('left')





plt.show()