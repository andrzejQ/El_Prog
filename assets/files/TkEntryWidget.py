#!/usr/bin/python3 -i
# v.3.7+ order in dict()
import tkinter as tk
# based on https://python-course.eu/tkinter_entry_widgets.php
# https://www.pythontutorial.net/tkinter/tkinter-grid/

def tkForm(fields):
  """tkForm(fields: dict)->dict
  fields: {'label1': 'defVal1', ...}
  return: modified fields or {} if Esc
  >_> tkForm( {'Imię':'iii', 'Imię 2':'iii 2', 'Nazwisko':'Nnn'} )
  {'Imię': 'iii 1', 'Imię 2': 'iii 2', 'Nazwisko': 'nnn 3'}
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


def tkFormConf(fields, confCsv='conf_0.csv'):
  """tkFormConf(fields: dict, confCsv: str)->dict (saving data in Csv)
  fields: {'label1': 'defVal1', ...} - used if confCsv is missing (on start)
  confCsv - text file UTF-16 (=UCS-2) Little Endian with BOM with <tab> separator
  return: modified fields saved in confCsv or {} if Esc (confCsv remain unchanged)
  >>> with open('conf_0.csv', 'w', encoding='utf-16') as cnf: cnf.write('') # clean Csv for doctest
  0
  >>> tkFormConf( {'Imię':'iii 1', 'Imię 2':'iii 2', 'Nazwisko':'nnn 3'}, confCsv='conf_0.csv')
  {'Imię': 'iii 1', 'Imię 2': 'iii 2', 'Nazwisko': 'nnn 3'}
  """
  try: # ordered dict py 3.7+
    with open(confCsv, 'r', encoding='utf-16') as cnf:
      di = dict([row.split('\t') for row in cnf.read().splitlines()])
  except FileNotFoundError:
    di = {}
  if not di:
    di = fields
  di = tkForm( di ) # show and edit form
  if not di: # ie. [Esc]
    return {}
  else: #[Ok]
    with open(confCsv, 'w', newline='\r\n', encoding='utf-16') as cnf:
      cnf.write('\n'.join(['\t'.join(kv) for kv in di.items()]))
    return di

if __name__ == '__main__':
  # from TkEntryWidget import tkForm
  # di = tkForm( {'Imię':'Iii', 'Imię 2': 'iii 2', 'Nazwisko': 'Nnn'} )
  # print(di) # {'Imię': 'Iii', 'Imię 2': 'iii 2', 'Nazwisko': 'Nnn'}
  print("doctest: press ENTER")
  import doctest
  doctest.testmod()

