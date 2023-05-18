FileName = input("Enter the name of the file to write to including .txt")
name = input("name")
birth = (input("Birth year"))
grad = (input("Graduation Year"))
with open(FileName, 'w') as open_file:
    open_file.write(name + birth + grad)


open_file = open('star.txt', 'w')
open_file.write('Star Wars')
open_file.write('Rouge One')
open_file.close()