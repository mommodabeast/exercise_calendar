#import pickle

def saving_and_reading_list():
    animals = ['Cat','Dog','Zebra','Lion','Tiger']
    with open('savelist.txt','a') as file:
        for item in animals:
            file.write("%s\n" % item)
        print('Task Completed')
        with open('savelist.txt','r') as file:
            list1 = []
            for line in file:
                line_strip = line.strip()
                line_split = line_strip.split()
                list1.append(line_split)
            list1[0][0]
            list_final = []
            for i in list1:
                for j in i:
                    list_final.append(j)
            print(list_final)
        
        
        
     #   pickle.dump(animals, file)
     #   aninmals = pickle.load(file)







