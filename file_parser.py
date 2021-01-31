parser_items = {
"root": ".",
"file_mid": "├── FILE",
"file_end": "└── FILE",
"indent": "│   ",
"empty_indent": "    ",
"newline": "\n"
}

def find_in_dict(d, f):
    count = 0
    for i in d:
        if i == f:
            return count, i
        count += 1
    return None

""" def make_indents(number, find_, len_):
    global parser_items
    op = ""
    for ind in range(number):
        if find_<len_:
            op += parser_items["empty_indent"]
        else:
            op += parser_items["indent"]
    return op """

def indentation(number_of_indents: int, ended_indents: dict):
    global parser_items
    ind = ""
    for i in range(number_of_indents):
        if ended_indents.get(i, True) == False:
            ind += parser_items["empty_indent"]
        else:
            ind += parser_items["indent"]
    return ind

def parse(d, indents = 0, ended_indents: dict = {}):
    global parser_items
    if indents == 0:
        output = parser_items["root"] + parser_items["newline"]
    else:
        output = parser_items["newline"]
    num = 0
    for file in d:
        f = find_in_dict(d, file)[0]
        le = len(d)-1
        if f<le:
            output += indentation(indents, ended_indents) + parser_items["file_mid"].replace("FILE", file) #parser_items["indent"]*indents
        else:
            output += indentation(indents, ended_indents) + parser_items["file_end"].replace("FILE", file) #parser_items["indent"]*indents
            ended_indents[indents] = False
            #print ("end of indent number", indents)
        if type(d[file]) == dict:
            if len(d[file]) != 0:
                ended_indents[indents + 1] = True
                output += parse(d[file], indents + 1)
        #if indents == 0:
        if num != le:
            output += parser_items["newline"]
        num += 1
    return output