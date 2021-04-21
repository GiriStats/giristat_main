import matplotlib.pyplot as plt


switcher = {
        'Толчок ДЦ':'LC',
        'Сумма дв-рья':'BI',
        'Толчок':'Jerk',
        'Рывок (сумма)':'Snatch_Summ'
    }

def draw_three_medians(df, discipline, years, save, dpi):

    medians1 = get_medians(df, years[0], discipline)
    medians2 = get_medians(df, years[1], discipline)
    medians3 = get_medians(df, years[2], discipline)

    w_categories_str, w_categories_str = get_categoties(years[0])

    if discipline == "Сумма дв-рья":
        medians1_snatch = get_medians(df, years[0], "Рывок (сумма)")
        medians1_jerk = get_medians(df, years[0], "Толчок")
        medians2_snatch  = get_medians(df, years[1], "Рывок (сумма)")
        medians2_jerk = get_medians(df, years[1], "Толчок")
        medians3_snatch = get_medians(df, years[2], "Рывок (сумма)")
        medians3_jerk = get_medians(df, years[2], "Толчок")


    if discipline=='Сумма дв-рья':
        ylim=(0,260)
    elif discipline=='Толчок ДЦ':
        ylim=(20,90)
    else:
        ylim=(0,300)
   
    fig, axes = plt.subplots(1,3, figsize=(10,4))

    axes[0].plot(w_categories_str, medians1, color='r', label='Сумма')
    axes[0].plot(w_categories_str, medians1, 'ro')
    axes[0].set_title(years[0], color='g')

    axes[1].plot(w_categories_str, medians2, color='r')
    axes[1].plot(w_categories_str, medians2, 'ro')
    axes[1].set_title(years[1], color='g')

    axes[2].plot(w_categories_str, medians3, color='r')
    axes[2].plot(w_categories_str, medians3, 'ro')
    axes[2].set_title(years[2], color='g')

    if discipline=='Сумма дв-рья':
        axes[0].plot(w_categories_str, medians1_snatch, color='g', label='Рывок')
        axes[0].plot(w_categories_str, medians1_snatch, 'go')
        axes[0].plot(w_categories_str, medians1_jerk, color='b', label='Толчок')
        axes[0].plot(w_categories_str, medians1_jerk, 'bo')

        axes[1].plot(w_categories_str, medians2_snatch, color='g')
        axes[1].plot(w_categories_str, medians2_snatch, 'go')
        axes[1].plot(w_categories_str, medians2_jerk, color='b')
        axes[1].plot(w_categories_str, medians2_jerk, 'bo')

        axes[2].plot(w_categories_str, medians3_snatch, color='g')
        axes[2].plot(w_categories_str, medians3_snatch, 'go')
        axes[2].plot(w_categories_str, medians3_jerk, color='b')
        axes[2].plot(w_categories_str, medians3_jerk, 'bo')

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
        ax.set_ylim(ylim)
        ax.grid()


    fig.tight_layout(rect=[0, 0, 1, 0.95])

    if save:
        path = '../giristat/images/'
        filename='Median_catagories_' + switcher.get(discipline, 'UN') + '_CR_'  + str(years)  + '.png'
        plt.savefig(path+filename, dpi=dpi)
        
    plt.show()


    return None


def get_categoties(year):
    if year == 2017:
        w_categories=[63, 68, 73, 78, 85, 95, 100]
        w_categories_str=['63','68','73','78','85','95','95+']
    else:
        w_categories=[63,68,73,85,100]
        w_categories_str=['63','68','73','85','85+']
    return w_categories, w_categories_str


def get_medians(df, year, discipline):
    df_year = df[df['Год']==year]

    df_year_63 = df_year[df_year['в/к']==63]
    df_year_68 = df_year[df_year['в/к']==68]
    df_year_73 = df_year[df_year['в/к']==73]
    df_year_85 = df_year[df_year['в/к']==85]
    df_year_999 = df_year[df_year['в/к']==999]

    medians=[]
    medians.append(df_year_63[discipline].median())
    medians.append(df_year_68[discipline].median())
    medians.append(df_year_73[discipline].median())
    medians.append(df_year_85[discipline].median())
    medians.append(df_year_999[discipline].median())

    if year == 2017:
        df_year_78 = df_year[df_year['в/к']==78]
        df_year_95 = df_year[df_year['в/к']==95]

        medians.insert(3, df_year_78[discipline].median())
        medians.insert(5, df_year_95[discipline].median())

    return medians

def draw_median(df, discipline, year, save, dpi):

    medians = get_medians(df, year, discipline)

    if discipline=='Сумма дв-рья':
        ylim=(0,260)
    elif discipline=='Толчок ДЦ':
        ylim=(20,90)
    else:
        ylim=(0,300)
   
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5.5))

    ax1.plot(w_categories, medians, 'r')
    ax1.plot(w_categories, medians, 'ro', label='медиана')
    ax1.set_xticks(w_categories)
    ax1.set_xlabel('в/к')
    ax1.set_yticks(medians)
    ax1.grid()
    ax1.legend(loc='upper left')

    ax2.plot(w_categories_str, medians, color='r')
    ax2.plot(w_categories_str, medians, 'ro')
    ax2.set_xlabel('в/к')
    ax2.set_ylim(ylim)
    ax2.grid()

    plt.suptitle('Медианы для каждой в/к. ' + discipline + '. ЧР ' + str(year), 
                size=22, 
                color='g', y=1)

    fig.tight_layout(rect=[0, 0, 1, 0.95])

    if save:
        path = '../giristat/images/'
        filename='Median_catagories_' + switcher.get(discipline, 'UN') + '_CR_'  + str(year)  + '.png'
        plt.savefig(path+filename, dpi=dpi)
        
    plt.show()