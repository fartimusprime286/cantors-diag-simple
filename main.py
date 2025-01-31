import math
import random

#number of decimal digits to run the proof with
decimal_digits = 10
# account for "0."
const_num_str_len = decimal_digits + 2
# largest amount of characters of f"SQ.RT OF {n}"
success_message = "THE NEW NUMBER GENERATED FROM THE DIAGONAL OF THE LIST OF IRRATIONAL NUMBERS ABOVE, DOES NOT MATCH ANY OF THE NUMBERS IN SUCH LIST."
result_message = "PROOF RESULT: THERE ARE DIFFERENT SIZED INFINITIES"
simulation_rerun_prompt = "Would you like to run another simulation? (y/n): "
generated_number_str = "NEW NUMBER GENERATED FROM DIAGONAL"
sqrt_op = "SQ.RT OF "

n_primes = 50
additional_numbers = { 99 }
phi = (1 + math.sqrt(5)) / 2
constants = {
    "tau": math.tau,
    "pi": math.pi,
    "e": math.e,
    "phi": phi,
}

def sieve_of_eratosthenes():
    witnesses = dict()
    #first prime
    n = 2
    #doesn't loop infinitely, stops and resumes at "yield"
    while True:
        if n not in witnesses:
            #discoverd new prime
            #yield n as next number for generator
            yield n
            #mark n^2 as a multiple
            witnesses[n*n] = [n]
        else:
            #n is a composite number
            for prime in witnesses[n]:
                #moves primes to their next multiple
                #example:
                #   1st iteration 2 is marked as prime and 4 (2*2) is marked as composite with 2 as a "witness"
                #   2nd iteration 3 is marked as prime and 9 (3*3) is marked as composite with 3 as a "witness"
                #   3rd iteration 4 is marked as composite, its witnesses are iterated over and moved forwards by 4
                #       it's current witness, 2, will be moved up to 6 (2*3) (its next multiple after 2), and marked as composite with 2 as a "witness"
                #   ...
                #   8th iteration 9 is marked as composite, its witnesses are iterated over and moved forwards by 9
                #       it's current witness, 3, will be moved up to 12 (3x4) (its next multiple after 3), and marked as composite with 3 as a "witness"
                #
                #   "sieves" out composite numbers with each subsequent iteration
                witnesses.setdefault(prime+n, []).append(prime)
            #delete prime_factors[n] as we have already reached n
            del witnesses[n]
        n += 1

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
    print("[2] Select Number of Primes")
    print("[3] Quit")

    user_in = input("")
    #attempt a cast to integer if it fails rerun the function
    try:
        option = int(user_in)
    except ValueError:
        return main_menu()

    if option == 1:
        run_proof()
    elif option == 2:
        select_n_primes()

    elif option == 3:
        print("Thank you for using the Cantor's Diagonal Proof Simulator. See you again soon!")
        quit()
    else:
        #if the option is not either 1 or 2 rerun the function
        main_menu()

def select_n_primes():
    global n_primes
    prompt = "Number of Primes: "
    user_in = input(prompt)
    try:
        user_in = int(user_in)
    except ValueError:
        return select_n_primes()

    n_primes = user_in
    main_menu()

def generate_primes(n):
    sieve = sieve_of_eratosthenes()
    primes = []
    for i in range(n):
        primes.append(next(sieve))

    return primes

def run_proof():
    print("CANTOR'S DIAGONAL PROOF SIMULATION")
    #get union of all defined numbers as a list

    primes = generate_primes(n_primes)
    #cast back to list for convenience
    all_numbers = list(set(primes).union(additional_numbers).union(constants.values()))

    #ensure we have enough numbers
    if len(all_numbers) < decimal_digits:
        print(f"Not enough numbers to generate a cantor's diagonal proof with {decimal_digits} digits.")
        return main_menu()

    new_number = "0."
    proof_numbers = random.sample(all_numbers, decimal_digits)

    #find the largest number for formatting
    len_largest_number = 0
    for n in proof_numbers:
        name = name_of(n)
        if name is None:
            name = str(n)

        length = len(name)
        if length > len_largest_number:
            len_largest_number = length

    max_formatted_str_len = len(sqrt_op) + len_largest_number

    for i in range(decimal_digits):
        n = proof_numbers[i]
        name = name_of(n)
        operation = ""
        #name is none if the number is not constant
        if name is None:
            #name is not a constant, sqrt it and define and operation name
            operation = sqrt_op
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