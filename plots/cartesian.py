import matplotlib.pyplot as plt
import sys
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")

snatch = 'Рывок (очки)'


def draw_cartesian(df, category, year, save=False, dpi=100, test=False):

    df = df[df['Discipline'] == 'Двоеборье']

    df = df[(df['WC'] == category) & (df['Year'] == year)]
    median_snatch = df[snatch].median()
    median_jerk = df['Jerk'].median()

    axis_label_size = 13
    axis_label_color = 'g'
    if category == 999:
        if year == 2017:
            title = 'Двоеборье. в/к 95+. ' + str(year)
        else:
            title = 'Двоеборье. в/к 85+. ' + str(year)
    else:
        title = 'Двоеборье. в/к ' + str(category) + '. ' + str(year)

    fig, axes = plt.subplots(1, 1, figsize=(12, 10))

    text_medians = 'median jerk = ' + str(median_jerk) + ' median snatch = ' + str(median_snatch)

    axes.set_title(title, size=19, color='g')
    axes.scatter(df['Jerk'], df[snatch], color='b', label=text_medians)
    axes.spines['left'].set_position('center')
    axes.spines['right'].set_color('none')
    axes.spines['bottom'].set_position('center')
    axes.spines['top'].set_color('none')
    axes.set_ylim(median_snatch-45, median_snatch+45)
    axes.set_xlim(median_jerk-90, median_jerk+90)
    axes.xaxis.set_ticks_position('bottom')
    axes.set_xlabel('толчок', size=axis_label_size, color=axis_label_color)
    axes.xaxis.set_label_coords(0.95, 0.45)
    axes.set_ylabel('рывок (очки)', size=axis_label_size, color=axis_label_color, rotation=0)
    axes.yaxis.set_label_coords(0.40, 0.95)

    # axes.legend(loc='lower left')

    for i in df.index:
        axes.annotate(df['Name'][i], (df['Jerk'][i], df[snatch][i]))

    for i in df.index:
        axes.annotate(str(df['Место'][i])+'  ', (df['Jerk'][i], df[snatch][i]), ha='right', color='b')

    plt.tight_layout()

    if save:
        path = '../giristat/images/'
        if category == 999:
            filename = 'snatch_jerck_scatter85+_CR_' + str(year) + '.png'
        else:
            filename = 'snatch_jerck_scatter' + str(category) + '_CR_' + str(year) + '.png'
        plt.savefig(path+filename, dpi=dpi)

    plt.show(not test)
    return None