import os
import database as db

def exit_(win):
    win.destroy()


# GUI Funcs
def to_string(time):
    text = []
    for i in time:
        if i == 0:
            text.append("00")
        elif i < 10:
            text.append("0" + str(i))
        else: text.append(str(i))
    
    return ":".join(text[::-1])

# Edge = 0 or 1 or 2 or 3
def transport(win, win_size, gui_size):
    if win.winfo_rootx() > 0:
        coord = f"300x100+0+0"
        win.geometry(coord)
    else:
        coord = f"300x100+{win_size[0]-gui_size[0]}+0"
        win.geometry(coord)



# Main Funcs
class clock:
    def __init__(self, time):
        self.second = time[0]
        self.minute = time[1]
        self.hour   = time[2]
        self.status = False

    def get_time(self):
        return self.second, self.minute, self.hour
    

    def set_time(self, time):
        self.second = time[0]
        self.minute = time[1]
        self.hour   = time[2]


    def stop(self):
        self.status = False


    def start(self):
        self.status = True


    def clock_calc(self):
        if self.status:
            self.second -= 1
            if self.second == -1 and (self.minute > 0 or self.hour > 0):
                self.second = 59
                if self.minute > 0:
                    self.minute -= 1
                if self.minute == 0 and self.hour > 0:
                    self.minute = 59
                    self.hour -= 1
            elif self.second == -1 and self.minute == 0 and self.hour == 0:
                return 1
        return 0


is_time_start = False
work_time = [0, 0, 0]
rest_time = [0, 0, 0]
timer = clock(work_time)

def start_time_check(label, button):
    global is_time_start, timer;

    # Stop and Resume
    if button.config("text")[-1] == "Devam":
        button.configure(text="Durdur")
        timer.start()
    elif button.config("text")[-1] == "Durdur":
        button.configure(text="Devam")
        timer.stop()

    if is_time_start == False:
        if work_time == [0, 0, 0] or rest_time == [0, 0, 0]:
            pass
        else:
            timer.set_time(work_time)
            timer.start()

            is_time_start = True
            button.configure(text="Durdur")

            start_time(label, button)


work = True
def start_time(label, button):
    global is_time_start, work    
    
    if is_time_start == False:
        return 0
    alarm = timer.clock_calc()

    if alarm:
        os.startfile("music\\music.mp3")
        if work:
            timer.set_time(rest_time)
            work = False
        else:
            timer.set_time(work_time)
            work = True

    time = to_string(timer.get_time())
    label.configure(text=time)

    label.after(1000, lambda: start_time(label, button)) # Her 1000 milisaniyede bir start_time çağırır
