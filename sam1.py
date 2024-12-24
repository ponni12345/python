sample_string="hello world"
print(sample_string.find("world"))
values={"name":"bob","age":"25"}
print("my name is{name},i am {age}years old,".format_map(values))
values={"name":"ponni","age":"20","degree":"bsc","email":"ponnisivakumar"}
print("my name is {name},i am {age}years old,i am stady in {degree},mail id is {email},".format_map(values))
