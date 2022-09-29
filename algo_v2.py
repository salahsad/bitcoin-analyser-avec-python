def calcul_moy(rates,nb_interval):

    somme = 0
    list = []
    for i in range(len(rates)):

        somme = somme + rates[i]['value']
        if i >= nb_interval :
            somme = somme - rates[i-nb_interval]['value']
            a = somme / nb_interval
        else :
            a = somme / (i+1)
        list.append({'date' : rates[i]['date'],'value': a})

    return list


