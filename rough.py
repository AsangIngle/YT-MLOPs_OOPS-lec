from OOPS_proj import chatbook
obj=chatbook()
#print(obj.name)
print(obj._chatbook__name)
#getter and setter

print(obj.get_name())
obj.set_name("addd")
print(obj.get_name())


#
user1=chatbook()
print(user1.id)
chatbook.set_id(10)
user2=chatbook()
print(user2.id)
user3=chatbook()
print(user3.id)
