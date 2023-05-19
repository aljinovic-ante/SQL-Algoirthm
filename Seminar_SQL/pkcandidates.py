from itertools import combinations

import relationcheck


def sortiraj_str(str1):
    after_sort = ''.join(sorted(str1))
    return after_sort


def candidates_for_pk(relation_choice):
    relation = relation_choice[0]
    lista = relation_choice[1]

    st = []
    candidates = []

    for i in range(1, len(relation)):
        temp = combinations(relation, i)
        st += temp

    for tup in st:
        tup = ''.join(tup)

        if candidates and len(candidates[0]) < len(tup):
            break

        tup_st = ""

        for rel in lista:
            if relationcheck.is_in(rel[0], tup):  # nadskup(tup, rel[0])  --> nadskup(nadskup, podskup)
                tup_st += rel[1]

            tup_st = sortiraj_str(tup_st)

        if tup_st == "":
            continue

        tup_st2 = tup_st + tup
        tup_st2 = "".join(set(tup_st2))

        counter = 0


        for rel in lista:
            if relationcheck.is_in(rel[0], tup_st2):
                tup_st2 += rel[1]
                tup_st2 = "".join(set(tup_st2))


        if relationcheck.is_in(tup_st2, relation) and len(relation) == len(tup_st2):
            candidates.append(tup)

    print("\n", candidates)
    print(" ")

    return candidates
