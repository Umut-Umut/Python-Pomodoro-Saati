import main

main.db.down_req() # database.py

import tkinter as tk

var_font = "Consolas 12"
var_bg = "#FFECC2"
size = [300, 100]
coord = [0, 0]
size_coord = f"{size[0]}x{size[1]}+{coord[0]}+{coord[1]}"

main_win = tk.Tk()
main_win.overrideredirect(1)
main_win.geometry(size_coord)
main_win.title("POMODORO")
main_win.configure(bg=var_bg)



# Labels
main_label = tk.Label(text="00:00:00", font="Consolas 24 bold", bg=var_bg)
main_label.pack(side='top')

# Frames
frame = tk.Frame()

# Buttons
main_button1 = tk.Button(frame, text="Başlat", font=var_font, width=8)
main_button2 = tk.Button(frame, text="Ayarlar", font=var_font, width=8)
main_button3 = tk.Button(frame, text="Çıkış", font=var_font, width=8)

main_button1.pack(side="left")
main_button2.pack(side="left")
main_button3.pack(side="right")


frame.pack()

# Button Commands
is_setting_open = False
def settings():
    global is_setting_open
    def ok():
        ent1_list = entry1.get().split(":")[::-1]
        ent2_list = entry2.get().split(":")[::-1]
        for i in range(2, -1, -1):
            ent1_list[i] = int(ent1_list[i])
            ent2_list[i] = int(ent2_list[i])

        main.work_time = ent1_list
        main.rest_time = ent2_list

        main.timer.stop()
        main.timer.set_time(main.work_time)
        main_button1.configure(text="Başlat")
        main.is_time_start = False

        label1.configure(text="1|" + main.to_string(ent1_list))
        label2.configure(text="2|" + main.to_string(ent2_list))
        main_label.configure(text=main.to_string(ent1_list))


    def back():
        global is_setting_open
        is_setting_open = False
        second_win.destroy()


    if is_setting_open == False:
        is_setting_open = True
        var_bg = "#FFECC2"

        second_win = tk.Toplevel(main_win, bg=var_bg)
        second_win.overrideredirect(1)
        second_win.geometry("300x100")
        second_win.title("SETTINGS")

        # Frames
        frame1 = tk.Frame(
            second_win,
            bg=var_bg
            )
        frame2 = tk.Frame(
            second_win, 
            bg=var_bg,
            width=30
            )
        frame3 = tk.Frame(
            second_win,
            bg=var_bg
            )

        # Entrys
        entry1 = tk.Entry(
            frame1,
            justify="center",
            font="Consolas 18",
            width=8
            )
        entry2 = tk.Entry(
            frame1, 
            justify="center", 
            font="Consolas 18", 
            width=8
            )
        entry1.insert(0, main.to_string(main.work_time))
        entry2.insert(0, main.to_string(main.rest_time))

        # Labels
        label1 = tk.Label(
            frame2, 
            text="1|" + main.to_string(main.work_time),
            font="Consolas 10",
            bg=var_bg
            )
        label2 = tk.Label(
            frame2,
            text="2|" + main.to_string(main.rest_time),
            font="Consolas 10",
            bg=var_bg
            )

        # Buttons
        button1 = tk.Button(
            frame3,
            text="Tamam",
            width=8,
            command=ok
            )
        button2 = tk.Button(
            frame3, 
            text="Geri", 
            width=8, 
            command=back
            )

        # Packs
        entry1.pack(side="left", padx=5)
        entry2.pack(side="right", padx=5)

        label1.pack(side="left", padx=20)
        label2.pack(side="right", padx=20)

        button1.pack(side="right", padx=5)
        button2.pack(side="left", padx=5)

        frame1.pack()
        frame2.pack()
        frame3.pack()
        
        second_win.mainloop()


command1 = lambda: main.start_time_check(main_label, main_button1)
command2 = lambda: settings()
command3 = lambda: main.exit_(main_win)
main_button1.configure(command=command1)
main_button2.configure(command=command2)
main_button3.configure(command=command3)

# Binds
lamb_transport = lambda e: main.transport(main_win, main_win.wm_maxsize(), size)
main_win.bind("<Button-3>", lamb_transport)

main_win.mainloop()
