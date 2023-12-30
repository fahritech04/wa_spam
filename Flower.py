import turtle

def draw_petal(t, radius):
    """Draws a single petal using the turtle t and the specified radius"""
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)

def draw_flower():
    """Draws a flower using multiple petals"""
    window = turtle.Screen()
    window.bgcolor("white")

    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.color("red")
    flower.speed(2)

    for _ in range(6):  # Draw 6 petals
        draw_petal(flower, 100)
        flower.left(60)

    flower.right(90)
    flower.forward(300)

    window.exitonclick()

draw_flower()
