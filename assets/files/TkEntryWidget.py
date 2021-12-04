#!/usr/bin/python3 -i
# v.3.7+ order in dict()
import tkinter as tk
# based on https://python-course.eu/tkinter_entry_widgets.php
# https://www.pythontutorial.net/tkinter/tkinter-grid/

def tkForm(fields):
  """tkForm(fields: dict)->dict
  fields: {'label1': 'defVal1', ...}
  return: modified fields or {} if Esc
  >>> tkForm( {'Imię':'Iii', 'Imię 2':'iii 2', 'Nazwisko':'Nnn'} )
  {'Imię': 'Iii', 'Imię 2': 'iii 2', 'Nazwisko': 'Nnn'}
  """
  master = tk.Tk()
  entries = {}
  for i, (field, defVal) in enumerate(fields.items()):
    tk.Label(master, text=field).grid(row=i, sticky=tk.E, padx=3)
    ent = tk.Entry(master); ent.grid(row=i, column=1, padx=5, pady=5); ent.insert(0, defVal)
    if i==0: ent.focus_set()
    entries[field] = ent # ent.get() - value
  tk.Button(master, text='Esc', command=master.destroy).grid(row=len(fields), column=0, ipadx=5, pady=9)
  master.bind('<Escape>', lambda _: master.destroy())
  tk.Button(master, text='Ok', command=master.quit).grid(row=len(fields), column=1, ipadx=5, pady=9)
  master.bind('<Return>', lambda _: master.quit()) # [Enter] = [Ok]
    
  master.mainloop()
  try: # [Ok] - get modified values
    entries_di = {}
    for k,v in entries.items():
      entries_di[k] = v.get()
    master.destroy()
  except tk.TclError: # on master.destroy() = [x] or [Esc] - cancel
    entries_di = {}
  return entries_di

if __name__ == '__main__':
  # from TkEntryWidget import tkForm
  # di = tkForm( {'Imię':'Iii', 'Imię 2': 'iii 2', 'Nazwisko': 'Nnn'} )
  # print(di) # {'Imię': 'Iii', 'Imię 2': 'iii 2', 'Nazwisko': 'Nnn'}
  print("doctest: press ENTER")
  import doctest
  doctest.testmod()

