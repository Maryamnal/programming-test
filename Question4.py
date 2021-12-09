#File handling
f=open('read.txt','x')#creating a file read.txt


print(f.read())# read content in the 'read.txt'file
f.write('''This course introduces the core python programming basics—including data types,
control flow structures, data structures, and functions. The course also discusses
the fundamental principles of Object-Oriented Programming. Students will solve
problems, explore real-world software development challenges, and create
practical and contemporary applications. The course will also introduce students
to version control using Git and GitHub. The students will use this throughout the
course to submit their assignments, and for collaboration and code management''')#add text to the file

f=open('read.txt.','r') 
print(f.read())# read content in the 'read.txt'file
f=open('write.txt.','w')# creating an empty file
f.write('write.txt')# write into write.txt file
