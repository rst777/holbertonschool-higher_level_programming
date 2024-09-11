#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []  # Liste pour stocker les résultats

    for i in range(list_length):
        try:
            # Vérifie si l'indice est dans les limites des deux listes
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result_list.append(0)
            else:
                # Vérifie si les éléments sont des nombres (int ou float)
                if (isinstance(my_list_1[i], (int, float)) and
                        isinstance(my_list_2[i], (int, float))):
                    try:
                        result = my_list_1[i] / my_list_2[i]
                    except ZeroDivisionError:
                        print("division by 0")
                        result = 0
                else:
                    print("wrong type")
                    result = 0

        except Exception as e:
            result = 0

        finally:
            result_list.append(result)

    return result_list
