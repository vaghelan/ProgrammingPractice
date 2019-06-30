import sys
import json
from string import printable
import re
#from langdetect import detect
import os

import fnmatch

#{ 'user' : { 'screen_name' : "xxxx", "id: : "xxx" } , "lang" : "xxx", "postedTime" : "zzz", "body" : "content...", "id" : n }
def cleanString(string):
    try:
        myString = string.replace('\n', ' ')
        myString = myString.replace('\r', ' ')
        myString = myString.replace('\t', ' ')
        return re.sub("[^{}]+".format(printable), "", myString).strip()
    except:
        return string


def remove_empty(tokens):
    r = []
    for t in tokens:
        if t.strip() != "":
            r.append(t.strip())
    return r

def stitch_me(tokens, num):

    r = []

    for t in tokens:

        r.append(t)

        if len(r) == num - 1:
            break

    copyFrom = num - 1
    s = ""
    for t in tokens[:copyFrom]:
        s = s + " " + t

    r.append(s)

    return r


files_path = sys.argv[1]
output_file = sys.argv[2]
max_output = int(sys.argv[3])

print max_output

op = open(output_file, "w")
#json_obj_list = []
lang_filter = [ 'en-gb', 'pt', 'es', 'en' ]


from dateutil.parser import parse


def is_number(s):
    try:
        s = long(s)
    except ValueError:
        return False

    return True


def validate(tokens):

    if tokens[0][0] != "@":
        print("@ is missing in token 0 \n")
        return False

    if not is_number(tokens[1]):
        print("userid not a number " + tokens[1] + "\n")
        return False

    #if is_number(tokens[2]):
    #    print("screen name is numeric " + tokens[2] + "\n")
    #    return False

    #if is_number(tokens[3]):
    #    print("user_name is numeric " + tokens[3] + "\n")
    #    return False

    #if not is_number(tokens[4]):
    #    print("retweets is not numeric " + tokens[4] + "\n")
    #    return False

    #if not is_number(tokens[5]):
    #    print("favorites is not numeric " + tokens[5] + "\n")
    #    return False

    if not is_number(tokens[6]):
        print("tweet id is not numeric " + tokens[6] + "\n")
        return False

    try:
        parse(tokens[7])
    except ValueError:
        print("Date is not date " + tokens[7] + "\n")
        return False
    except OverflowError:
        print("Date overflow error " + tokens[7] + "\n")
        return False

    #if is_number(tokens[8]):
    #    print("text is not string " + tokens[8] + "\n")
    #    return False

    return True


def finish():
    log = "INFO : Total lines processed : " + str(total_lines) + "\n"
    print log

    op.close()


total_lines = 0
total_lines_processed = 0
for root, dirnames, filenames in os.walk(files_path):
    for filename in fnmatch.filter(filenames, '*.csv'):

            print "Processing : " + os.path.join(root, filename)

            fp = open(os.path.join(root, filename), "r")


            for line in fp:

                total_lines = total_lines + 1

                tokens = line.strip().split("\t")

                if len(tokens) > 9:
                    tokens = stitch_me(tokens, 9)
                    if len(tokens) == 9:
                       print("Success : Stiched Data Error : num tokens " + str(len(tokens)))
                elif len(tokens) < 9:
                    print("Data Format Error : < 9 " + str(len(tokens)) + "  skipping ..." + line)
                    continue

                if validate(tokens) == False:
                    print("Data Validation Error : skipping ..." + line)
                    continue

                try:
                    us = unicode(cleanString(tokens[8]), "utf-8")
                    if tokens[0][1:].lower() != tokens[2].lower():
                        continue
                    total_lines_processed =  total_lines_processed  + 1
                    if max_output != 0 and total_lines_processed > max_output:
                        finish()
                        sys.exit(1)

                    json_obj = {}
                    json_obj['user'] = {}
                    json_obj['user']['id'] = tokens[1]
                    json_obj['user']['screen_name'] = tokens[2]
                    json_obj['lang'] = 'es'
                    json_obj['postedTime'] = tokens[7]
                    json_obj['body'] = us
                    json_obj['id'] = long(tokens[6])
                    op.write(json.dumps(json_obj, ensure_ascii=False) + "\n")
                    op.flush()
                    #found = True
                    #json_obj_list.append(json_obj)
                except Exception as e:
                    print(e.message + " : Data Error : num tokens " + str(len(tokens)) + "  " + line)


log = "INFO : Total lines processed : " + str(total_lines) + "\n"
print log

op.close()
