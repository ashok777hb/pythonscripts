#read input file
fin = open("data.txt", "rt")
#read file contents to string
data = fin.read()
#replace all occurrences of the required string
data = data.replace('pyton', 'python')
#close the input file
fin.close()
#open the input file in write mode
fin = open("data.txt", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()
