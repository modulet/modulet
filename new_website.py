#          ______          _      _____                  
#    ____ |___  /         | |    |  __ \                 
#   / __ \   / / __ _  ___| | __ | |__) |_ _  ___ ___    
#  / / _` | / / / _` |/ __| |/ / |  ___/ _` |/ __/ _ \   
# | | (_| |/ /_| (_| | (__|   <  | |  | (_| | (_|  __/   
#  \ \__,_/_____\__,_|\___|_|\_\ |_|   \__,_|\___\___|   
#   \____/   _       _       _       _       _       _   
#  _| |_   _| |_   _| |_   _| |_   _| |_   _| |_   _| |_ 
# |_   _| |_   _| |_   _| |_   _| |_   _| |_   _| |_   _|
#  _|_|__   |_|     |_|     |_|    _|_|     |_|     |_|  
# |  \/  |         | |     | |    | |                    
# | \  / | ___   __| |_   _| | ___| |_                   
# | |\/| |/ _ \ / _` | | | | |/ _ \ __|                  
# | |  | | (_) | (_| | |_| | |  __/ |_                   
# |_|_ |_|\___/ \__,_|\__,_|_|\___|\__|      _       _   
#  _| |_   _| |_   _| |_   _| |_   _| |_   _| |_   _| |_ 
# |_   _| |_   _| |_   _| |_   _| |_   _| |_   _| |_   _|
#  _|_|_    |_|     |_| _   |_|     |_|     |_|     |_|  
# |  __ \              | |                               
# | |__) |   _ ___  ___| |_ _   _ _ __                   
# |  ___/ | | / __|/ _ \ __| | | | '_ \                  
# | |   | |_| \__ \  __/ |_| |_| | |_) |                 
# |_|    \__, |___/\___|\__|\__,_| .__/                  
#         __/  |                  | |                     
#        |___/                   |_|                     
#
#
#
#   ZACK PACE @ sayRequil
#   - Release 1.0 Alpha -
#
#
import os
from data import *

cur_site = mod_data.cur_site
cur_page = mod_data.cur_page
cur_page_i = mod_data.cur_page_i

def new_website(path="/My_Website",name="My Website"):
  os.make_dirs(path)
  n = open(path . "/name.mod","w+")
  n.write(name)
  
def set_website(path="/My_Website"):
  cur_site = path
  
def get_website_path()
  return cur_site
  
def new_page(path="/My_Website",name="page" . cur_page+1):
  cur_page = cur_page+1
  newp = "/".join(path,name)
  p = open(newp . ".php","w+")
  p.close()
  cur_page_i = p.open(newp . ".php","a+")
  
def set_page()
