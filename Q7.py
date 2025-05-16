import csv

def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

with open('collatz_sequences.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Starting Number", "Collatz Sequence"])
    for i in range(2, 513):
        seq = collatz_sequence(i)
        writer.writerow([i, ' '.join(str(num) for num in seq)])

print("Collatz sequences saved to 'collatz_sequences.csv'.")

#read back and validate
with open('collatz_sequences.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    errors = 0

    for row in reader:
        starting_num = int(row[0])
        csv_sequence = list(map(int, row[1].split()))
        actual_sequence = collatz_sequence(starting_num)

        if csv_sequence != actual_sequence:
            errors += 1
            print(f" Mismatch for {starting_num}:\nCSV:    {csv_sequence}\nActual: {actual_sequence}")

    if errors == 0:
        print("All sequences in the CSV file are correct.")
    else:
        print(f" {errors} sequences did not match.")


