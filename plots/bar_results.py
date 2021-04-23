import matplotlib.pyplot as plt
import numpy as np
import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd
import plots.median as mm



def bar_resultsLC(df, category, year, save=False, dpi=80, test=False):

    df = df[(df['в/к'] == category) & (df['Год']==year)& (df['Вид']=='ДЦ')]

    names=df['Ф.И.']
    gold=df[:1]
    silver=df[1:2]
    bronze=df[2:3]
    title_color='g' #'navy'

    figure_width=len(df)

    fig, ax = plt.subplots(1, 1, figsize=(figure_width, 10))
    ax.bar(df['Ф.И.'], df['Толчок ДЦ'], color='skyblue', zorder=3)
    ax.bar(df['Ф.И.'], (df['Толчок ДЦ']), color='paleturquoise', zorder=3, alpha=0)
    ax.bar(gold['Ф.И.'], (gold['Толчок ДЦ']), color='gold', zorder=3, alpha=1)
    ax.bar(silver['Ф.И.'], (silver['Толчок ДЦ']), color='silver', zorder=3, alpha=1)
    ax.bar(bronze['Ф.И.'], (bronze['Толчок ДЦ']), color='orange', zorder=3, alpha=1)

    # ax.set_yticks([30,35,40,45,50,55,60,65,70,75,80,85,90])    
    ax.set_xticks([])
    ax.grid(axis='y', zorder=0)
    ax.set_ylabel('Толчок ДЦ', size=18)

    ax.set_title('Чемпионат России ' + str(year) + '. ДЦ, вк ' + str(category), color=title_color, fontsize=32)

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
            filename='bar_resultsLC85+_CR_'  + str(year)  + '.png'
        else:
            filename='bar_resultsLC' + str(category) + '_CR_'  + str(year)  + '.png'
        plt.savefig(path+filename, dpi=dpi)


    plt.show(not test)
    return None


def bar_resultsBI(df, category, year, save=False, dpi=80, test=False):

    discipline='Сумма дв-рья'
    df = df[(df['в/к'] == category) & (df['Год']==year)& (df['Вид']=='Двоеборье')]

    df['sum_str'] = df[discipline].map('{0:g}'.format)
    sums=df['sum_str']
    names=df['Ф.И.']
    
    gold=df[:1]
    silver=df[1:2]
    bronze=df[2:3]
    title_color='g' #'navy'

    figure_width=len(df)

    fig, ax = plt.subplots(1, 1, figsize=(figure_width, 10))
    ax.bar(df['Ф.И.'], df[discipline], color='skyblue', zorder=3)
    ax.bar(df['Ф.И.'], (df[discipline]), color='paleturquoise', zorder=3, alpha=0)
    ax.bar(gold['Ф.И.'], (gold[discipline]), color='gold', zorder=3, alpha=1)
    ax.bar(silver['Ф.И.'], (silver[discipline]), color='silver', zorder=3, alpha=1)
    ax.bar(bronze['Ф.И.'], (bronze[discipline]), color='orange', zorder=3, alpha=1)

    ax.set_xticks([])
    ax.grid(axis='y', zorder=0)
    ax.set_ylabel(discipline, size=18)

    ax.set_title('Чемпионат России ' + str(year) + '. Двоеборье, вк ' + str(category), color=title_color, fontsize=32)

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

    i=0
    for b in ax.patches[:lenght]:
        ax.annotate(str(sums.values[i]), 
                    (b.get_x(), b.get_height()), 
                    color='dimgray',
                    size=30)
        i=i+1



    plt.tight_layout()

    if save:
        path = '../giristat/images/'
        if category==999:
            filename='bar_resultsBI85+_CR_'  + str(year)  + '.png'
        else:
            filename='bar_resultsBI' + str(category) + '_CR_'  + str(year)  + '.png'
        plt.savefig(path+filename, dpi=dpi)


    plt.show(not test)
    return None


def bar_result_weightLC(df, category, year, save=False, dpi=80, test=False):

    discipline='Толчок ДЦ'
    df = df[(df['в/к'] == category) & (df['Год']==year)& (df['Вид']=='ДЦ')]

    results = df[discipline].map('{0:g}'.format)
    names=df['Ф.И.']

    # ymin = df['Соб. вес'].min()
    weight_ylim=(50,120)

    # print(str(category) +  ': ' + str(ymin))


    # figure_width=len(df[discipline])*0.8
    figure_width=len(df)*0.9
    title_color='g' #'navy'

    fig, ax1 = plt.subplots(1, 1, figsize=(figure_width,8))

    ax1.bar(df['Ф.И.'], df[discipline], color='skyblue',  zorder=3) #color='tomato',

    ax1.set_ylabel(discipline, size=18)
    ax1.grid(axis='y', zorder=0)

    ax2=ax1.twinx()
    ax2.bar(df['Ф.И.'], df['Соб. вес'], color='w', alpha=0.6)

    if category==63:
        weight_ylim = (50,90)
    elif category==68:
        weight_ylim = (62,102)
    elif category==73:
        weight_ylim = (65,105)
    elif category==85:
        weight_ylim = (70,120)
    elif category==999:
        weight_ylim = (80,180)

    ax2.set_ylim(weight_ylim)

    ax2.set_xticks([])
    ax2.set_ylabel('собственный вес, кг', size=18)

    i=0
    for p in ax2.patches:
        ax2.annotate(str(p.get_height()), 
                    (p.get_x()+0.48, p.get_height()-3.1), 
                    ha="left",
                    color='grey',
                    size=19,
                    rotation=90)
        ax2.annotate(str(names.values[i]), 
                    (p.get_x(), weight_ylim[0]+1),                
                    color='royalblue',
                    size=20,
                    rotation=90,)
        i=i+1
        

    i=0
    for b in ax1.patches:
        ax1.annotate(str(results.values[i]), 
                    (b.get_x()+0.1, b.get_height()-5),                
                    color='w',
                    size=30,
                    va='center',
                    ha='left',
                    rotation=90)
        i=i+1



    ax1.set_title('Чемпионат России ' + str(year) + '. ДЦ, вк ' + str(category), color=title_color, fontsize=32)

    plt.tight_layout()

    if save:
        path = '../giristat/images/'
        if category==999:
            filename='bar_results_weightLC85+_CR_'  + str(year)  + '.png'
        else:
            filename='bar_results_weightLC' + str(category) + '_CR_'  + str(year)  + '.png'
        plt.savefig(path+filename, dpi=dpi)


    plt.show(not test)
    return None