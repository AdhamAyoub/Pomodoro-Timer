from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    check_labels.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    start_button.config(state="active")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state="disabled")

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(break_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_minute = str(count // 60).zfill(2)
    count_second = str(count % 60).zfill(2)
    canvas.itemconfig(timer_txt, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        check_labels.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_txt = canvas.create_text(102, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", width=10, command=start_timer)
start_button.grid(row=2, column=0)

check_labels = Label(font=(FONT_NAME, 15, "normal"), bg=YELLOW, fg=GREEN)
check_labels.grid(row=3, column=1)

reset_button = Button(text="reset", width=10, command=reset)
reset_button.grid(row=2, column=2)

window.mainloop()
