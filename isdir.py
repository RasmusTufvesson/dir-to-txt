import subprocess as sp

def get_dir_out(dire):
    out = ""
    backslash = "\\"
    process = sp.Popen(f'dir /ad /b "{str(dire)}" 1>nul 2>nul && (echo is a folder) || (echo is not a folder)', stdout=sp.PIPE, shell=True)#.replace(backslash, "/")
    searching = True
    while searching:
        o = process.stdout.readline()
        if o == b'':
            searching = False
            break
        else:
            out += o.decode("utf-8")
    return out

def check_if_folder(path, iftrue = True):
    out = get_dir_out(path)
    #print (path)
    #print (repr(out))
    #print (out == "is a folder\r\n")
    if out == "is a folder\r\n":
        return iftrue
    else:
        return False