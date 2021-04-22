import matplotlib.pyplot as plt
import numpy as np
import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd
import plots.median as mm



def bar_results(df, category, year, save=False, dpi=80, test=False):

    df = df[(df['в/к'] == category) & (df['Год']==year)& (df['Вид']=='ДЦ')]

    names=df['Ф.И.']
    gold=df[:1]
    silver=df[1:2]
    bronze=df[2:3]

    figure_width=len(df)

    fig, ax = plt.subplots(1, 1, figsize=(figure_width, 10))
    ax.bar(df['Ф.И.'], df['Толчок ДЦ'], color='skyblue', zorder=3)
    ax.bar(df['Ф.И.'], (df['Толчок ДЦ']), color='paleturquoise', zorder=3, alpha=0)
    ax.bar(gold['Ф.И.'], (gold['Толчок ДЦ']), color='gold', zorder=3, alpha=1)
    ax.bar(silver['Ф.И.'], (silver['Толчок ДЦ']), color='silver', zorder=3, alpha=1)
    ax.bar(bronze['Ф.И.'], (bronze['Толчок ДЦ']), color='orange', zorder=3, alpha=1)

    ax.set_yticks([30,35,40,45,50,55,60,65,70,75,80,85,90])    
    ax.set_xticks([])
    ax.grid(axis='y', zorder=0)
    ax.set_ylabel('Толчок ДЦ', size=18)

    ax.set_title('Чемпионат России ' + str(year) + '. ДЦ, вк ' + str(category), color='navy', fontsize=32)

    lenght=int(len(ax.patches)/2-1)

    i=0
    for b in ax.patches[:lenght]:
        ax.annotate(str(names.values[i]), 
                    (b.get_x()+b.get_width()/2, 2), 
                    color='royalblue',
                    va='bottom',
                    ha='center',
                    rotation=90,
                    size=30)
        i=i+1

    for b in ax.patches[int(len(ax.patches)/2):]:
        ax.annotate(str(int(b.get_height())), 
                    (b.get_x(), b.get_height()), 
                    color='dimgray',
                    size=30)



    plt.tight_layout()

    if save:
        path = '../giristat/images/'
        if category==999:
            filename='bar_results85+_CR_'  + str(year)  + '.png'
        else:
            filename='bar_results' + str(category) + '_CR_'  + str(year)  + '.png'
        plt.savefig(path+filename, dpi=dpi)


    plt.show(not test)
    return None
