import graphics

# set a window
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 1400

# set a global list to store user's schedules
time_distr_lst = []


def get_user_demographics(win):
  """
  In this function, we ask users to input the demographic information(name, class year, and favorite color, for the preparation of drawing a stick man figure in button module.
  """
  
  name = input("What is your name?")

  exit_menu = False 
  
  while not exit_menu:
    classyr = int(input("What is your current class year? Choose from: 2027, 2026, 2025, 2024. Any J-class would be rounded: "))
    # if the class yr is not in the correct range, ask for the input again.
    if classyr == 2027 or classyr == 2026 or classyr == 2025 or classyr == 2024:
      break
    else:
      print("Pleas provide us a valid class year!")
      continue
      
  while not exit_menu:
    """
    The below code call different color figures downloaded from the internet, and print it according to user's favorite color. For example, if in print module, user responds Yellow, then the below function would print a pre-established yellow stick figure from the internet, and show it in the output window. 
    """
    
    favcolor =  input("What is your favorite color? Choose from below: red, yellow, dark blue, light blue, purple: ")

    if favcolor == "dark blue":
      dark_blue_image = graphics.Image(graphics.Point(300,300), "Figures/DarkBlue_Figure.png").draw(win)
    elif favcolor == "light blue":
      graphics.Image(graphics.Point(300, 300), "Figures/LightBlue_Figure.png").draw(win)
    elif favcolor == "red":
      graphics.Image(graphics.Point(300, 300),"Figures/Red_Figure.png").draw(win)
    elif favcolor == "yellow":
      graphics.Image(graphics.Point(300, 300),"Figures/Yellow_Figure.png").draw(win)
    elif favcolor == "purple":
      graphics.Image(graphics.Point(300, 300),"Figures/Purple_Figure.png").draw(win)
      
    else:
      print("Please select from the provided colors!")
      continue

    # After confirming the correct name, calss year, and favorite color, print all of them out.
    print('*' * 30)
    print(f"Your name is {name}.", end="\n")
    print(f"Your class year is {classyr}.", end="\n")
    print(f"Your favorite color is {favcolor}.", end="\n")
    print('*' * 30)

    exit_menu = True
  return name, classyr, favcolor


def time_distr():

  """
  In this function, after drawing the matchstick person, we ask users a series of questions to get to know their class schedule and time management during the semester.

  def time_distr():
    set the empty list of all answers in advance: time_distr_lst.
    set the loop:
      ask user's input about credits, and append user's answer to the time_distr_lst.
      repeat the same process of hwhrs, othertime, meals, and workout sleephrs.
    print the summary list of all answers.
  """
  
  global time_distr_lst
  
  while True:
    credits = int(input("How many credits do you have this semester? "))
    if credits >= 12 and credits <= 24: 
      time_distr_lst.append(credits)
      break
    else:
      print("Please provid a valid credits!")
      continue
      
  while True:
    hwhrs = int(input("How many hours do you spend on homework every day? "))
    if hwhrs > 0 and hwhrs <= 12:
      time_distr_lst.append(hwhrs)
      break
    else:
      print("Please provide a reasonable number of hours spent per day!")
      continue
      
  while True:
    othertime = int(input("How many hours do you spend on meetings/ discussions/ lab/ club/ other commitments every day? "))
    if othertime >= 0 and othertime <= 12:
      time_distr_lst.append(othertime)
      break
    else:
      print("Please provide a reasonable number of hours!")
      continue
      
  while True:
    meals = input("Do you usually eat breakfast/lunch/dinner or skip it? - Eat/Skip: ")
    if meals == "eat" or meals =="Eat" or meals == "skip" or meals == "Skip":
      time_distr_lst.append(meals)
      break
    else:
      print("Please select either Eat or Skip!")
      continue
      
  while True:
    workout = int(input("How many hours do you spend on workout every week? "))
    if workout >= 0 and workout <=12:
      time_distr_lst.append(workout)
      break
    else:
      print("Please provide a valid number!")
      continue
      
  while True:
    sleephrs = int(input("How many hours of sleep do you get every day? "))
    if sleephrs >=3 and sleephrs <= 15:
      time_distr_lst.append(sleephrs)
      break
    else:
      print("Please provide a valid number!")
      continue

  print(f"Here's your summary of time distribution in the semester in nutshell: {time_distr_lst}")
  print('*' * 30)


  return time_distr_lst



def schedule_summary():
  """
  In this function, we pass down the time_distr_lst and print it out. We will not call this function, only to use it in the summary.py module
  """
  global time_distr_lst
  print(f"You took {time_distr_lst[0]} credits this semester. This is equivalent to {time_distr_lst[0]*3} hours of study. You usually spend {time_distr_lst[1]} hours on homework every day, meaning {time_distr_lst[1]*7} hours of homework every week, and {time_distr_lst[2]} hours on other commitments every day. You usually {time_distr_lst[3]} a meal and spend {time_distr_lst[4]} hours to workout every week. Finally, you usually obtain a {time_distr_lst[5]} hours of sleep every day.")
  print('*' * 30)



def main():  
  win = graphics.GraphWin("Show Figure", WINDOW_WIDTH, WINDOW_HEIGHT)
  get_user_demographics(win)
  time_distr()
  win.close()

if __name__ == "__main__":
  main()