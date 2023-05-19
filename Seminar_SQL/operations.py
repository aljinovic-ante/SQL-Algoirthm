import os
import pkcandidates, thirdnf, boycecodd, relationcheck
import time

def input_relation_scheme():

    relation_scheme = input("Input Relation Scheme:")
    if(len(relation_scheme)<10 or not relation_scheme.isalpha()):
        input_relation_scheme()
    relation_scheme = relation_scheme.upper()

    lst = []

    for letter in relation_scheme:
        if letter not in lst and letter.isalpha():
            lst.append(letter)

    lst.sort()
    relation_scheme = ''.join(lst)

    print("Relation Scheme: " + relation_scheme)

    return relation_scheme


def new_functional_dependencies(relation):
    dependencies = []

    print("Relationship Creation Tool")
    print("To abort, input -1")
    print("Minimum: 5 relationship pairs ")

    user_input = 0
    count = 0

    while True:
        print("Please enter key attributes (" + str(count + 1) + "): ", end="")
        user_input = input("")

        single_dependency = []

        if user_input == "-1":
            if count >= 5:
                break

            else:
                print("Error: minimum relationship pairs not reached.")
                continue

        elif not relationcheck.is_in(user_input.upper(), relation) or not user_input:
            print("Error: " + user_input + " not in relation.")
            continue

        else:
            single_dependency.append(user_input.upper())

        print("Please enter non-key attributes (" + str(count + 1) + "): ", end="")
        user_input = input("")

        if user_input == "-1":
            if count >= 5:
                break

            else:
                print("Error: minimum relationship pairs not reached.")
                continue

        elif not relationcheck.is_in(user_input.upper(), relation) or not user_input:
            print("Error: " + user_input + " not in relation.")
            continue

        else:
            single_dependency.append(user_input.upper())

        dependencies.append(single_dependency)
        count += 1

    return dependencies


def view_functional_dependencies(all_relations):
    counter = 1
    all_rs_string = ""

    for rs in all_relations:
        all_rs_string += str(counter) + ". R = {" + rs[0] + "},    FR = {"

        for fd in rs[1]:
            all_rs_string += fd[0] + "->" + fd[1] + ", "

        all_rs_string = all_rs_string[:-2] + "}\n"
        counter += 1

    print(all_rs_string)


def print_relation(relation):
    print_string = "R = {" + relation[0] + "},    FR = {"

    for dependency in relation[1]:
        print_string += dependency[0] + "->" + dependency[1] + ", "

    print_string = print_string[:-2] + "}"

    print(print_string)

def delete(all_relations, message=""):
    view_functional_dependencies(all_relations)

    print(message)
    print("\n\nChoose a relation you wish to delete: ", end="")
    choice = int(input())

    if choice < 1 or choice > len(all_relations):
        message = "Error: invalid choice."
        delete(all_relations, message)

    else:
        print("Are you sure you want to delete relation " + str(all_relations[choice-1][0]) + "? (y/n)")

        if(input("")).lower() == 'y':
            del all_relations[choice-1]
            print("Deleted sucessfully")

        else:
            pass


def select(all_relations):
    print("\nThese are the functional dependencies and relation schemes.")
    print("Choose one of them by typing in the corresponding number.\n\n")

    view_functional_dependencies(all_relations)

    index = int(input()) - 1
    relation_choice = all_relations[index]

    os.system('cls')
    time.sleep(1)
    print("\nYou have selected this relation scheme with these functional dependencies: ")
    print_relation(relation_choice)
    # ovde sad ide trazenje primarnih kljuceva za odabranu FR I R

    while True:

        print("\nPress [3] if you want the Decomposition into Third Normal Form (3NF) for the selected FR and R")
        print("Press [4] if you want the Decomposition into Boyce-Codd Normal Form (BCNF) for the selected FR and R")
        print("Press [5] if you want to exit.\n")

        choice2 = int(input())
        list_of_pk = pkcandidates.candidates_for_pk(relation_choice)

        # print("LIST OF PK: " + str(list_of_PK))

        if choice2 == 3:
            os.system('cls')
            time.sleep(1)
            print("LIST OF PK: " + str(list_of_pk))
            thirdnf.normalise_to_3nf(relation_choice, list_of_pk)
            break

        elif choice2 == 4:
            os.system('cls')
            time.sleep(1)
            print("LIST OF PK: " + str(list_of_pk))
            result = boycecodd.bcnf(relation_choice, list_of_pk)
            print("Result is: " + str(result))
            break

        elif choice2 == 5:
            os.system('cls')
            time.sleep(1)
            break

        else:
            os.system('cls')
            time.sleep(1)
            print("You have not selected one of the offered possibilities! Choose again.")
