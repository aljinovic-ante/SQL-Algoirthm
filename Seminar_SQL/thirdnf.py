import relationcheck
import os
import time


def normalise_to_3nf(relation_choice_, pk_):
    os.system('cls')
    time.sleep(1)
    relation_choice=relation_choice_[1]
    pk=pk_[0]
    print("Third Normal Form: ")
    print("R : ", relation_choice_[0])
    print("FR : ", relation_choice)
    print("PK: ",pk)
    lista=[]
    for fr in relation_choice:
        fr_joined = ''.join(fr)
        #print("appendamo 1: "+str(fr_joined)+" u "+str(lista))
        if not relationcheck.is_combination_in(fr_joined,lista):
            lista.append(fr_joined)
            
        #print("FR_JOINED + " + str(fr_joined))
        
    #print(lista)
    
    sorted_pk = ''.join(sorted(pk))
    for word in lista:
        sorted_word = ''.join(sorted(word))
        sorted_pk=list(sorted_pk)
        sorted_word=list(sorted_word)
        #print("s pk"+str(sorted_pk))
        #print("s w"+str(sorted_word))
    
        if set(sorted_pk).issubset(set(sorted_word)):
            print("Result is: "+str(lista))
            break
    else:
        print("No match found. PK added.")
        lista.append(pk)
        print("Result is: "+str(lista))


def candidates_for_pk(relation_choice):
    candidates_list = []

    for item in relation_choice[1]:
        candidates_list.append(item)

    return candidates_list
