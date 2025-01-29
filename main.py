import math
import random

#number of decimal digits to run the proof with
decimal_digits = 10
# account for "0."
const_num_str_len = decimal_digits + 2
# largest amount of characters of f"SQ.RT OF {n}"
max_formatted_str_len = 11
success_message = "THE NEW NUMBER GENERATED FROM THE DIAGONAL OF THE LIST OF IRRATIONAL NUMBERS ABOVE, DOES NOT MATCH ANY OF THE NUMBERS IN SUCH LIST."
result_message = "PROOF RESULT: THERE ARE DIFFERENT SIZED INFINITIES"
simulation_rerun_prompt = "Would you like to run another simulation? (y/n): "
generated_number_str = "NEW NUMBER GENERATED FROM DIAGONAL"

primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 }
additional_numbers = { 99 }
phi = (1 + math.sqrt(5)) / 2
constants = {
    "tau": math.tau,
    "pi": math.pi,
    "e": math.e,
    "phi": phi,
}

#returns a string that is either a substring or padded as necessary
def chop_str(string, length, rpad_char="0"):
    value = string[0:length]
    #pad string if we do not meet the required length
    while len(value) < length:
        value += rpad_char

    return value

#scans for the name of a constant and returns it if present
def name_of(n):
    for name, constant in constants.items():
        if n == constant:
            return name

    return None

#prompt user with main menu
def main_menu():
    print("MAIN MENU")
    print("---------")
    print("[1] Run Simulation")
    print("[2] Quit")

    user_in = input("")
    #attempt a cast to integer if it fails rerun the function
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
        #if the option is not either 1 or 2 rerun the function
        main_menu()

def run_proof():
    print("CANTOR'S DIAGONAL PROOF SIMULATION")
    #get union of all defined numbers as a list
    all_numbers = list(primes.union(additional_numbers).union(constants.values()))

    #ensure we have enough numbers
    if len(all_numbers) < decimal_digits:
        print(f"Not enough numbers to generate a cantor's diagonal proof with {decimal_digits} digits.")
        return main_menu()

    new_number = "0."
    for i in range(decimal_digits):
        n = random.choice(all_numbers)
        all_numbers.remove(n)
        name = name_of(n)
        operation = ""
        #name is none if the number is not constant
        if name is None:
            #name is not a constant, sqrt it and define and operation name
            operation = "SQ.RT OF "
            #set name to stringified number for later use
            name = str(n)
            n = math.sqrt(n)

        n /= 10

        #account for "0."
        digit = i + 2
        n = chop_str(str(n), const_num_str_len)
        new_number += n[digit]

        prepended_name = operation + name
        formatted_number_idx = f"{i+1:02d}"
        formatted_operation = f"{prepended_name:<{max_formatted_str_len}}"
        formatted_number = f"{n[0:digit]}[{n[digit]}]{n[digit + 1:const_num_str_len]}"

        print(f"{formatted_number_idx}. {formatted_operation} / 10 = {formatted_number}")

    #print results
    formatted_generated_number_string = f"{generated_number_str}: {new_number}"
    print(formatted_generated_number_string, end="\n\n")
    print(success_message, end="\n\n")
    print(result_message)

    rerun = input(simulation_rerun_prompt)
    #continue prompting until we have valid input
    while rerun.lower() != "y" and rerun.lower() != "n":
        rerun = input(simulation_rerun_prompt)

    if rerun.lower() == "y":
        run_proof()
    else:
        main_menu()

if __name__ == "__main__":
    main_menu()