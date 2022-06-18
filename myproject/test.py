from dataclasses import dataclass
import uuid
@dataclass
class Employee:
    name:str
    age:int
    employee_id:str
siddhart = Employee(name="Siddarth",age=30,employee_id=uuid.uuid4())

print(siddhart.age)