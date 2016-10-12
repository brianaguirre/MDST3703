__author__ = 'BrianAguirre'

import requests
import os, struct
import wget
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import MD5

def prettyHTML(str):
    counter = 0
    s = str.decode("utf-8")
    return s

def findReports(string):
    report_list = dict()
    report_name = ""
    report_num = ""
    counter = 0
    for i in range(0, len(string)):
        if (string[i] == '4' and string[i-1] == 'h' and string[i-2] == '<' and string[i+2] != '<'):
            index_report = i+2
            current_letter = string[index_report]

            #REVERSE NUMBER: 'hello world'[::-1]
            while (current_letter != '<'):
                report_name += string[index_report]
                index_report += 1
                current_letter = string[index_report]

            index_num = index_report+80
            current_num = string[index_num]
            while(current_num != '/'):
                report_num += string[index_num]
                index_num += 1
                current_num = string[index_num]

            i = index_report

            #FOLDERS: NOT NEEDED:
            """if (report_name[0] == ' '):
                folder = "*FOLDER* "+report_name
                report_list.(folder)
            else:
                report_list.append(report_name)"""

            report_list[report_name] = report_num
            report_name = ""
            report_num = ""
    return report_list


def findFiles(string):
    file_list = dict()
    file_name = ""
    username_files = ""

    for i in range(0, len(string)):
        if (string[i] == 'm' and string[i+1] == 'e' and string[i+2] == 'd' and string[i+3] == 'i' and string[i+4] == 'a'):
            slash_count = 0
            index_file_start = i+5
            current_letter = string[index_file_start]
            current_letter_user = ""
            username_start = 0
            username_end = 0
            while(slash_count<2):
                if (current_letter == '/'):
                    slash_count+=1
                    index_file_start += 1
                    current_letter = string[index_file_start]
                    while(current_letter != '/' and slash_count!= 2):
                        username_start = index_file_start
                        username_end = username_start
                        current_letter_user = string[username_end]
                        username_files += current_letter_user


                        username_end += 1
                        current_letter_user = string[username_end]


                        index_file_start = username_end
                        current_letter = string[index_file_start]
                else:
                    index_file_start+=1
                    current_letter = string[index_file_start]
            i = index_file_start
            index_file_end = index_file_start
            current_letter = string[index_file_start]
            while (current_letter != '"'):
                index_file_end += 1
                current_letter = string[index_file_end]

            file_name = string[index_file_start:index_file_end]
            file_list[file_name] = username_files

            file_name = ""
            username_files = ""
    return file_list


def combineDict(dict1, dict2):
    dict_total = dict()
    for i in range (0, len(list(dict1.keys()))):
        dict_total[list(dict1.keys())[i]] = dict1[list(dict1.keys())[i]]
    for i in range (0, len(list(dict2.keys()))):
        dict_total[list(dict2.keys())[i]] = dict2[list(dict2.keys())[i]]

    return dict_total


def private_Rep(string):
    report_list = dict()
    report_name = ""
    report_num = ""
    counter = 0
    for i in range(0, len(string)):
        if (string[i] == '4' and string[i-1] == 'h' and string[i-2] == '<' and string[i+2] != '<'):
            index_report = i+2
            current_letter = string[index_report]

            #REVERSE NUMBER: 'hello world'[::-1]
            while (current_letter != '<' and current_letter != '/'):
                report_name += string[index_report]
                index_report += 1
                current_letter = string[index_report]

            index_num = index_report+76
            current_num = string[index_num]
            while(current_num != '/' and current_num != '<'):
                report_num += string[index_num]
                index_num += 1
                current_num = string[index_num]

            i = index_report

            #FOLDERS: NOT NEEDED:
            """if (report_name[0] == ' '):
                folder = "*FOLDER* "+report_name
                report_list.(folder)
            else:
                report_list.append(report_name)"""

            report_list[report_name] = report_num
            report_name = ""
            report_num = ""
    return report_list


def decrypt_file(key, in_filename, chunksize=1024):

    out_filename = os.path.splitext(in_filename)[0]

    if len(key) < 16:
        key += ' ' * 8
    if len(key) % 8 != 0:
        key += ' ' * (8 - len(key) % 8)

    # Decrypt the file chunk by chunk
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)


"""------------------------------------------------------------------------------

                           FILE DOWNLOAD APPLICATION

   ------------------------------------------------------------------------------"""

#ADD QUIT OPTION:
#ADD GO BACK TO MAIN REPORT MENU:

    #LOGIN SUCCESSFUL:
print("Welcome to SECURE SHARE: FILE DOWNLOAD APPLICATION.")
print("This application (FDA) allows you to download the files attached to your reports under SECURE SHARE.")
print("Enter your USERNAME: ")
USERNAME = input()
print("Enter your PASSWORD:")
PASSWORD = input()
with requests.Session() as c:
    #WEBSITE AUTHENTICATION:
    url = 'https://gentle-springs-7311.herokuapp.com/secureshare/login/?next=/'
    c.get(url)
    csrftoken = c.cookies['csrftoken']
    login_data = dict(csrfmiddlewaretoken=csrftoken, username=USERNAME, password=PASSWORD)
    login_page = c.get('https://gentle-springs-7311.herokuapp.com/secureshare/#') #IN CASE IT FAILS TO LOGIN:

    c.post(url, data=login_data, headers = {"Referer": "https://gentle-springs-7311.herokuapp.com/secureshare/"})
    page = c.get('https://gentle-springs-7311.herokuapp.com/secureshare/')
    print()
    print()



    if(login_page.content == page.content):
        print("ERROR: Failed to login to SECURE SHARE.")
        print("Make sure your USERNAME and PASSWORD are correct.")
        print("This program will now terminate. Try again by running FDA.")
        print("Goodbye :)")
        quit()
    else:
        print("SUCCESS! You are now logged into SECURE SHARE as '" + USERNAME +"'")

        while(True):
            #REPORTS
            print("To QUIT this program, simply type in 'EXIT' whenever you are prompted for input.")
            print("Reports Under " + USERNAME +":")


            empty_reports = []
            reports = dict()
            public_rep = findReports(prettyHTML(page.content))

            temp_reports = dict()


            #TEST
            account_page = c.get('https://gentle-springs-7311.herokuapp.com/secureshare/user/'+ USERNAME + '/')
            priv_rep = private_Rep(prettyHTML(account_page.content))

            reports = combineDict(public_rep, priv_rep)


            for i in range(1, len(list(reports.keys()))+1):
                temp_reports[str(i)] = list(reports.keys())[i-1]
                print(str(i) + ". "+ list(reports.keys())[i-1])

            print()
            print()



            #SELECT A REPORT:
            print("Please enter a number for the report you wish you access: ")
            report_num = input()

            if str(report_num).upper() == "EXIT":
                print("You have been logged out of SECURE SHARE.")
                print("Goodbye :)")
                quit()

            else:
                report_page = c.get('https://gentle-springs-7311.herokuapp.com/secureshare/report/' + reports[temp_reports[report_num]] + '/')

                print()
                print("The files under report " + temp_reports[report_num] + " are: ")
                files = findFiles(prettyHTML(report_page.content))
                for i in range (1, len(list(files.keys()))+1):
                    print("" + str(i) + ". " + list(files.keys())[i-1])

                print()



                #SELECT A FILE TO DOWNLOAD:
                print("Enter the number for the file you wish to download:")
                file_num = input()
                if str(file_num).upper() == "EXIT":
                    print("You have been logged out of SECURE SHARE.")
                    print("Goodbye :)")
                    quit()

                else:
                    file_num = int(file_num)
                    if (file_num == {}):
                        print ("There are no files under this report.")
                    else:
                        print(files[list(files.keys())[file_num-1]])
                    print()
                    print()
                    print(list(files.keys())[file_num-1])
                    file_url = "https://gentle-springs-7311.herokuapp.com/media/"+ files[list(files.keys())[file_num-1]] +"/" + list(files.keys())[file_num-1]
                    print(file_url)
                    print()
                    print()

                    filename = wget.download(file_url)

                    #DECRYPT:
                    print("Your file encrypted file: " + list(files.keys())[file_num-1] + " has downloaded.")
                    print("To decrypt it, please enter the key used when it was uploaded.")
                    key = input()

                    if str(key).upper() == "EXIT":
                        print("You have been logged out of SECURE SHARE.")
                        print("Goodbye :)")
                        quit()

                    else:
                        decrypt_file(key, list(files.keys())[file_num-1], chunksize=1024)
                        print("Your file: " + list(files.keys())[file_num-1] +"has been decrypted.")
                        print("It is currently in the same folder as this FDA application under the name: " + list(files.keys())[file_num-1][0:len(list(files.keys())[file_num-1])-4])
                        print()
                        print()