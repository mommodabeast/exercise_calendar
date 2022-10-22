import json
import re

def save_json(filename, data_to_save):
    with open(filename,"w") as file:
        json.dump(data_to_save, file, indent=4)


def read_json(filename):
    with open(filename,"r") as file:
       data = json.load(file)
       return data


def convert_list(list_to_convert):
    list_string =''.join(str(l) for l in list_to_convert)
    num = re.findall(r'\d+', list_string)
    return [int(x) for x in num]


def calculating_result(schedule, user_performance):
    # This function needs to be edited and fixed. 
    lista = [[3, 9, 20], [4, 10, 25]]
    lista1 = lista[0]
    lista2 = lista[1]

    sets_result = lista1[0]/lista2[0]
    reps_result = lista1[1]/lista2[1]
    weight_result = lista1[2]/lista2[2]

    final_result = ((sets_result + reps_result + weight_result)/3)
    x = round(final_result, 2)
    percentage = x*100
    x = round(percentage,-1)
    return (f"{percentage}%")