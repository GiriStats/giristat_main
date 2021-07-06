import matplotlib.pyplot as plt
import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd


def bar_results(disc, df, category, year, save=False, dpi=80, test=False):
    """Draws a bar diagram for given
    discipline, dataframe, category, year,
    and save the diagram depending on the flag save,
    with given resolution.
    The window will close automatically if test=True
    """

    if disc not in {'BI','LC'}:
        print("Disc must be LC or BI")
        return 
    discipline_title = {
        "LC": 'ДЦ',
        "BI": 'Двоеборье',
    }[disc]

    df = df[(df['WC'] == category) & (df['Year'] == year) & (df['Discipline'] == discipline_title)]
    names = df['Name']

    if disc == "LC":
        discipline = 'Толчок ДЦ'
        ax = draw_bars(df, discipline)
        build_second_bars_LC(ax)
    elif disc == 'BI':
        discipline = 'Сумма дв-рья'
        ax = draw_bars(df, discipline)
        df['sum_str'] = df[discipline].map('{0:g}'.format)
        sums = df['sum_str']
        build_second_bars_BI(ax, sums)

    set_title(ax, category, df, discipline_title, year)
    annotate_bars_with_names(ax,  names)
    draw_master_lines(year, category, disc)
    plt.tight_layout()

    save_img(category, dpi, year, save)
    plt.show(not test)
    return None


def draw_bars(df, discipline):
    gold = df[:1]
    silver = df[1:2]
    bronze = df[2:3]
    figure_width = len(df)
    fig, ax = plt.subplots(1, 1, figsize=(figure_width, 10))
    ax.bar(df['Name'], df[discipline], color='skyblue', zorder=3)
    ax.bar(df['Name'], (df[discipline]), color='paleturquoise', zorder=3, alpha=0)
    ax.bar(gold['Name'], (gold[discipline]), color='gold', zorder=3, alpha=1)
    ax.bar(silver['Name'], (silver[discipline]), color='silver', zorder=3, alpha=1)
    ax.bar(bronze['Name'], (bronze[discipline]), color='orange', zorder=3, alpha=1)
    ax.set_xticks([])
    ax.grid(axis='y', zorder=0)
    ax.set_ylabel('Толчок ДЦ', size=18)
    return ax


def save_img(category, dpi, year, save):
    if save:
        path = '../giristat/images/'
        if category == 999:
            filename = 'bar_resultsLC85+_CR_' + str(year) + '.png'
        else:
            filename = 'bar_resultsLC' + str(category) + '_CR_' + str(year) + '.png'
        plt.savefig(path + filename, dpi=dpi)


def annotate_bars_with_names(ax, names):
    lenght = int(len(ax.patches)/2-1)
    i = 0
    for b in ax.patches[:lenght]:
        ax.annotate(str(names.values[i]),
                    (b.get_x() + b.get_width() / 2, 2),
                    color='royalblue',
                    va='bottom',
                    ha='center',
                    rotation=90,
                    size=30)
        i = i + 1


def set_title(ax, category, df, discipline_title, year):
    title_color = 'g'
    if category == 999:
        ax.set_title('Чемпионат России ' + str(year) + '. ' + discipline_title + ', вк ' + df['WC'].any(),
                     color=title_color, fontsize=32)
    else:
        ax.set_title('Чемпионат России ' + str(year) + '. ' + discipline_title + ', вк ' + str(category),
                     color=title_color, fontsize=32)


def build_second_bars_LC(ax):
    for b in ax.patches[int(len(ax.patches)/2):]:
        ax.annotate(str(int(b.get_height())),
                    (b.get_x(), b.get_height()),
                    color='dimgray',
                    size=30)
    return None


def build_second_bars_BI(ax, sums):
    i = 0
    for b in ax.patches[:int(len(ax.patches)/2-1)]:
        ax.annotate(str(sums.values[i]),
                    (b.get_x(), b.get_height()),
                    color='dimgray',
                    size=30)
        i = i + 1


def draw_master_lines(year, category, disc):
    norms = perd.get_norms(year)
    if disc == 'BI':
        discipline = "BI"
    elif disc == "LC":
        discipline = "LC"
    else:
        print("discipline_title must be secific value")
        return

    norms_bi = norms[(norms['discipline'] == discipline)]

    msmk_bi_cat = norms_bi[(norms['title'] == "MSMK") & (norms_bi['weight_category'] == category)]
    ms_bi_cat = norms_bi[(norms['title'] == "MS") & (norms_bi['weight_category'] == category)]
    kms_bi_cat = norms_bi[(norms['title'] == "KMS") & (norms_bi['weight_category'] == category)]  

    msmk = msmk_bi_cat.iloc[0]['result']
    ms = ms_bi_cat.iloc[0]['result']
    kms = kms_bi_cat.iloc[0]['result']

    msmk_legend = "МСМК " + str(msmk)
    ms_legend = "МС " + str(ms)
    kms_legend = "KМС " + str(kms)

    plt.axhline(y=msmk, color='r', linestyle='-', linewidth=3, label=msmk_legend)
    plt.axhline(y=ms, color='g', linestyle='-', linewidth=3, label=ms_legend)
    plt.axhline(y=kms, color='b', linestyle='-', linewidth=3, label=kms_legend)

    plt.legend()
    plt.setp(plt.gca().get_legend().get_texts(), fontsize='15') 


# todo make reuse for BI
def bar_result_weightLC(df, category, year, save=False, dpi=80, test=False):
    discipline = 'Толчок ДЦ'
    df = df[(df['WC'] == category) & (df['Year'] == year) & (df['Discipline'] == 'ДЦ')]

    results = df[discipline].map('{0:g}'.format)
    names = df['Name']

    #todo find out
    # ymin = df['Weight'].min()
    weight_ylim=(50, 120)

    # figure_width=len(df[discipline])*0.8
    figure_width = len(df)*0.9
    title_color = 'g'

    fig, ax1 = plt.subplots(1, 1, figsize=(figure_width,8))

    ax1.bar(df['Name'], df[discipline], color='skyblue',  zorder=3)

    ax1.set_ylabel(discipline, size=18)
    ax1.grid(axis='y', zorder=0)

    ax2=ax1.twinx()
    ax2.bar(df['Name'], df['Weight'], color='w', alpha=0.6)

    weight_ylim = {
        63: (50, 90),
        68: (62, 102),
        73: (65, 105),
        85: (70, 120),
        999: (80, 180),
    }[category]

    ax2.set_ylim(weight_ylim)
    ax2.set_xticks([])
    ax2.set_ylabel('собственный вес, кг', size=18)

    i = 0
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
        i = i+1

    i = 0
    for b in ax1.patches:
        ax1.annotate(str(results.values[i]), 
                    (b.get_x()+0.1, b.get_height()-5),                
                    color='w',
                    size=30,
                    va='center',
                    ha='left',
                    rotation=90)
        i = i+1

    if category == 999:
        ax1.set_title('Чемпионат России ' + str(year) + '. ДЦ, вк ' + df['WC'].any(), color=title_color, fontsize=32)
    else:
        ax1.set_title('Чемпионат России ' + str(year) + '. ДЦ, вк ' + str(category), color=title_color, fontsize=32)

    plt.tight_layout()

    if save:
        path = '../giristat/images/'
        if category == 999:
            filename = 'bar_results_weightLC85+_CR_'  + str(year)  + '.png'
        else:
            filename = 'bar_results_weightLC' + str(category) + '_CR_'  + str(year)  + '.png'
        plt.savefig(path+filename, dpi=dpi)

    plt.show(not test)
    return None
