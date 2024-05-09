from suma import add
from resta import subtract 
from multiplicacion import multiply
from division import divide
from potencia import power
from modulo import modulo

"""
    Christian Ruiz
    Herramientas computacionales
    

"""
def main():
     score = 0

     while True:
         print('======== Menu ========'
         '\n6. modulo'
         '\n5. potencia'
         '\n4. division'
         '\n3. multiplicacion'
         '\n2. resta'
         '\n1. suma'
         '\n0. Exit')

         option = int(input('\nChoice an option: '))

         if option == 0:
             print(f"Your total score was {score}")
             break

         num_1 = int(input('Enter first number: '))

         num_2 = int(input('Enter second number: '))

         answer = int(input('Enter you answer: '))

         if option == 1:
             result = add(num_1, num_2)
         elif option == 2:
             result = subtract(num_1, num_2) 
         elif option == 3:
             result = multiply(num_1, num_2)
         elif option == 4:
             result = divide(num_1, num_2)
         elif option == 5:
             result = power(num_1, num_2)
         elif option == 6:
             result = modulo(num_1, num_2)

         if result == answer:
             score += 1
             print('Correct!!')

         else:
             print('Incorrect')
             print(f'======== Game Over ========'
             f'\nYou score is {score}')


# INITIALISER
if __name__ == "__main__":
    main()