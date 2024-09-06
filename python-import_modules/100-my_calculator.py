#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
def main():
    # Vérifie le nombre d'arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Récupère les arguments
    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]

    # Conversion en entier
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Vérifie l'opérateur
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Affiche le résultat
    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()
