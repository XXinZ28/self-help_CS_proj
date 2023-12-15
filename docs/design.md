# Project Design
**Team Name**: Group2 
**Team Members**: Doris Chi and Xinxin Zhang

## Sprint Planning
### Prototype I

**First Version**
* module 1: input user demographics and use this information to draw a matchstick man
* module 2: input user's class schedules by asking questions
* module 3: create graphics (buttons) to represent mood keywords for the user to choose from; after they finish with their selection, they can click the "continue" button to go to the next module
* module 4: the next module will pop out a new window with 3 buttons to click from: "class schedule summary","mood summary," "main summary," and "exit." These buttons will produce either a portion of the summary of their answers or a full summary of their answers, indicating whether the user is feeling overload/burnout or okay with their class schedules. 

**Second Version**
* module print:
  1) Ask user's input for name, class year, and favorite color.
  2) Call the different color stick figures from button module based on the user's chosen color.
  3) Ask questions about time distribution, temporarily store the value.
* module button:
  * import module graphics
  1) Import different color figures from internet
  2) draw buttons for choosing mood key words in the window
* main module:
  * call module print, module button, utility button, etc. 


### Prototype II
_Note: We recommend completing your project, in its entirety, by Prototype II. Then using the extra time to fix bugs that you find during demo day and incorporate other ideas._

* In **Main**
  * Import module 1 & turtle
  * Import module 2
  * Import module 3
  * Import module 4
    
* In **module 1**: demographics info
  * Import Turtle
  * In user input demographic information: input 1) user's name; 2) class year; 3) and favorite color.
    * if not matched with the string type, show the menu again until matching
    * if match, continue the program
  * use the turtle module to draw the matchstick figure based on their chosen color
  * store the user's name and class year and print them out
    
* In **module 2**: class sechedule
  * Ask users for input again by asking a series of questions: 
    * input(How many credits do you take for this semester?)
    * input(How much time do you spend on homework every day?)
    * input(How much time do you spend on meetings/ discussions/ lab/ club/ other commitments every day?)
    * input(Do you usually eat breakfast/lunch/dinner or skip it?)
    * input(How much time do you spend on work out every week?)
    * input(How much sleep do you get every day?)
  * store user response in a list called schedule

* In **module 3**: choose mood keywords 
  * draw a new window
  * draw several circles
  * ask users to click on the keywords shown on the window that describe their mood over the past month? Those keywords are appeared in the button. Choose all that applies:
    * i.e., Frustrated, Positive, Burnout, Anxious, Peaceful, Optimistic, Blue, etc.
  * use click point = GetMouse, if true (falls on a keywords), then return the word, store in a list called mood.
  * After finishing the keywords selection, click continue to go to the next module.


* In **module 4**: summary
  * draw a new window
  * draw 4 rectangles
  * use click point = GetMouse, if true (falls within a summary button)
  * then print a summary
    * the summary will use the elements in the lists and insert into a paragraph
  * else if inside the exit button
  * exit the game and print ("have a good day")

  
## User Personas
User are most likely to be College student; Someone who disoriented or worried about their schedules, care about mental health, want to have a better understanding or their work-life balance, or want to learn about time management.


## Project Structure 
_Insert a diagram/description of how individual components of the project are connected and interact with each other._

![<Team 2 project structure>](images/Structure.png)
 
