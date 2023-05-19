#SEMINAR ALJINOVIĆ, BRNAS, KLJAKOVIĆ GAŠPIĆ
import os
import operations
import time


all_relations = [
                ["ABCDEFGHIJ", [["DI", "B"], ["AJ", "F"], ["GB", "FJE"], ["AJ", "HD"], ["I", "CG"]]],
                ["ABCDEFGHIJ", [["A", "BCD"], ["B", "EF"], ["C", "G"], ["F", "HI"], ["D", "J"]]],
                ["ABCDEFGHIJ", [["A", "BC"], ["B", "DE"], ["C", "FGH"], ["F", "I"], ["GH", "J"]]],
                ["ABCDEFGHIJ", [["A", "BC"], ["B", "D"], ["B", "EF"], ["C", "G"], ["F", "HI"]]],
                ["ABCDEFGHIJK", [["AB", "CDE"], ["BD", "FG"], ["AFH", "IJ"], ["H", "K"], ["A", "H"], ["CGK", "B"]]],
                ["ABCDEFGHIJK", [["AB", "CD"], ["BC", "EFG"], ["DE", "HI"], ["FGH", "J"], ["AKC", "BEF"]]]
                #["IMA", [["I", "M"], ["M", "A"]]],
                #["INAE", [["I", "N"], ["N", "A"],["E","A"]]],
                #["IDPTE", [["DP", "T"], ["DP", "E"],["PT","D"]]]
]

while True:

    print("\n")
    print("Press [A] to input functional dependencies and relation schemes.")
    print("Press [B] to delete functional dependencies and relation schemes.")
    print("Press [C] to view functional dependencies and relation schemes.")
    print("Press [D] to select one of the functional dependencies and relation schemes.")
    print("Press [E] if you want to exit the program.")

    choice = input()
    choice = choice.upper()

    if choice == "A":
        os.system('cls')
        time.sleep(1)

        relation = operations.input_relation_scheme()
        dependencies = operations.new_functional_dependencies(relation)

        relation_with_dependencies = []

        relation_with_dependencies.append(relation)
        relation_with_dependencies.append(dependencies)

        all_relations.append(relation_with_dependencies)

        operations.print_relation(relation_with_dependencies)

    elif choice == "B":
        os.system('cls')
        time.sleep(1)
        operations.delete(all_relations)

    elif choice == "C":
        os.system('cls')
        time.sleep(1)
        operations.view_functional_dependencies(all_relations)

    elif choice == "D":
        operations.select(all_relations)
        
    elif choice == "E":
        print("Program exited!")
        break