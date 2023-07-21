# Fibonacci Python-Programm

Das Python-Programm "fibonacci.py" berechnet und gibt die Fibonacci-Folge aus. Die Fibonacci-Folge ist eine sequentielle Reihe von Zahlen, bei der jede Zahl die Summe der beiden vorherigen Zahlen ist.

## Funktionsweise

Das Programm verwendet eine Funktion namens "fibonacci(n)", die eine Liste mit den ersten "n" Fibonacci-Zahlen zurückgibt. Die Funktion "fibonacci(n)" nimmt eine Ganzzahl "n" als Eingabe und gibt eine Liste zurück, die die entsprechende Anzahl von Fibonacci-Zahlen enthält.

Zuerst werden Randfälle behandelt: 
- Wenn "n" kleiner oder gleich 0 ist, wird eine leere Liste zurückgegeben. 
- Wenn "n" gleich 1 ist, wird eine Liste mit nur der Zahl 0 zurückgegeben. 
- Wenn "n" gleich 2 ist, wird eine Liste mit den Zahlen 0 und 1 zurückgegeben.

Ansonsten wird eine Liste "fib_sequence" mit den Zahlen 0 und 1 initialisiert. Eine Schleife wird gestartet, die von 2 bis "n" läuft, um die weiteren Fibonacci-Zahlen zu berechnen. Jede Zahl wird durch Addition der beiden letzten Zahlen in der Liste "fib_sequence" berechnet und der Liste hinzugefügt.

Schließlich wird das Hauptprogramm ausgeführt, das den Benutzer nach der Anzahl "n" der gewünschten Fibonacci-Zahlen fragt. Die Eingabe des Benutzers wird in eine Ganzzahl konvertiert, und dann wird die Funktion "fibonacci(n)" aufgerufen, um die Fibonacci-Zahlen zu berechnen. Das Ergebnis wird anschließend auf der Konsole ausgegeben.

## Verwendung

Um die Fibonacci-Folge für eine bestimmte Anzahl von Zahlen zu berechnen, führen Sie das Programm aus und geben Sie die gewünschte Grenze "n" ein, wenn Sie dazu aufgefordert werden. Das Programm zeigt dann die Fibonacci-Zahlen bis zur angegebenen Grenze auf der Konsole an.

## Beispiel


