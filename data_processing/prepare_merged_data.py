import pandas as pd

class DataEntry:
    '''represents an entry in a protocol'''

    def __init__(self):
        self.name = None
        self.birth = None
        self.wc = None
        self.weight = None
        self.discipline = None
        self.jerk = None
        self.snatch = None
        self.jerkLC = None
        self.wc_t = None
        self.team = None


    def __init__(self, name, birth, wc, weight, discipline, jerk, snatch, jerkLC, wc_t, team):
        self.name = name
        self.birth = birth
        self.wc = wc
        self.weight = weight
        self.discipline = discipline
        self.jerk = jerk
        self.snatch = snatch
        self.jerkLC = jerkLC
        self.wc_t = wc_t
        self.team = team




def get_merged_df(file1, file2):
    # 'source/RC_LC_2017-20.csv'
    # 'source/RC_BI_2017-20.csv'
    df_lc = pd.read_csv(file1)

    df_lc = df_lc.rename(columns={'Ком. очки':'Очки',
                                'JerkLC':'JerkLC'})
    df_lc = df_lc.drop(columns={'Unnamed: 2',
                                'Unnamed: 12'})
    df_lc = df_lc[df_lc['JerkLC'] != "снят врачом"]
    df_lc = df_lc[df_lc['JerkLC'] != 'Снят  врачом']
    df_lc['JerkLC'] = pd.to_numeric(df_lc['JerkLC'])
    df_lc['Weight'] = pd.to_numeric(df_lc['Weight'])

    df_bi = pd.read_csv(file2)
    df_bi = df_bi.drop(columns={'Unnamed: 2',
                                'Unnamed: 17'})
    df_bi = df_bi.rename(columns={'Ком. Очки':'Очки',
                                'Сумма       дв-рья':'Сумма дв-рья',
                                'Unnamed: 11':'Рывок (очки)',
                                'Snatch':'Snatch'})
    df_bi = df_bi[df_bi['Jerk'] != "Cнят врачом"]
    df_bi = df_bi[df_bi['Jerk'] != "Снят врачом"]
    df_bi = df_bi[df_bi['Snatch'] != "Снят  врачом"]
    df_bi = df_bi[df_bi['Weight'] != "снят врачом"]
    df_bi = df_bi[df_bi['Сумма дв-рья'] != "снят врачом"]
    df_bi['Jerk'] = pd.to_numeric(df_bi['Jerk'])
    df_bi['Weight'] = df_bi['Weight'].str.replace(',', '.').astype(float)
    df_bi['Weight'] = pd.to_numeric(df_bi['Weight'])
    df_bi['Сумма дв-рья'] = pd.to_numeric(df_bi['Сумма дв-рья'])

    # merge datasets
    df = df_lc.append(df_bi, sort=False)

    df['Name'] = df['Name'].apply(lambda x: str.strip(x))
    df['NameCoach'] = df['NameCoach'].astype(str)
    df['NameCoach'] = df['NameCoach'].apply(lambda x: str.strip(x))
    df['WC_t'] = df['WC'].apply(lambda x: str(x))

    df.loc[(df['Year'] == 2017) & (df['WC_t']=='999'), 'WC_t'] = "95+"
    df.loc[(df['Year'] != 2017) & (df['WC_t']=='999'), 'WC_t'] = "85+"

    return df


def get_df(file1):
    # All-RC-2017-20.csv
    df = pd.read_csv(file1)
    df = df.rename(columns={'Ком. очки': 'Очки',
                            'Сумма       дв-рья': 'Сумма дв-рья',
                            'Unnamed: 11': 'Рывок (очки)'})
    df = df.drop(columns={'Unnamed: 2', 'Unnamed: 18'})
    df = df[df['Jerk'] != "снят врачом"]
    df = df[df['Jerk'] != "Снят врачом"]
    df = df[df['Сумма дв-рья'] != "снят врачом"]
    df = df[df['JerkLC'] != "снят врачом"]
    df = df[df['Weight'] != "снят врачом"]

    df['Weight'] = df['Weight'].str.replace(',', '.').astype(float)
    df['JerkLC'] = pd.to_numeric(df['JerkLC'])
    df['Jerk'] = pd.to_numeric(df['Jerk'])
    df['Weight'] = pd.to_numeric(df['Weight'])
    df['Сумма дв-рья'] = pd.to_numeric(df['Сумма дв-рья'])
    df['Name'] = df['Name'].apply(lambda x: str.strip(x))
    df['NameCoach'] = df['NameCoach'].astype(str)
    df['NameCoach'] = df['NameCoach'].apply(lambda x: str.strip(x))
    df['WC_t'] = df['WC'].apply(lambda x: str(x))
    df.loc[(df['Year'] == 2017) & (df['WC_t']=='999'), 'WC_t'] = "95+"
    df.loc[(df['Year'] != 2017) & (df['WC_t']=='999'), 'WC_t'] = "85+"

    return df


def get_norms(year):
    norms = pd.read_csv('../source/norms.csv')
    year_norms = norms[(norms['year_from'] == year) | (norms['year_to'] == year) | (norms['year2'] == year) | (norms['year3'] == year)]
    return year_norms



def get_dataentries(df):
    '''Load all entries from file to DataEntries'''
    df = df.reset_index()
    entry = []

    for i in range(df.shape[0]):
        entry.append(DataEntry(df.Name[i],
                               df.BirthDate[i],
                               df.WC[i],
                               df.Weight[i],
                               df.Discipline[i],
                               df.Jerk[i],
                               df.Snatch[i],
                               df.JerkLC[i],
                               df.WC_t[i],
                               df.Team[i] ))


    # for i in range(df.shape[0]):
    # #     # print(i)
    #     entry.append(DataEntry())
    #     entry[i].name = df.Name[i]
    #     entry[i].birth = df.BirthDate[i]
    #     entry[i].team = df.Team[i]
    #     entry[i].weight = df.Weight[i]
    #     entry[i].jerk = df.Jerk[i]
    #     entry[i].snatch = df.Snatch[i]
    #     entry[i].jerkLC = df.JerkLC[i]
    #     entry[i].discipline = df.Discipline[i]
    #     entry[i].wc = df.WC[i]
    #     entry[i].wc_t = df.WC_t[i]

    # print(entry.__len__())

    for i in range(entry.__len__()):
        print(i, entry[i].name, entry[i].birth)

    return entry




