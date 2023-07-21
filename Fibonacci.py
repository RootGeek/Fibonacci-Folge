ascii_art = '''
                                                       
 ____    ___    ___   _____   ____  _____  _____  _  __
|  _ \  / _ \  / _ \ |_   _| / ___|| ____|| ____|| |/ /
| |_) || | | || | | |  | |  | |  _ |  _|  |  _|  | ' / 
|  _ < | |_| || |_| |  | |  | |_| || |___ | |___ | . \ 
|_| \_\ \___/  \___/   |_|   \____||_____||_____||_|\_\\
                                                       
'''

# Funktion zur Berechnung der Fibonacci-Folge
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence

if __name__ == "__main__":
    print(ascii_art)  # Print the RootGeek ASCII art
    n = int(input("Geben Sie die Anzahl der Fibonacci-Zahlen ein: "))
    result = fibonacci(n)
    print("Fibonacci-Folge:")
    print(result)
