import turtle

n1 = int(input("Enter the no of the sides of the polygon : "))
l1 = int(input("Enter the length of the sides of the polygon : "))

for _ in range(n1):
	turtle.forward(l1)
	turtle.right(360 / n1)

turtle.penup()
turtle.goto(80,40)
turtle.pendown()
n2 = int(input("Enter the no of the sides of the polygon : "))
l2 = int(input("Enter the length of the sides of the polygon : "))

for _ in range(n2):
	turtle.forward(l2)
	turtle.right(360 / n2)