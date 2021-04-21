# giristat

Here you can easily create plots and graphs and different kinds of visualization for kettlebell competition data. 

The website https://alekseidudchenko.github.io/giristat/ uses plots built using this project.

## How to use

### Competitors and results per category
### Medians for weight categories
draw_three_medians(df, discipline, years, save, dpi)
#### example

import plots.median_mean as m

df = perd.get_df()

mm.draw_three_medians(df, discipline='Сумма дв-рья', years=[2018,2019,2020],  save=True, dpi=80)

### An athlete dynamics over time


