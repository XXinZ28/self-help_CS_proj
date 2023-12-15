import graphics

# set a window
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 400
# create a global list called keywords to store user's mood
keywords = []

def buttons(win):
  """
  In this function, we created 12 buttons to represent mood keywords
  """
  tired = graphics.Rectangle(graphics.Point(30, 60), graphics.Point(60, 90))
  blue = graphics.Rectangle (graphics.Point(110, 60), graphics.Point(140, 90))
  excited = graphics.Rectangle (graphics.Point(190, 60), graphics.Point(220, 90))
  happy = graphics.Rectangle(graphics.Point(270, 60),graphics.Point(300, 90))
  hopeless = graphics.Rectangle(graphics.Point (350, 60), graphics.Point(380, 90))
  anxious = graphics.Rectangle(graphics.Point(30,160), graphics.Point(60, 190))
  worried = graphics.Rectangle(graphics.Point(110, 160), graphics.Point(140, 190))
  cheerful = graphics.Rectangle(graphics.Point(190, 160), graphics.Point(220, 190))
  optimistic = graphics.Rectangle(graphics.Point(270, 160), graphics.Point(300, 190))
  detached = graphics.Rectangle(graphics.Point(350, 160), graphics.Point(380, 190))
  peaceful = graphics.Rectangle(graphics.Point(30, 260), graphics.Point(60, 290))
  depressed = graphics.Rectangle(graphics.Point(110, 260), graphics.Point(140, 290))   
  finish = graphics.Rectangle(graphics.Point(230, 360), graphics.Point(260, 390))

  # add text to each button
  text1 = graphics.Text(graphics.Point(45, 75), "tired")
  text1.draw(win)
  text2 = graphics.Text(graphics.Point(125, 75), "blue")
  text2.draw(win)
  text3 = graphics.Text(graphics.Point(205, 75), "excited")
  text3.draw(win)
  text4 = graphics.Text(graphics.Point(285, 75), "happy")
  text4.draw(win)
  text5 = graphics.Text(graphics.Point(365, 75), "hopeless")
  text5.draw(win)
  text6 = graphics.Text(graphics.Point(45, 175), "anxious")
  text6.draw(win)
  text7 = graphics.Text(graphics.Point(125, 175), "worried")
  text7.draw(win)
  text8 = graphics.Text(graphics.Point(205, 175), "cheerful")
  text8.draw(win)
  text9 = graphics.Text(graphics.Point(285, 175), "optimistic")
  text9.draw(win)
  text10 = graphics.Text(graphics.Point(365, 175), "detached")
  text10.draw(win)
  text11 = graphics.Text(graphics.Point(45, 275), "peaceful")
  text11.draw(win)
  text12 = graphics.Text(graphics.Point(125, 275), "depressed")
  text12.draw(win)
  text13 = graphics.Text(graphics.Point(245, 375), "finish")
  text13.draw(win)
  text14 = graphics.Text(graphics.Point(215, 325), "Click keywords that describe your mood this month.")
  text14.draw(win)

  # draw buttons
  tired.draw(win)
  blue.draw(win)
  excited.draw(win)
  happy.draw(win)
  hopeless.draw(win)
  anxious.draw(win)
  worried.draw(win)
  cheerful.draw(win)
  optimistic.draw(win)
  detached.draw(win)
  peaceful.draw(win)
  depressed.draw(win)
  finish.draw(win)

  return tired, blue, excited, happy, hopeless, anxious, worried, cheerful, optimistic, detached, peaceful, depressed, finish
  


def inside(point, rectangle):
  """
  In this function, we get user's click point from their mouse, p1 is the lower left, p2 is the upper right
  """
  ll = rectangle.getP1()
  ur=rectangle.getP2()
  return ll.getX() < point.getX ()< ur.getX() and ll.getY()<point.getY()  < ur.getY()


  
def mood_summary():
  """
  In this function, we pass down the keywords list and print it out. We will not call this function, only to use it in the summary.py module
  """
  print(f"Here's how you've feeling lately: {keywords}. I hope your semester is not too stressful!")



def main():
  win = graphics.GraphWin("Mood Selection", WINDOW_WIDTH, WINDOW_HEIGHT)
    
  tired, blue, excited, happy, hopeless, anxious, worried, cheerful, optimistic, detached, peaceful, depressed, finish = buttons(win)
  
  buttons(win)

  global keywords

  # does the user click this keywords?
  while True:
    click = win.getMouse()

    if click is None:
      continue
    if inside(click, tired):
      keywords.append("tired")
      print("tired")
      continue 
    if inside(click, blue):
      keywords.append("blue")
      print("blue")
      continue
    if inside(click, excited):
      keywords.append("excited")
      print("excited")
      continue 
    if inside(click, happy):
      keywords.append("happy")
      print("happy")
      continue
    if inside(click, hopeless):
      keywords.append("hopeless")
      print("hopeless")
      continue 
    if inside(click, anxious):
      keywords.append("anxious")
      print("anxious")
      continue
    if inside(click, worried):
      keywords.append("worried")
      print("worried")
      continue 
    if inside(click, cheerful):
      keywords.append("cheerful")
      print("cheerful")
      continue
    if inside(click, optimistic):
      keywords.append("optimistic")
      print("optimistic")
      continue 
    if inside(click, detached):
      keywords.append("detached")
      print("detached")
      continue
    if inside(click, peaceful):
      keywords.append("peaceful")
      print("peaceful")
      continue 
    if inside(click, depressed):
      keywords.append("depressed")
      print("depressed")
      continue
    elif inside(click, finish):
      break
    return keywords

  print("you've finished your keyword selection")
  print(keywords)
  
  win.close()

if __name__ == "__main__":
  main()

      

  