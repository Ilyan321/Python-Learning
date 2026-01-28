person={"name":["Ilyan","fazal","mudasir"],"age":[19,20,21]}
person1={"name1":["Ilyan1","fazal1","mudasir1"],"age1":[19,20,21]}
print(person["name"])    # print key
person["email"]="ilyaankhan342@gmail.com"   #add key
del person["age"]   #delete key
dic2=person | person1   #merge two dictionaries
print(dic2)   #print entire dictionary

ndic={
    "person": {"name":["Ilyan","fazal","mudasir"],"age":[19,20,21]},
    "person1": {"name1":["Ilyan1","fazal1","mudasir1"],"age1":[19,20,21]}
}
print(ndic)