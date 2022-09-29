from datetime import date, datetime, timedelta
from rates_data_manager import *
import matplotlib.pyplot as plt
from algo_v2 import calcul_moy

date_start = date(2018,1,1)
date_end = date(2021,6,10)
assets = "BTC/EUR"

rates = get_and_manage_rates_data(assets, date_start, date_end)
M100 = calcul_moy(rates,100)
M20 = calcul_moy(rates,20)

my_interval = [20,50]
my_list=[]
for i in my_interval:
    my_tuple = calcul_moy(rates,i)
    my_list.append((my_tuple,i))


abc = achat_vente(my_list[0][0],my_list[1][0],1)


for a in abc :
    date = a[0]
    date_str = datetime.strptime(date,"%Y-%m-%d")
    if a[1] == False:
        plt.axvline(x=date_str, color='r')
    else :
        plt.axvline(x=date_str,color='g')


budget_initial = 1000
print("la date de debut est : " , date_start )
print("la date de fin est : " , date_end)
print("le budget initial est : ", budget_initial)

budget_final =compute_buy_and_sell_gains(budget_initial,rates,abc)
print("le budget final est ", budget_final)

plt.ylabel(assets)
rates_date = [datetime.strptime(r["date"],"%Y-%m-%d") for r in rates]
rates_values = [r["value"] for r in rates]
plt.plot(rates_date,rates_values)

for j in my_list:
    valeur = [i["value"] for i in j[0]]
    plt.plot(rates_date,valeur,label="MA"+ str(j[1]))
    plt.legend()

plt.show()