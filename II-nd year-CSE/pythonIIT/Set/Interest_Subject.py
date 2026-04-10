user1={"python", "java", "c++", "c"}
user2={"datastructure", "c++", "java", "maths"}
u=user1.intersection(user2)
print("common interests between the users:")
print(u)
v=user1.difference(user2)
print("new courses to one user based on the other user's interest:")
print(v)
