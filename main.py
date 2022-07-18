from tkinter import * # for GUI
import random #for randomisng
import time
from PIL import Image, ImageTk #forimages
from tkinter import messagebox  # for message box

names = [] #list
asked = []#list
score = 0 #list

questions_answers = { #Questions that will be asked
    1: ["For how many days is a Test match scheduled?", '100 overs', '3 days','One day ', '5 days' ,'5 days',4],#Q1 4 is index 6
    2: [" The Olympics are held every how many years?",'3 years','8 years','4 years', '1 year','4 years',3],#Q2
    3: ["In soccer, what body part can’t touch the ball?", 'Head','Hands','Legs','Chest','Hands',2],#Q3
    4: ["What’s the diameter of a basketball hoop in inches?",'14 Inches','16 Inches','18 Inches','20 Inches','18 Inches',3],#Q4
    5: ["Which batsman started his international cricketing career at the age of 16?",'MS Dhoni','Virat Kohli','Joe Root','Sachin Tendulkar','Sachin Tendulkar',4],#Q5
    6: ["How many players are there in a football (soccer) team?",'7','9','11','13','11',3],#Q6
    7: ["Which sport is not played with a ball?",'Basketball','Football','Cricket','Ice Hockey','Ice Hockey',4],#Q7
    8: ["Where will the 2023 Cricket World Cup be hosted?",'Australia','India','New Zealand','England','India',2],#Q8
    9: ["Which famous boxer is frequently ranked as the best heavyweight boxer of all time?",'Muhammad Ali','Tyson Fury','Mike Tyson','Anthony Joshua','Muhammad Ali',1],#Q9
    10: ["Which sport does Serena Williams play?",'Basketball','Tennis','Cricket','Football','Tennis',2],#Q10



}
def randomQuestions (): #randomises questions
    global qnum  #the question number is the key in our dictionary
    qnum = random.randint(1,10) # Number of questions
    if qnum not in asked:# asked is a list we declared, so to start of with any number will be added
      asked.append(qnum)
    elif qnum in asked:
      randomQuestions()
     

class Mainpage:#start page
  def __init__(self, parent):
    background_color="lightgrey"#background color

    self.heading_label=Label(window, text = "General Knowledge Sports quiz", font =( "Times","19","bold"),bg=background_color)
    self.heading_label.place(x=100, y=20)#Heading of the quiz

    self.var1=IntVar()

    self.user_label=Label(window, text="Please Enter your name Below: ", font=( "Times","18","bold"),bg=background_color)
    self.user_label.place(x=300, y=270)#name heading
    

    self.entry_box=Entry(window)
    self.entry_box.place(x=420, y=320)#entry box
    

    self.start_button = Button(window, text="START", font=( "Helvetica","13","bold"), bg="Light green",command=self.name_storage)
    self.start_button.place(x=100, y=500)#start button

  def name_storage(self): #stores names
      name = self.entry_box.get()
        # component 6 error handling
      if name == '':
            messagebox.showerror('Name is required!!', 'Please enter your name!')
      elif len(name) > 15: # to make sure name entered is between 1-15
        messagebox.showerror('an error has occurred!', 'please enter a name between 1 and 15 characters')
      elif name.isnumeric():
            messagebox.showerror('an error has occurred!', 'Name can only consist of letters ONLY!!')
      elif not name.isalpha(): # to make sure name entered is only letters not numbers
        messagebox.showerror('an error has occurred!', 'No Symbols Please! Please Try Again!')
      else:# to make sure name entered is only letters not symbols

            names.append(name)  # add name to names list declared at the beginning
            print (names)
            self.heading_label.destroy() #destroys the heading label
            self.user_label.destroy() #destroys the uder label
            self.entry_box.destroy() #destroys the entry box
            self.start_button.destroy() #destroys the start button
            Quizpage(window) # now we open the quiz questions page

class Quizpage:#Quiz page

  def __init__(self, parent):
    background_color="white"#background color
 
 
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid() #frame of quiz page

    randomQuestions() #question randomiser

    self.question_label=Label(window, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold")) #questions
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.var1=IntVar()

    self.options1 = Radiobutton(window, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.options1.place(x=0, y=60) #option 1

    self.options2 = Radiobutton(window, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.var1, pady=10)
    self.options2.place(x=0, y=120) #option 2

    self.options3 = Radiobutton(window, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.var1, pady=10)
    self.options3.place(x=0, y=180) #option 3

    self.options4 = Radiobutton(window, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.var1, pady=10)
    self.options4.place(x=0, y=240) #option 4

    self.confirm_button = Button(window, text="Confrim",bg="white",command=self.test_progress)
    self.confirm_button.place(x=380, y=270)#confirm button which takes you to the next page 
    self.score_label = Label(window, text ='score')
    self.score_label.place(x=407, y=300)  
    
    self.leave = Button(window, text='Leave', font=('Helvetica', '13', 'bold'), bg='red', command=self.result_screen) #leave button which takes you to the exit page 

    self.leave.place(x=0, y=300)  
    
    
     
     
  def questions_setup(self):
     randomQuestions()
     self.var1.set(0)
     self.question_label.config(text=questions_answers[qnum][0])
     self.options1.config(text=questions_answers[qnum][1])
     self.options2.config(text=questions_answers[qnum][2])
     self.options3.config(text=questions_answers[qnum][3])
     self.options4.config(text=questions_answers[qnum][4])

 #score mechanics 
  def test_progress(self):
      global score # this score needs to be accessible to all
      scr_label=self.score_label
      choice=self.var1.get()# get the user choice, remember are con1 is the IntVar() method that stores the number chosen
      if len(asked)>9: # to determine if its the last question and just end the quiz after
        if choice == questions_answers[qnum][6]: # checking that the key  has the correct answer which is stored in index 6 of the value area
          score +=1 # adds one point to score
          scr_label.configure(text=score)  # will change label to new score when score is gained 
          self.confirm_button.config(text="Confirm") # will change the text on the button to confirm
          self.result_screen() # to open end screen (end box) when quiz is done
        else:
          score+=0 # score will stay the same
          time.sleep(2)
          scr_label.configure(text="The correct answer was: "+ questions_answers[qnum][5]) # this is to give the right answer instead of their score
          self.confirm_button.config(text="confirm") # button
          self.result_screen()
      else:
            if choice==0:  # if user does not select an option
              self.confirm_button.config(text="Try Again, you didn't select an option then submit again" ) # error message
              choice=self.var1.get() # still get the answer if they choose it
            else:
              if choice == questions_answers[qnum][6]:  # if the choice made is correct
                score+=1  # add +1 to score
                scr_label.configure(text=score)
                self.confirm_button.config(text="confirm")
                self.questions_setup() # move to the next question:
      
              else: # if choice was not the correct answer
                  score+=0 # score will stay the same
                  scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5]) # error message
                  self.confirm_button.config(text="Confirmn")
                  self.questions_setup() # move to the next question:


  def result_screen(self): # method to end screen
    window.destroy()
    name = names[0]
    open_end_object = end()



class end:


  def __init__(self):
        background_color = 'black' #Background color of the page
        global end_window
        end_window = Tk()
        end_window.title('Exit Box') #Window title
        end_window.geometry('600x600') #Window size

        self.end_frame = Frame(end_window, width=700, height=600,bg=background_color)
        self.end_frame.grid(row=1)

        self.end_heading = Label(end_window,text='Thank You For Trying Out The Quiz  ',  font=('Tw Cen Mt', 22, 'bold'), bg='white') #Code for main heading of the page
        self.end_heading.place(x=15, y=35) #Location of the heading

        self.exit_button = Button(end_window,text='Exit',width=10,bg='red',font=('Tw Cen Mt', 12, 'bold'),command=self.close_end,) #Code for the exit button
        self.exit_button.place(x=260, y=200) #Location of the heading

        self.list_label = Label(end_window, text='Do not hesitate to try again' + str(names),font=('Tw Cen Mt', 12, 'bold'),width=40, bg='white') #Code for label to try again
        self.list_label.place(x=110, y=80) #Location of the label
        
        self.final_score = Label(end_window, text='Your final score is ' + str(score), font=('Tw Cen Mt', 12, 'bold'), width=40, bg='white') #Code for quiz summary
        self.final_score.place(x=110, y=150)#Location of the label
        
  
  
  def close_end(self):
      self.end_frame.destroy() #destroys the end frame label
      self.end_heading.destroy() #destroys the end heading label
      self.exit_button.destroy() #destroys the exit button
      self.list_label.destroy() #destroys the list label
      end_window.destroy() #destroys the end window
  
  
  
if __name__ == '__main__':
  window = Tk()
  window.title('12CSC Quiz')
  window.geometry('700x600')
  bg_image = Image.open('img4.jpg')
  bg_image = bg_image.resize((1000, 600), Image.ANTIALIAS)
  bg_image = ImageTk.PhotoImage(bg_image)
  image_label = Label(window, image=bg_image)
  image_label.place(x=0, y=0, relwidth=1, relheight=1)
  start_object = Mainpage(window)
  window.mainloop()