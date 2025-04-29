from pydantic import BaseModel,EmailStr,Field
from typing import Optional 

class Student(BaseModel):
    
    name: str="Gagan"
    age: Optional[int]=None #optional field
    email: Optional[EmailStr]=None #optional field
    cgpa : float = Field(gt=0,lt=10.0,default=5,description="A decimal value representing the cgpa of the student") #greater than 0.0


new_student={'age':32,'email':'gagannarang0804@gmail.com','cgpa':9} #gives validation , wont run if not string or selected data type 

student=Student(**new_student)

student_dict=dict(student)

print(student_dict['age'])