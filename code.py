
#folder collecting
import reader
#from pathlib import Path, PurePath#os
import sys
import traceback
import isdir

folder = {}

"""
def open_folder_path(path: list):
    global folder
    out = folder
    for x in range(len(path)):
        out = out[path[x]]
    return out

def _add_to_folder(path: list):
    #global folder
    fold = open_folder_path(path)
    for x in range(len(path)):
        fold[x] = items[x]
    return fold
"""

def add_to_folder(path: list, item: str):
    global folder
    #print (item)
    #print (path, item)
    exec("folder"+get_folder_path(path)+f"['{item}'] = '{str(item)}'")#+str(_add_to_folder(path)))
    #print (folder)#print (path, item)

def add_folder_to_folder(path: list, item: str, item_name: str):
    global folder
    #print (path, item_name, item, folder)
    exec("folder"+get_folder_path(path)+f"['{item_name}'] = {str(item)}")
    #print (path, item_name, item)

def get_folder_path(path: list):
    out = ""
    for x in range(len(path)):
        out += "['"+path[x]+"']"
    return out

#def file_filter(st, *useless):
    #try:
    #    os.listdir(st)
    #    return False#st
    #except:
    #    #print (repr(st))
    #    return st#False
#    if Path(st).is_file():
#        return st
#    else:
#        return False

def create_list(li, re, filt):
    h=[]
    for filename in li:
        try:
            try:
                filt
            except NameError:
                print (str(filt)+' is not a function')
            if filt(filename, re)!=False:
                h.append(filename) #.split('.')[0]
        except:
            err=sys.exc_info()
            traceback.print_exception(*err)
            
    return h

global_path = ""

def check_folder(st, *useless):
    global global_path
    return isdir.check_if_folder(global_path+"\\"+st, st)

def search_folder(read_path: str, dict_path: list):
    #global folder
    #myfolder = open_folder_path(dict_path)
    global global_path
    filt = reader.reader.filter(read_path)
    files = reader.reader(read_path).read_all()
    global_path = read_path
    folders = reader.create_list(files, None, check_folder, True)#file_filter)#filt.file_filter()
    files = filt.invert(folders)
    files = reader.create_list(files, "bin", reader.end)
    for file in files:
        #myfolder[""]
        add_to_folder(dict_path, file)
    
    for fold in folders:
        d_path = dict_path
        add_folder_to_folder(d_path, "{}", str(fold))
        #print ("dict path before:", dict_path)
        p = dict_path
        p.append(str(fold))
        r_path = read_path
        #print ("dict path after:", dict_path)
        search_folder(r_path+"/"+str(fold), p)
        del dict_path[len(dict_path)-1]
        #print ("after: ", dict_path)


#dict parser
import file_parser
def parse(d):
    return file_parser.parse(d)

#starter
def main(path: str = ".", stdout = None):
    global folder
    search_folder(path, [])
    if stdout == None:
        print (parse(folder))
    else:
        with open(stdout, "wb") as file:
            file.write(parse(folder).encode("utf-8"))

#argument parser
import argh
argh.dispatch_command(main)