import graphics
import buttons
import myprint


def summary_buttons(win):

#draw 3 output buttons
  schedules = graphics.Rectangle(graphics.Point(100, 100), graphics.Point(150, 150))
  mood = graphics.Rectangle (graphics.Point(300, 100), graphics.Point(350, 150))
  total_summary = graphics.Rectangle (graphics.Point(100, 200), graphics.Point(150, 250))
  Exit = graphics.Rectangle (graphics.Point(300, 200), graphics.Point(350, 250))

  text0 = graphics.Text(graphics.Point(200,50), "Please select your option of summary!")
  text0.draw(win)
  text1 = graphics.Text(graphics.Point(125, 125), "schedules")
  text1.draw(win)
  text2 = graphics.Text(graphics.Point(325, 125), "mood")
  text2.draw(win)
  text3 = graphics.Text(graphics.Point(125, 225), "total summary")
  text3.draw(win)
  text4 = graphics.Text(graphics.Point(325, 225), "Exit")
  text4.draw(win)

  schedules.draw(win)
  mood.draw(win)
  total_summary.draw(win)
  Exit.draw(win)

  return schedules, mood, total_summary, Exit


def summary_text(win, schedules, mood, total_summary, Exit):
  """
  In this function, we create the central global loop to call all the functions in other modules as the display of summary for users' reference in the end. It is still display in the button window. 
  """
  
  while True:
    click = win.getMouse()
    if click is None:
      continue
    if buttons.inside(click, schedules):
      myprint.schedule_summary()
      continue 
    if buttons.inside(click, mood):
      buttons.mood_summary()
      continue
    if buttons.inside(click, total_summary):
      myprint.schedule_summary()
      buttons.mood_summary() 
    if buttons.inside(click, Exit):
      print("good bye!")
      break
  win.close()

def main():
  # set the window
  win = graphics.GraphWin("Summary",500,300)
  schedules, mood, total_summary, Exit = summary_buttons(win)
  summary_text(win, schedules, mood, total_summary, Exit)


if __name__ == "__main__":
  main()