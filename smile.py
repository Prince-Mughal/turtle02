
# Import drawing package
import turtle as our_turtle
# Initialize Screen
window_screen = our_turtle.Screen()
# Initialize turtle
turtle_handler = our_turtle.Turtle()
# Procedure to handle Pen Movement
def set_pen_position(x_axis, y_axis):
  turtle_handler.penup()
  turtle_handler.goto(x_axis,y_axis)
  turtle_handler.pendown()
# Main Procedure
def main(color="white",speed='normal'):
    # Prepare screen
    window_screen.clearscreen()
    window_screen.bgcolor(color)
    turtle_handler.speed(speed)
    turtle_handler.hideturtle()
    # Draw Face
    set_pen_position(0,0)
    turtle_handler.circle(80)
    # Draw Left EYE
    set_pen_position(-30, 90)
    turtle_handler.color('black')
    turtle_handler.begin_fill()
    turtle_handler.circle(10)
    turtle_handler.end_fill()
    # Draw Right EYE
    set_pen_position(30, 90)
    turtle_handler.color('black')
    turtle_handler.begin_fill()
    turtle_handler.circle(10)
    turtle_handler.end_fill()
    # Draw Mouth
    set_pen_position(-40, 50)
    turtle_handler.color('black')
    turtle_handler.right(70)
    turtle_handler.circle(40, 135)
    # Write Apologies
    set_pen_position(1, -30)
    turtle_handler.write("Dear Fellows, I am Sorry!", align="center")

if __name__ == "__main__":
  main()

