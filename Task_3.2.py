import turtle

def draw_koch_snowflake(t, order, size):
    """Функція для малювання фракталу сніжинки Коха"""
    for _ in range(3):
        draw_koch_curve(t, order, size)
        t.right(120)

def draw_koch_curve(t, order, size):
    """Функція для малювання однієї сторони фрактала сніжинки Коха"""
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        draw_koch_curve(t, order - 1, size)
        t.left(60)
        draw_koch_curve(t, order - 1, size)
        t.right(120)
        draw_koch_curve(t, order - 1, size)
        t.left(60)
        draw_koch_curve(t, order - 1, size)

def main():
    """Основна функція для налаштування екрану та запуску малювання"""
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    t.goto(-200, 100)
    t.pendown()
    
    draw_koch_snowflake(t, order, 400)
    turtle.done()

if __name__ == "__main__":
    main()
