import relationcheck
import os
import time

def remove_from_temp(fr, temp):
    for letter in fr:
        if letter in temp:
            temp.remove(letter)
    return temp


def bcnf(relation_choice, pk_list):
    os.system('cls')
    time.sleep(1)
    print("Boyce-Codd Normal Form: ")
    relation_list = []

    for letter in relation_choice[0]:
        relation_list.append(letter)

    dependency_list = relation_choice[1]

    print("List R: => "+str(relation_list))
    print("List FR: => "+str(relation_choice[1]))
    print("List PK => "+str(pk_list))

    temp = relation_list
    temp2 = []

    for fr in dependency_list:
        if relationcheck.is_in(fr[0], temp):
            temp = remove_from_temp(fr[1], temp)
            temp2.append(fr)

    # check if one of the PK is left in the temp so we can append him to temp2 (final list)
    temp2 = check_pk(check_pk_in_temp(pk_list,temp), temp, temp2)
    return temp2

def check_pk_in_temp(pk_list,temp):
    for pk in pk_list:
        pk_temp=list(pk)
        #print("Pk temp je: "+str(pk_temp))
        if set(pk_temp).issubset(set(temp)):
            #print("Pk temp je: "+str(pk_temp) +"a subset je od "+str(temp))
            return pk

def check_nonkey(pk, temp):
    all_letters = ""

    for letter in temp: #abfg
        if letter not in pk:  #ab
            all_letters+=letter

    return all_letters



def check_pk(pk, temp, temp2):
    #print("PK koji smo poslali + "+str(pk))
    #print("temp + "+str(temp))
    #print("temp2 + "+str(temp2))
    temp_list = []

    pk_list = list(pk)
    #print("pk_list + "+str(pk_list))
    temp_str=""

    if set(pk_list).issubset(set(temp)):
        nonkey = check_nonkey(pk, temp)
        temp_list.append(pk)
        temp_list.append(nonkey)
        temp2.append(temp_list)

    return temp2
