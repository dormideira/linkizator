# Converts user input link and text into HTML <a> tag hyperlink. 
# Link and text can be more than 1 if they're separated by new lines or commas. 
# They can also be 1 or 2 .csv files or 2 .txt files that can be accessed from your directory. 
# It also trims leading and trailing white spaces, as well as bullet points such as "-" and "*". 
# Output can be exported as a .txt file or just printed in the command line. 
# Manual tests are commented below their respective functions. 
import csv

# Turns 1 link and 1 text into <a> tag hyperlink. 
# Adds 'http' to the beginning of each link if there isn't any. 
def linker(link, text):
    if "http" not in link:
        link = "https://" + link
    return ("<a href='{0}'>{1}</a>".format(link, text))

# Determine if link is a list 
# 1. By type
# 1. If there's a new line
# 1. If there's more than 1 comma
def is_listable(list_suspect): 
    return(type(list_suspect) == list or type(list_suspect) == dict or type(list_suspect) == tuple or "\n" in list_suspect or list_suspect.count(",") > 1)
## Tests is_listable: 
# if is_listable(sample_list):
#     print("is_listable(sample_list) test ok.")
# else: print("Something wrong with is_listable(sample_list) test.")
# if is_listable(sample_dict):
#     print("is_listable(sample_dict) test ok.")
# else: print("Something wrong with is_listable(sample_dict) test.")
# if is_listable(sample_tuple):
#     print("is_listable(sample_tuple) test ok.")
# else: print("Something wrong with is_listable(sample_tuple) test.")
# if is_listable(sample_links):
#     print("is_listable(sample_links) test ok.")
# else: print("Something wrong with is_listable(sample_links) test.")
# if is_listable(sample_links):
#     print("is_listable(sample_texts) test ok.")
# else: print("Something wrong with is_listable(sample_texts) test.")
## End of is_listable tests

# Takes a string that looks like a list (new lines etc., see is_listable function def) \
# and turns it into a Python list. 
def listify(stringy_list):
    if is_listable(stringy_list):
        if type(stringy_list) == str: 
            if stringy_list.count(",") > 1 and "\n" not in stringy_list:
                csv_list = stringy_list.split(sep=",")
                trimmed_csv_list = []
                for csv_list_item in csv_list:
                    trimmed_csv_list.append(csv_list_item.strip())
                return trimmed_csv_list
            else: 
                # Trims item identifiers: new line + dash, new line + period, new line + asterisk: 
                item_identifiers = [
                    "\n-", "\n*", "\n."
                ]
                for item_identifier in item_identifiers:
                    while item_identifier in stringy_list:
                        stringy_list = stringy_list.replace(item_identifier, "\n")
                # Identifies separator and splits upon it: new line, comma + new line, \
                # semicolon + new line, comma + space + new line, semicolon + space + new line:
                separators = [
                    ",\n", ";\n", ", \n", "; \n", "\n"
                ]
                for separator in separators: 
                    while separator in stringy_list: 
                        stringy_list = stringy_list.split(sep=separator)
                if type(stringy_list) == list:
                    split_list = stringy_list
                else: 
                    print("Listification failed, sorry. ")
                # Trims item identifiers in 1st item: 
                item_identifiers_without_n = [
                    "-", "*", "."
                ]
                split_list_first_item = split_list[0]
                for item_identifier_without_n in item_identifiers_without_n:
                    while item_identifier_without_n in split_list_first_item[0]:
                        split_list[0] = split_list_first_item[1:]
                # Trims leading or trailing whitespaces: 
                trimmed_list = []
                for split_list_item in split_list:
                    trimmed_list_item = split_list_item.strip()
                    trimmed_list.append(trimmed_list_item)
                return trimmed_list
        elif type(stringy_list) == list:
            return stringy_list
        elif type(stringy_list) == tuple: 
            return list(stringy_list)
        elif type(stringy_list) == dict: 
            list_from_dict = list(stringy_list.values())
            return list_from_dict
    else: 
        print("Listification not recommended, please review your input.")
        return
## Tests listify: 
# sample_list = ["a", "b", "c"]
# if listify(sample_list) == ["a", "b", "c"]:
#     print("sample_list OK")
# else: 
#     print("sample_list failed")
# sample_dict = {1: "a", 2: "b", 3: "c"}
# if listify(sample_dict) == ["a", "b", "c"]:
#     print("sample_dict OK")
# else: 
#     print("sample_dict failed")
# if listify(sample_dict) == ["a", "b", "c"]:
#     print("sample_dict OK")
# else: 
#     print("sample_dict failed")
# sample_tuple = ("a", "b", "c")
# if listify(sample_tuple) == ["a", "b", "c"]:
#     print("sample_tuple OK")
# else: 
#     print("sample_tuple failed")
# sample_CSV_list = "a, b, c"
# if listify(sample_CSV_list) == ["a", "b", "c"]:
#     print("sample_CSV_list OK")
# else: 
#     print("sample_CSV_list failed")
# sample_not_list = "a; b; c"
# if listify(sample_not_list) != ["a", "b", "c"]:
#     print("sample_not_list OK")
# sample_stringy_list_comma_n = """a,
# b,
# c"""
# if listify(sample_stringy_list_comma_n) == ["a", "b", "c"]:
#     print("sample_stringy_list_comma_n OK")
# else: 
#     print("sample_stringy_list_comma_n failed")
# sample_stringy_list_semicolon_n = """a;
# b;
# c"""
# if listify(sample_stringy_list_semicolon_n) == ["a", "b", "c"]:
#     print("sample_stringy_list_semicolon_n OK")
# else: 
#     print("sample_stringy_list_semicolon_n failed")
# sample_stringy_list_comma_ws_n = """a, 
# b, 
# c"""
# if listify(sample_stringy_list_comma_ws_n) == ["a", "b", "c"]:
#     print("sample_stringy_list_comma_ws_n OK")
# else: 
#     print("sample_stringy_list_comma_ws_n failed")
# sample_stringy_list_semicolon_ws_n = """a; 
# b; 
# c"""
# if listify(sample_stringy_list_semicolon_ws_n) == ["a", "b", "c"]:
#     print("sample_stringy_list_semicolon_ws_n OK")
# else: 
#     print("sample_stringy_list_semicolon_ws_n failed")
# sample_stringy_list_n = """a
# b
# c"""
# if listify(sample_stringy_list_n) == ["a", "b", "c"]:
#     print("sample_stringy_list_n OK")
# else: 
#     print("sample_stringy_list_n failed")
# sample_stringy_list_comma_n_item_id = """- a,
# * b,
# . c"""
# if listify(sample_stringy_list_comma_n_item_id) == ["a", "b", "c"]:
#     print("sample_stringy_list_comma_n_item_id OK")
# else: 
#     print("sample_stringy_list_comma_n_item_id failed")
# sample_stringy_list_semicolon_n_item_id = """- a;
# * b;
# . c"""
# if listify(sample_stringy_list_semicolon_n_item_id) == ["a", "b", "c"]:
#     print("sample_stringy_list_semicolon_n_item_id OK")
# else: 
#     print("sample_stringy_list_semicolon_n_item_id failed")
# sample_stringy_list_comma_ws_n_item_id = """- a, 
# * b, 
# . c"""
# if listify(sample_stringy_list_comma_ws_n_item_id) == ["a", "b", "c"]:
#     print("sample_stringy_list_comma_ws_n_item_id OK")
# else: 
#     print("sample_stringy_list_comma_ws_n_item_id failed")
# sample_stringy_list_semicolon_ws_n_item_id = """- a; 
# * b; 
# . c"""
# if listify(sample_stringy_list_semicolon_ws_n_item_id) == ["a", "b", "c"]:
#     print("sample_stringy_list_semicolon_ws_n_item_id OK")
# else: 
#     print("sample_stringy_list_semicolon_ws_n_item_id failed")
# sample_stringy_list_n_item_id = """- a
# * b
# . c"""
# if listify(sample_stringy_list_n_item_id) == ["a", "b", "c"]:
#     print("sample_stringy_list_n_item_id OK")
# else: 
#     print("sample_stringy_list_n_item_id failed")
## END OF LISTIFY TESTS HURRAY

## AND NOW FOR SOMETHING COMPLETELY DIFFERENT

# Asks user for link and text:
print("Enter a link or links file name with extension. \
* Files must be in the current directory, but you can enter paths with backslashes.")
link = input()

# Is link a file that can be read? If yes, makes it a list: 
if link.lower()[-4:] == ".txt":
    with open(link) as link_file:
        link = link_file.read()
elif link.lower()[-4:] == ".csv":
    with open(link) as link_file:
        link_csv = list(csv.reader(link_file))
        link = []
        # If the .csv only has 1 column, list it: 
        if len(link_csv[0]) == 1: 
            for row in link_csv: 
                link.append(row[0])
        else: 
            # Otherwise, asks which column should be read: 
            print("Link .csv file contains more than 1 column. \
Enter the number of the column you need. (e.g.: 1 would be the 1st column).")
            column = int(input()) - 1
            for row in link_csv: 
                link.append(row[column])
else: 
    # Not a file that can be read. 
    print("Unable to read link file. Make sure that the file format is .txt or .csv.")
    exit()

print("Now enter a text or texts file name with extension. \
* Files must be in the current directory, but you can enter paths with backslashes.")
text = input()

# Is text a file that can be read? If yes, open it. 
if text.lower()[-4:] == ".txt":
    with open(text) as text_file:
        text = text_file.read()
elif text.lower()[-4:] == ".csv":
    with open(text) as text_file:
        text_csv = list(csv.reader(text_file))
        text = []
        # If the .csv only has 1 column, list it: 
        if len(text_csv[0]) == 1: 
            for row in text_csv: 
                text.append(row[0])
        else: 
            # Otherwise, asks which column should be read: 
            print("text .csv file contains more than 1 column. \
Enter the number of the column you need. (e.g.: 1 would be the 1st column).")
            column = int(input()) - 1
            for row in text_csv: 
                text.append(row[column])
else: 
    # Not a file that can be read. 
    print("Unable to read text file. Make sure that the file format is .txt or .csv.")
    exit()

# Checks for unfortunate events: 
if is_listable(link) or is_listable(text): 
    if not is_listable(link) and is_listable(text):
        print("Uh oh! It looks like you have more than one text but only one link. \
Enter 'ok' if you just happen have more than 1 comma in your text \
and we'll get on with it (or don't and check your link).")
        user_ok = input()
        if user_ok.lower() == "ok" :
            print(linker(link, text))
        else: 
            exit()
    elif is_listable(link) and not is_listable(text): 
        print("Uh oh! It looks like you have more than one link but only one text. Please check your input.")
        exit()
    elif is_listable(link) and is_listable(text):
        link = listify(link)
        text = listify(text)
        if len(link) != len(text):
            print("Uh oh! The amount of links and texts don't match. Please check your input.")
            exit()
        else: 
            # FINALLY the happy path
            # Asks if links are URLs that need to be concatenated: 
            print("Do you need to add something before or after your links to make them valid URLs, \
like www.something.com/{{link}}.php?")
            invalid_URLs = input()
            if "y" in invalid_URLs:
                print("What do you need before your links? Just hit enter if it's nothing. ")
                before_link = input()
                print("What do you need after your links? Just hit enter if it's nothing. ")
                after_link = input()
                for index in range(len(link)):
                    link[index] = before_link + link[index] + after_link
            else: 
                print("Okie dokie. ")
            linked_links = "\n"
            for links, texts in zip(link, text):
                linked_links = linked_links + linker(links, texts) + "\n"
            # Asks if file output or just plain print: 
            print("Would you like that to go? (Into a .txt file to current directory for your convenience etc.)")
            to_go = input()
            if "y" in to_go.lower():
                takeout_links = open("Links for take-out.txt", "w")
                takeout_links.write(linked_links)
                takeout_links.close()
            else: 
                print(linked_links)
    else: 
        print("Something unspeakable happened while trying to combine links and texts. \
Please consult with your nearest metaphysical or spiritual guide. ")
        exit()
else: 
    # Just spits the goddamn HTML: 
    print(linker(link, text))

print("Thanks for flying with us.")
