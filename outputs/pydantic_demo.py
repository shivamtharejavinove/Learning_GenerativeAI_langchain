from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str 
    age :Optional [int] = None # here we are defining also the value in advance that 
    email : EmailStr
    cgpa: float = Field(gt=0, lt=10, description=' a decimal value giving the cgpa of a student') # can give a default value by default = 4

new_student = {'name': " nitish", 'age':'32' , 'email':'anw@gmail.com', 'cgpa':1} # type coercing coerce and as we gave an email here it will show error here if it is not a valid email, with if not given correctly 
student = Student(**new_student)   # object Student of student class with new_student dictionary   
# print(type(student))
print (student)
# right now we are getting a pydantic function here but we can convert it to json, typeddict  from here only 
student_dict = dict(student)
print(student_dict['age'])
student_json = student.model_dump_json()
print(student_json)