import math
import random

primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 }
additional_numbers = { 99 }
constants = {
    "tau": math.tau,
    "pi": math.pi,
    "e": math.e,
    "phi": (1 + math.sqrt(5)) / 2,
}

def chop_str(string, length):
    return string[0:length]

def name_of(n):
    for name, constant in constants.items():
        if n == constant:
            return name

    return None

def main_menu():
    print("MAIN MENU")
    print("---------")
    print("[1] Run Simulation")
    print("[2] Quit")

    user_in = input("")
    try:
        option = int(user_in)
    except ValueError:
        return main_menu()

    if option == 1:
        run_proof()
    elif option == 2:
        print("Thank you for using the Cantor's Diagonal Proof Simulator. See you again soon!")
        quit()
    else:
        main_menu()

def run_proof():
    print("CANTOR'S DIAGONAL PROOF SIMULATION")
    all_numbers = list(primes.union(additional_numbers).union(constants.values()))
    new_number = "0."
    for i in range(10):
        n = random.choice(all_numbers)
        name = name_of(n)
        prepend = ""
        if name is None:
            prepend = "SQ.RT OF "
            name = str(n)
            n = math.sqrt(n) / 10
        else:
            n /= 10

        digit = i + 2
        n = chop_str(str(n), 12)
        new_number += n[digit]

        print(f"{i+1:02d}. {f"{prepend}{name}":<11} / 10 = {n[0:digit]}[{n[digit]}]{n[digit+1:12]}")
    print(f"\nNEW NUMBER GENERATED FROM DIAGONAL: {new_number}")
    print("\nTHE NEW NUMBER GENERATED FROM THE DIAGONAL OF THE LIST OF IRRATIONAL NUMBERS ABOVE, DOES NOT MATCH ANY OF THE NUMBERS IN SUCH LIST.")
    print("\nPROOF RESULT: THERE ARE DIFFERENT SIZED INFINITIES")
    rerun = input("Would you like to run another simulation? (y/n): ")
    while rerun.lower() != "y" and rerun.lower() != "n":
        rerun = input("Would you like to run another simulation? (y/n): ")

    if rerun.lower() == "y":
        run_proof()
    else:
        main_menu()

main_menu()
