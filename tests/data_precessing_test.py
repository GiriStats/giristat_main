import sys 
sys.path.append("/home/aleksei/Dropbox/GiriStat/giristat_main")
import data_processing.prepare_merged_data as perd


def test(year):
    print(str(year) + "  " + str(len(perd.get_norms(year))))


# test(2017)
# test(2018)
# test(2019)
# test(2020)
# test(2021)
# test(2022)
# test(2023)


