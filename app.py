from calc_func import do_addition, do_subtraction
from multiply import do_multiplication

def main():
    print('Welcome to the calculator app')
    print("""
          \nSelect the function from the given options
          1. Add
          2. Substract
          3. Multiply
          """)
    
    user_input = input("Select the function")
    a = int(input('Value of A'))
    b = int(input('Value of B'))

    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "2":
        result = do_subtraction(a,b)
    elif user_input == "2":
        result = do_multiplication(a,b)

    print('Result: ', result)

    if __name__ == "__main__":
        main()
