from tkinter import *
from PIL import Image,ImageTk
 #-------------------------------CONSTANTS----------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
checkmark=''
skip=0
current_state=NORMAL
timer=None
#-------------------------- TIMER RESET ---------------------------#
def reset_timer():
    global checkmark,reps
    window.after_cancel(timer)
    reps=0
    checkmark=''
    title_label.config(text="Timer",fg=GREEN)
    start_button.config(state=NORMAL)
    canvas.itemconfig(timer_text, text="00:00")

#-------------------------- TIMER MECHANISM ---------------------------#
def start_timer():
    global reps,current_state
    start_button.config(state=DISABLED)
    reps+=1
    if reps % 8 ==0:
        title_label.config(text="BREAK",fg=RED)
        count_down(LONG_BREAK_MIN*60)
        
    elif reps % 2 == 0:
        title_label.config(text="BREAK",fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        title_label.config(text="WORK",fg=GREEN)
        count_down(WORK_MIN*60)


#--------------------------- COUNTDOWN MECHANISM --------------------------#
def sec2min(sec):
    min=str(sec//60)
    remaining_seconds=str(sec%60)
    if(int(remaining_seconds)<10):
        remaining_seconds="0"+remaining_seconds
    text_final= min+":"+remaining_seconds
    return text_final
def count_down(count):
    global checkmark
    global skip
    canvas.itemconfig(timer_text, text=sec2min(count))
    if(count>0):
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        if(reps%2!=0):
            if(reps>8 and skip==1):
                checkmark=checkmark+"\n"
            checkmark="💯"+ checkmark
            check_marks.config(text=checkmark)


#---------------------------- UI SETUP -------------------------#
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

title_label= Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
title_label.grid(column=1,row=0)

canvas = Canvas(width=300,height=400,bg=YELLOW, highlightthickness=0)
#Load an image in the script
img = (Image.open("tomato.png"))
#Resize the Image using resize method
tomato_image= img.resize((300,300), Image.ANTIALIAS)
tom_img= ImageTk.PhotoImage(tomato_image)

canvas.create_image(150,200,image=tom_img)
timer_text = canvas.create_text(150,240, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)
start_button = Button(text="Start",bg=YELLOW, highlightthickness=0, command=start_timer, state=NORMAL)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",bg=YELLOW, highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)
check_marks = Label(text=checkmark, fg=RED, bg=YELLOW,font=(FONT_NAME, 35, "bold"))
check_marks.grid(column=1,row=3)
window.mainloop()
