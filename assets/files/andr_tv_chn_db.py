import json 
import csv
from collections import namedtuple
''''
Po wyszukaniu kanałów w programie LiveTV - Android TV
powstaje plik "\backup_user_databases\TvProviderChannels\tv_provider_db.json",
z aktualną informacją o dostępnych kanałach DVB-T/T2 - wynik w "andrTVchInfo.csv"
- tj. płaski JSON z rozbudowaną wartością "internal_provider_data", jako 
literał (str) słownika "custom"
'''
andrTVchInfo = 'andrTVchInfo.csv'
with open(r'tv_provider_db.json ', 'r', encoding='utf-8') as fj:
  d = json.load(fj) 

def cTV (MHz_): 
  '''cTV(474) -> "C21"; cTV(177.5) -> "E5"'''
  try: MHz = float(MHz_ or 0)
  except ValueError: MHz = 0.0
  Band = namedtuple("Band", 'CSE Nr F0 dF')
  bands = (          Band( 'C',21,470.0,8.0 ),
                     Band( 'S', 9,230.0,8.0 ),
                     Band( 'E', 5,174.0,7.0 ),
                     Band( 'S', 1,110.0,8.0 )
  )
  for b in bands:
    if MHz > b.F0 : break
  else: return '?'
  return b.CSE+str(int( b.Nr + (MHz-b.F0)/b.dF ))
  
header = dict.fromkeys([])
custom = dict.fromkeys([])
chnInfo = []
for k in d:
  # dodaj potencjalne inne klucze w dalszych paczkach kanałów zachowując kolejność
  internal_data_str = k.pop("internal_provider_data",'') # tu jest słownik jako str
  internal_data = json.loads(internal_data_str)
  c = internal_data.get('custom',{}) #$# ;print((f'{c=}'));break
  
  header = dict.fromkeys(list(header) + list(k.keys()), '')
  custom = dict.fromkeys(list(custom) + list(c.keys()))
  chnInfo += [{'nr':1+k.get("internal_provider_flag4",-1), 'C':cTV(int(c.get("frequency",'0'))/1000000.0), **k, **c }] #$# ;break ;print(f'{chnInfo=}')

header =  dict.fromkeys(['nr','C'] + list(header) + ["internal_prov_data"] + list(custom), '') #"internal_prov_data" - pusta = separator

print(f'{header=}\n')
  

print(len(d),'kanałów - zob.',andrTVchInfo)

with open('FULL_'+andrTVchInfo,'w',newline='',encoding='utf-8-sig') as csvF:
  csvWr = csv.DictWriter(csvF, header, delimiter=';',quoting=csv.QUOTE_MINIMAL)
  csvWr.writeheader()
  csvWr.writerows(chnInfo)


# Bardziej istotne (pominięte ulubione)
#['package_name','input_id','browsable','searchable','locked','internal_provider_flag2','internal_prov_data','fav_groups','hidden','selectable','sched_disabled','now_next_disabled','lcn_editable','deleted','without_sdt','freesat_id','region_id','scrambled','favorite_id','is_data','set_displayname','set_displaynumber','set_favourite','is_favourite','favourite_info','set_hidden']

header2 = \
['nr', 'C','display_name','transponder_info','video_format','provider_name','internal_provider_flag3','display_number','type','service_type','original_network_id','transport_stream_id','service_id','dvbUri','video_pid','audio_pid','pcr_pid','video_type','video_code','audio_type','audio_code','audio_mode','pmt_pid','network_id'] #,'internal_provider_flag4','frequency'  

chnInfo2 = sorted(chnInfo, key=lambda d: d['nr']) 

with open(andrTVchInfo,'w',newline='',encoding='utf-8-sig') as csvF:
  csvWr = csv.DictWriter(csvF, header2, delimiter=';',quoting=csv.QUOTE_MINIMAL, extrasaction='ignore')
  csvWr.writeheader()
  csvWr.writerows(chnInfo2)

