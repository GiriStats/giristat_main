import pandas as pd


def get_df(file1, file2):
    # 'source/RC_LC_2017-20.csv'
    # 'source/RC_BI_2017-20.csv'
    df_lc = pd.read_csv(file1)

    df_lc = df_lc.rename(columns={'Ком. очки':'Очки',
                                'JerkLC':'JerkLC'})
    df_lc = df_lc.drop(columns={'Unnamed: 2',
                                'Unnamed: 12'})
    df_lc = df_lc[df_lc['JerkLC'] != "снят врачом"]
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


def get_norms(year):
    norms = pd.read_csv('source/norms.csv')
    year_norms = norms[(norms['year_from'] == year) | (norms['year_to'] == year) | (norms['year2'] == year) | (norms['year3'] == year)]
    return year_norms

