
#1
from xml.etree.ElementTree import tostring


print("hello world")

#2a
name="Bushra"
print("hello",name)

#2b
name="Bushra"
print("hello"+" "+name)

#3a
num=23
print("hello",num)
#3b
num=23
print("hello"+ str(num) )

#4a
food1="pasta"
food2="sushi"

print("I love to eat {} and {}".format(food1 , food2))


#4b
food1="pasta"
food2="sushi"

print(f"I love to eat {food1} and {food2}")

#NINJA BONUS
food1="%s"%"pasta "
food2=" %s"%"sushi"

print("I love to eat %s and %s" %(food1,food2))
