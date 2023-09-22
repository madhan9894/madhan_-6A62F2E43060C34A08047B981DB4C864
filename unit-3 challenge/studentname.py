class Student:

  def __init__(self,name, roll_number,cgpa):
    self.name =name
    self.roll_number = roll_number
    self.cgpa =cgpa



def sort_students(student_list):
  #sort the list of students in descending order of CGPA
  sorted_student = sorted(student_list,
                         key=lambda student: student.cgpa,
                         reverse=True)
  #syntax - Lambda aeg.exp
  return sorted_students


#Example usage:
students =[
    students("Hari", "A123", 7.8),
    students("Srikanth", "A124", 8.9),
    students("saumya", "A125", 9.1),
    students("Mahidar", "A126", 9.9),
]

sorted_students = sort_student(students)

#print the sorted list of students
for students in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
student.roll_number,                                                    
                                             student.cgpa))