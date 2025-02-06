import tkinter as tk

# W I N D O W  A N D  E L S E
window = tk.Tk()
# 1
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.8)
window.geometry(f"{window_width}x{window_height}")

# 2
window.title("The most boring game")
window.configure(bg="white")

# 2.2 ---------- GRay-blue sidebar
sidebar = tk.Frame(window, width=155, bg="#9c9c9c")
sidebar.place(x=0, y=0, relheight=1)

# 2.3 ---------- Purplke backround
grid_frame = tk.Frame(window, bg="#3c00c7")
grid_frame.place(x=155, y=0, relwidth=1, relheight=1)

# 2.4 -------- the line
separator_canvas = tk.Canvas(window, width=5, bg="#16007a")
separator_canvas.place(x=149, y=0, relheight=1)
separator_canvas.create_line(0, 0, 0, window_height, fill="#16007a")



# T I C K I N G --------------------------------------
#Starting values:
x = 1
tick = 0

counter_value = 0  
counting = False
counting_scheduled = False

money_value = 0 #--> $$$$$$$$$$$ (-1 because 1 isn't 0)
hmyhc = 0 #HowMuchYouHaveClicked

UP1 = 100
up1 = UP1



#counter (stop and unstop)
def ticksss():
  global tick, tickspeed

  tickspeed = 1 / (.001 * float(slider.get())) 
  tick += 1
  ticks_text.set(value=f"Ticks: {format(tick)}")
  window.after(int(tickspeed), ticksss)



def toggle_counter():
  global counting, counter_value

  if not counting:
    counting = True
    counter_value = 1
    start_counting()
  else:
    counting = False



def start_counting():
    global counter_value, x, counting_scheduled

    if counting and not counting_scheduled:
      counting_scheduled = True
      window.after(int(tickspeed), reset_scheduled_flag)
      window.after(int(tickspeed), start_counting)
      
      counter_text.set(value=f"Counter: {format(counter_value)}")
      counter_value += 1
      calculate_money()


      
def reset_scheduled_flag():
  global counting_scheduled

  counting_scheduled = False



#THE FORMAT
def format(number):
  if number < 1e6:
    return f"{round(number)}"
  if number > 1e6:
    return f"{number:.3e}"
    
#elssseeeeee 

def upgrades():
  global hmyhc
  hmyhc += 1
  upgrade.config(text=f"Upgrades: {hmyhc:.0e}")



def calculate_money():
  global money_value, x
  
  money_value += x

  update() # Set configuration options for the label
  


def butt1buy():
  global money_value, x, up1, upgrades

  if money_value < up1:
    pass
  else:
    x += 1
    money_value -= up1
    up1 += UP1
    
    upgrades()
    
    update()
    butt1.config(text=f"HEREEEE\n {up1}$")



def butt1buyfully():
  global money_value, up1, y

  if money_value < up1:
    pass
  else:
    upgrades()

    update()

#update text format
def update():
  money_text.set(value=f"Money: ${format(money_value)}")



#For the "format"s * * * *
ticks_text = tk.StringVar()  # Set the configuration options for the label
counter_text = tk.StringVar()
money_text = tk.StringVar()


#$ bar info (On the side)
ticks = tk.Label(window, textvariable=ticks_text, bg="#9c9c9c", fg="red")
ticks.grid(row=0, column=0, padx=(4,4), pady=(4,0), sticky="w")

counter = tk.Label(window, textvariable=counter_text, width=0, height=0, bg="#9c9c9c")
counter.grid(row=1, column=0, padx=(4,4), pady=(4,0), sticky="w")

money = tk.Label(window, textvariable=money_text, width=0, height=0, bg="#9c9c9c", fg="light green")
money.grid(row=2, column=0, padx=(4,4), pady=(4,0), sticky="w")

upgrade = tk.Label(window, text=f"Upgrades: {hmyhc:.0e}", width=0, height=0, bg="#9c9c9c")
upgrade.grid(row=3, column=0, padx=(4,4), pady=(4,0), sticky="w")

# Create buttons using the grid layout + SLIDER & COUNTEr
# COunter Togglleee
buttcounter = tk.Button(grid_frame, text="Toggle ON/OFF", width=10, height=2, bg="white", command=toggle_counter)
buttcounter.grid(row=0, column=0, padx=(10,0), pady=(10,10))
# SlideR
slider = tk.Scale(grid_frame, from_=1, to=100, orient="horizontal", width=19, bg="white")
slider.grid(row=0, column=1, padx=(0,0), pady=(10,10), columnspan=4, sticky="w")
ticksss(), toggle_counter(), toggle_counter() #(for starting the ticks and counter, and because else it doesn't show up)
# 1
butt1 = tk.Button(grid_frame, text=f"HEREEEE\n {up1}$", width=10, height=2, bg="white", command=butt1buy)
butt1.grid(row=1, column=0, padx=(10,0), pady=(10,5))
butt1u = tk.Button(grid_frame, text="↑", width=3, height=2, bg="white", command=butt1buyfully)
butt1u.grid(row=1, column=1, padx=(0,0), pady=(10,5), sticky="w")

# 2
butt2 = tk.Button(grid_frame, text="Upgrade 2\n1,000$", width=10, height=2, bg="white")
butt2.grid(row=2, column=0, padx=(10,0), pady=(5,5))
butt2u = tk.Button(grid_frame, text="↑", width=3, height=2, bg="white")
butt2u.grid(row=2, column=1, padx=(0,0), pady=(5,5), sticky="w")

# 3
butt3 = tk.Button(grid_frame, text="Upgrade \nUUU", width=10, height=2, bg="white")
butt3.grid(row=3, column=0, padx=(10,0), pady=(5,5), sticky="w")

# Affichage de la fenêtre ----------------
window.mainloop()