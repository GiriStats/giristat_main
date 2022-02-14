import matplotlib.pyplot as plt

switcher = {
        'Толчок ДЦ': 'LC',
        'Сумма дв-рья': 'BI',
        'Толчок': 'Jerk',
        'Рывок (сумма)': 'Snatch_Summ'
    }


def draw_three_medians(df, discipline, years, save=False, dpi=80, test=False):

    medians_main = []

    for year in years:
        medians_main.append(get_medians(df, year, discipline))

    #todo make possible to have different categories.
    w_categories_str, w_categories_str = get_categories(years[0])

    if discipline == "Сумма дв-рья":
        medians_snatch = []
        medians_jerk = []

        for year in years:
            medians_snatch.append(get_medians(df, year, "Snatch"))
            medians_jerk.append(get_medians(df, year, "Jerk"))
  
    fig, axes = plt.subplots(1, 3, figsize=(10, 4))

    for i in range(3):
        axes[i].plot(w_categories_str, medians_main[i], color='r', label='Сумма')
        axes[i].plot(w_categories_str, medians_main[i], 'ro')
        axes[i].set_title(years[i], color='g')

    if discipline == 'Сумма дв-рья':
        for i in range(3):
            axes[i].plot(w_categories_str, medians_snatch[i], color='g', label='Рывок')
            axes[i].plot(w_categories_str, medians_snatch[i], 'go')
            axes[i].plot(w_categories_str, medians_jerk[i], color='g', label='Толчок')
            axes[i].plot(w_categories_str, medians_jerk[i], 'bo')

        plt.suptitle('Медианы для каждой в/к. Двоеборье.', 
                size=22, 
                color='g', y=1)

    else:
        plt.suptitle('Медианы для каждой в/к. ' + discipline + '.', 
                size=22, 
                color='g', y=1)

    axes[0].legend(loc='upper left')

    for ax in axes:
        ax.set_xlabel('в/к')
        ax.set_ylim(get_ylim(discipline))
        ax.grid()

    fig.tight_layout(rect=[0, 0, 1, 0.95])

    if save:
        path = '../giristat/images/'
        filename = 'Median_catagories_' + switcher.get(discipline, 'UN') + '_CR_' + str(years) + '.png'
        plt.savefig(path+filename, dpi=dpi)
        
    # plt.show(not test)
    plt.show() #TODO
    return None


def draw_median(df, discipline, year, save=False, dpi=80, test=False):
    if discipline not in {'Jerk', 'Snatch', 'JerkLC', 'Сумма дв-рья'}:
        print("*****************************ERROR*******************")
        print("Discipline not in {'Jerk', 'Snatch', 'JerkLC', 'Сумма дв-рья'}")
        return

    medians = get_medians(df, year, discipline)
    w_categories = get_categories(year)
   
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.5))

    for i in range(2):
        axes[i].plot(w_categories[i], medians, 'r')
        axes[i].plot(w_categories[i], medians, 'ro', label='медиана')
        axes[i].set_xticks(w_categories[i])
        axes[i].set_xlabel('в/к')
        axes[i].grid()
    
    axes[0].set_yticks(medians)
    axes[0].legend(loc='upper left')
    axes[1].set_ylim(get_ylim(discipline))

    plt.suptitle('Медианы для каждой в/к. ' + discipline + '. ЧР ' + str(year), 
                size=22, 
                color='g', y=1)

    fig.tight_layout(rect=[0, 0, 1, 0.95])

    if save:
        path = '../giristat/images/'
        filename = 'Median_categories_' + switcher.get(discipline, 'UN') + '_CR_' + str(year) + '.png'
        plt.savefig(path+filename, dpi=dpi)

    plt.show() #TODO
    # plt.show(not test)
    return None


def get_categories(year):
    if year == 2017:
        w_categories = [63, 68, 73, 78, 85, 95, 100]
        w_categories_str = ['63', '68', '73', '78', '85', '95', '95+']
    else:
        w_categories = [63, 68, 73, 85, 100]
        w_categories_str = ['63', '68', '73', '85', '85+']
    return w_categories, w_categories_str


def get_medians(df, year, discipline):
    df_year = df[df['Year'] == year]

    df_year_63 = df_year[df_year['WC'] == 63]
    df_year_68 = df_year[df_year['WC'] == 68]
    df_year_73 = df_year[df_year['WC'] == 73]
    df_year_85 = df_year[df_year['WC'] == 85]
    df_year_999 = df_year[df_year['WC'] == 999]

    medians = []
    medians.append(df_year_63[discipline].median())
    medians.append(df_year_68[discipline].median())
    medians.append(df_year_73[discipline].median())
    medians.append(df_year_85[discipline].median())
    medians.append(df_year_999[discipline].median())

    if year == 2017:
        df_year_78 = df_year[df_year['WC'] == 78]
        df_year_95 = df_year[df_year['WC'] == 95]

        medians.insert(3, df_year_78[discipline].median())
        medians.insert(5, df_year_95[discipline].median())

    return medians


def get_ylim(discipline):
    if discipline == 'Сумма дв-рья':
        ylim = (0, 260)
    elif discipline == 'JerkLC':
        ylim = (20, 90)
    elif discipline == 'Jerk':
        ylim = (0, 200)
    else:
        ylim = (0, 300)
    return ylim