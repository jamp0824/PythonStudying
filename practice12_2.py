ex_dict = { "a" : "python", "b" : "C", "c" : "java"}

ex_dict["d"] = "C++"
#print(ex_dict)

ex_dict.update({"b":"javascript","e":"C#"})
#print(ex_dict)

del ex_dict["a"]

print(ex_dict)

key_list = list(ex_dict.keys())
values_list =list(ex_dict.values())

print(key_list)
print(values_list)
