#!/usr/bin/python3 -i

import tkinter as tk
# based on https://python-course.eu/tkinter_entry_widgets.php
# https://www.pythontutorial.net/tkinter/tkinter-grid/

def tkForm(fields): 
  # fields: etykiety pól ( , ...) lub [ , ...]
  # zwraca: {etykieta: wartość, ...} lub {} gdy Esc
  master = tk.Tk()
  entries = {}
  for i, field in enumerate(fields):
    tk.Label(master, text=field).grid(row=i, sticky=tk.E, padx=3)
    ent = tk.Entry(master); ent.grid(row=i, column=1, padx=5, pady=5)
    if i==0: ent.focus_set()
    entries[field] = ent # ent.get() - wartość pola
  tk.Button(master, text='Esc', command=master.destroy).grid(row=len(fields), column=0, ipadx=5, pady=9)
  master.bind('<Escape>', lambda _: master.destroy())
  tk.Button(master, text='Ok', command=master.quit).grid(row=len(fields), column=1, ipadx=5, pady=9)
  master.bind('<Return>', lambda _: master.quit()) # [Enter] = [Ok]
    
  master.mainloop()
  try: # Po [Ok] weź wartości z formularza
    entries_di = {}
    for k,v in entries.items():
      entries_di[k] = v.get()
    master.destroy() # gdy już nie potrzebne
  except tk.TclError: # Anulowanie - po zamknięciu przez [x] albo [Esc]
    entries_di = {}
  return entries_di

if __name__ == '__main__':
  dane = tkForm( ('Imię', 'Imię 2', 'Nazwisko') )
  print(dane)

