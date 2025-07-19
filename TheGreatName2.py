#Libraries
from random import shuffle
from random import choice
from threading import Thread
from multiprocessing import cpu_count



#functions
def main():
    userin = input('Type a word:')
    global list1
    var1 = power(userin)
    for x in userin:
        var2 = power2(var1) 
        list1.append(var2)


def power(word):
    num = {ch: ord(ch) -96 for  ch in word}
    num = [num[ch] for ch in word]
    del word
    return num

def power2(num):
    shuffle(num)
    num = [abs(ch) for ch in num]
    num = list(map(str, num))
    num = "".join(num)
    return num

def re_var1():
    global shuffle
    del shuffle

def re_var2():  
    
   global choice
   del choice
   global list1
   del list1
   
def re_thread():
    global cpu_count
    if cpu_count >= 2:
        global task1
        del task1 
        global task2
        del task2
    del cpu_count

def results():
    print('number from list:' )
    print(choice(list1))
    re_var2()


#Vars
list1 = []
cpu_count = cpu_count()



#The main code
if cpu_count >= 2:
    main()
    task1 = Thread(target= re_var1)
    task1.start()
    task2 = Thread(target= results)
    task2.start()
    task1.join
    task2.join
    re_thread()

    
else:
    main()
    re_var1()
    results()
    re_thread()









