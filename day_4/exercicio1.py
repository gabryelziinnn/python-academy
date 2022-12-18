'''
Debugging sayHello function
The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. 
It is your job to fix the code and get the program working again!

Example output:

Hello, Mr. Spock
'''
nomes = ['Mr. Spock', 'Captain Kirk', 'Liutenant Uhura', 'Dr. McCoy', 'Mr. Scott']

def say_hello():
    frase = 'Hello' + ', '
    for palavras in nomes:
        print(frase,palavras)
say_hello()
