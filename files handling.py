input1 = input("Enter text to write to file name: ")

file1 = open('output.txt', 'w')
writing_file1 = file1.write(input1)
print("Data Successfully written to output.txt")
file1.close()


input2 = input("Enter additional text to append: ")
file3 = open('output.txt', 'a')
writing_file3 = file3.write(input2)
print("Data Successfully written to output.txt")
file3.close()

with open('output.txt', "r") as file4:
    contents = file4.read()
    print(contents)
    file4.close()