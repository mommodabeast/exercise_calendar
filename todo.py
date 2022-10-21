import json
import re

def saving_json():
    schema = {"12/04/23":[["3 sets", "10 reps", "20 kg"], ["3 sets", "10 reps", "20 kg"]]}
    with open("savelist.json","w") as file:
        json.dump(schema, file, indent=4)
        file.write('\n')


def reading_json():
    with open("savelist.json","r") as file:
       data = json.load(file)
       print(data)


def convert_list():
    schema = [["namn på övning", ("3 sets", "10 reps", "10 kg")], ["namn på övning", ("4 sets", "12 reps", "15 kg")],["5","7reps","89"]]
    hello =''.join(str(l) for l in schema)
    num = re.findall(r'\d+', hello)
    print([int(x) for x in num])


def calculating_result():
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
 


 
 
 
 
 
 #   for int in num:
 #       print(int)