class StudentClass:#create a class called StudentClass
  def accept(self, Name, RollNo,marks1,marks2):#initalize the parameters
    self.Name= Name
    self.RollNo = RollNo
    self.marks1 = marks1
    self.marks2 = marks2

student1 = StudentClass('Nabatanzi Gorreti',11,70,80)# assign or add the object values
student2= StudentClass('Ayikor Robinah',10,65,90)
student3= StudentClass('Nalwoga Mariam',9,70,80)
#Display of the student information of student 1
print(student1.Name)
print(student1.RollNo)
print(student1.marks1)
print(student1.marks2)

# Search Function
def search(self, RollNo):
  for i in range(StudentClass.__len__()):
# iterate through the list containing
# student object and checks through
# roll no of each object
   if(StudentClass[i].rollno == RollNo):
# returns the object with matching
# roll number
    return i

# Delete Function
del student1.RollNo #deletes roll number of student1

# Update Function
student1.RollNo=13 # this will overwrite the first number to replace it with the 13 returning RollNo of student1 as 13



    