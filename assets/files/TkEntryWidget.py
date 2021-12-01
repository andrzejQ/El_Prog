import tkinter as tk
# https://python-course.eu/tkinter_entry_widgets.php
# https://www.pythontutorial.net/tkinter/tkinter-grid/
optns = {'padx':7, 'pady':7} #

master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0, **optns)
tk.Label(master, text="Last Name ").grid(row=1, **optns)

e1 = tk.Entry(master); e1.grid(row=0, column=1, **optns)
e2 = tk.Entry(master); e2.grid(row=1, column=1, **optns)

def print_data(): # pierwszy string to e1.get(); zamiast e1 można użyć nazwy więcej-mówiącej
  print(f"""First Name: {e1.get()}
Last Name : {e2.get()}""")

tk.Button(master, text='Show', command=print_data).grid(row=3, column=0, sticky=tk.W, **optns)
tk.Button(master, text='Ok (&quit)', command=master.quit).grid(row=3, column=1, sticky=tk.E, **optns)

tk.mainloop()
try:
  # Po [Ok (quit)] weź wyniki z e1, e2:
  print_data()
  #...
  # master.destroy() # gdy już nie potrzebne
except tk.TclError:
  print ('Anulowanie - po zamknięciu okna przez [x] w nagłówku')

