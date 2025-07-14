try:
    file1 = open('sample.txt', 'r')
    reading_file1 = file1.read()
    print(reading_file1)
    file1.close()
except FileNotFoundError:
    print("The File", "sample.txt", "was not found")