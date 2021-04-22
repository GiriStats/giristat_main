# giristat

Here you can easily create plots and graphs and different kinds of visualization for kettlebell competition data. 

The website https://alekseidudchenko.github.io/giristat/ uses plots built using this project.

## How to use

### Competitors and results per category
coming soon

### Medians for weight categories
```python
draw_three_medians(df, discipline, years, save, dpi)
```

#### example
```python
import plots.median_mean as m

df = perd.get_df() # get your dataset any way you prefer 
mm.draw_three_medians(df, discipline='Сумма дв-рья', years=[2018,2019,2020],  save=True, dpi=80)
```
![image](https://alekseidudchenko.github.io/giristat/images/Median_catagories_BI_CR_%5B2018,%202019,%202020%5D.png)

### Biathlon 2D scatter
```python
c.draw_cartesian(df, category, year, save=False, dpi=80)
```

#### example
```python
import plots.cartesian as c

df = perd.get_df() # get your dataset any way you prefer 
c.draw_cartesian(df, category=63, year=2020, save=True, dpi=100)
```
![image](https://alekseidudchenko.github.io/giristat/images/snatch_jerck_scatter73_CR_2020.png)


### An athlete dynamics over time

comming soon


