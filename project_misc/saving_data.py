
def reading_data():
    d = {}                                                #empty dictionary
    with open("userdata.txt", "r") as file:               #opens file in read mode
        for line in file:                                 
            x = line.split(",")                           #split line up at "," and assign both parts to x
            x[-1] = x[-1].strip()                         #selects the last element in the list x and strips off whitespace
            a = x[0]                                      #part 0 goeas to a
            b = x[1]                                      #part 2 goes to b                                  #
            d[a] = b                                      #will put a and b together in the dictionary"d"
        return d


def saving_data():
    training = input("Vad vill du träna?")                
    date = input("När vill du köra?")
    with open("userdata.txt","a") as file:                #opens file in append mode
        file.write("\n")                                  #newline for every input
        file.write(training + "," + date)                 #puts training and date together and splits them with a ,
    
    
    
    
    
    
  
    




#  st_ls = []
   ##    for i in range(2):
     #       str_ls.append((input("Vad vill du köra för pass?" + str(i+1) + ": "))+ "/n")
    #file.write(str_ls)


#            c = len(b)-1                                  #length of b-1 beacuse of /n
#           b = b[0:c]                                     #goes from element 0 upto but not including /n

#    file = open("userdata.txt")
#    file.close()

#from multiprocessing.resource_sharer import stop

#def saving_data():
#    with open("userdata.txt", "r") as read_file:
#        with open("userdata_input.txt","w") as write_file:
#            for line in read_file:
#                write_file.write(line)

#saving_data()   

#from this import d




#saving_data()   
   
    #name = f.write("Wazzup?")
    #f.write("Yessir!")
    
    #reading_size = 100
    #f_contents = f.read(reading_size)
    
    #while len(f_contents) > 0:
    #    print(f_contents, end="")
    #    f_contents = f.read(reading_size)
        
    #for line in f:
     #   print(line, end="")

   
    


    
