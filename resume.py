import sys
import json
import os
import datetime


template_py = '''
# Schema of Resume
# Press "i" to edit (VIM)

import datetime

class Basic:
    data = {
        "first_name": "",
        "last_name": "",
        "position": "",
        "email": "",
        "phone": "",
        "url": "",
        "summary": "",
        "location": {
            "address": "",
            "postalCode": "",
            "city": "",
            "countryCode": "",
            "region": "",
        }
    }

class Work:
    data = [
        {
            "company_name": "",
            "position": "",
            "url": "",
            "start_date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "end_date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "summary": "",
        },
        # Add more if you need
    ]

class Education:
    data = [
        {
            "institute": "",
            "url": "",
            "area": "",
            "degree": "",
            "start_date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "end_date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "gpa": 4.0, # Ctrl-A, Ctrl-Z to alter numbers
            "full_gpa": 4.0, # Ctrl-A, Ctrl-Z to alter numbers
            "summary": "",
        },
        # Add more if you need
    ]

class Project:
    data = [
        {
            "name": "",
            "description": "",
            "highlights": "",
            "domain": "",
            "date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "url": "",
            "roles": "", # seperated by ,
        },
        # Add more if you need
    ]

class Awards:
    data = [
        {
            "title": "",
            "date": "",
            "awarder": "",
            "summary": "",
        },
        # Add more if you need
    ]

class Publication:
    data = [
        {
            "name": "",
            "publisher": "",
            "releaseDate": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "url": "",
            "summary": ""
        },
        # Add more if you need
    ],

class Skills:
    data = {
        "domain": "", # Seperated by ,
        "master": "", # Seperated by ,
        "know": "", # Seperated by ,
    }

class Language:
    data = {
        "speaking": "", # Seperated by ,
        "reading": "", # Seperated by ,
    }

class Interests:
    data = [
        {
            "name": "",
            "keywords": "", # Seperated by ,
        },
        # Add more if you need
    ]

class References:
    data = [
        {
            "name": "",
            "reference": "",
            "contact no.": "",
        }
    ]


# press <Shift - Z> twice to save changes
'''

class Basic:
    data = {
        "first_name": "",
        "last_name": "",
        "position": "",
        "email": "",
        "phone": "",
        "url": "",
        "summary": "",
        "location": {
            "address": "",
            "postalCode": "",
            "city": "",
            "countryCode": "",
            "region": "",
        }
    }

class Work:
    data = [
        {
            "company_name": "",
            "position": "",
            "url": "",
            "start_date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "end_date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "summary": "",
        },
        # Add more if you need
    ]

class Education:
    data = [
        {
            "institute": "",
            "url": "",
            "area": "",
            "degree": "",
            "start_date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "end_date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "gpa": 4.0, # Ctrl-A, Ctrl-Z to alter numbers
            "full_gpa": 4.0, # Ctrl-A, Ctrl-Z to alter numbers
            "summary": "",
        },
        # Add more if you need
    ]

class Project:
    data = [
        {
            "name": "",
            "description": "",
            "highlights": "",
            "domain": "",
            "date": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "url": "",
            "roles": "", # seperated by ,
        },
        # Add more if you need
    ]

class Awards:
    data = [
        {
            "title": "",
            "date": "",
            "awarder": "",
            "summary": "",
        },
        # Add more if you need
    ]

class Publication:
    data = [
        {
            "name": "",
            "publisher": "",
            "releaseDate": str(datetime.date(2021, 1, 1)), # Ctrl-A, Ctrl-Z to alter numbers
            "url": "",
            "summary": ""
        },
        # Add more if you need
    ],

class Skills:
    data = {
        "domain": "", # Seperated by ,
        "master": "", # Seperated by ,
        "know": "", # Seperated by ,
    }

class Language:
    data = {
        "speaking": "", # Seperated by ,
        "reading": "", # Seperated by ,
    }

class Interests:
    data = [
        {
            "name": "",
            "keywords": "", # Seperated by ,
        },
        # Add more if you need
    ]

class References:
    data = [
        {
            "name": "",
            "reference": "",
            "contact no.": "",
        }
    ]


def fillin_guide():
    instr = "=== Resume Maker ===\nYou will need to answer the following questions.\nType '/b' to redo the last question\n"
    print(instr + "=== Basic ===")
    i = 0
    while i < len(Basic.data):
        query = "Your %s? > "
        entry = list(Basic.data)[i]
        if type(Basic.data[entry]) == dict:
            j = 0
            while j < len(Basic.data[entry]):
                inner_entry = list(Basic.data[entry])[j]
                query = "%s %s? > "
                answer = input(query % (entry, inner_entry))
                if answer == '/b':
                    j -= 1
                    continue
                Basic.data[entry][inner_entry] = answer
                j += 1
        else:
            answer = input(query % entry)
            if answer == '/b': 
                i -= 1
                continue
            Basic.data[entry] = answer
        i += 1

    print("=== Work ===")
    create_work = input("Add a work experience? [Y/n] > ")
    if create_work.lower() == 'y':
        i = 0; j = 0; work = 0
        while work < j + 1:
            while i < len(Work.data[j]):
                query = "Work %s? > "
                each_entry = list(Work.data[j])[i]
                answer = input(query % each_entry) 
                if answer == '/b':
                    i -= 1
                    continue
                Work.data[j][each_entry] = answer
                i += 1
            work += 1
            answer = input("Add another? [Y/n] > ")
            if answer.lower() == 'y': 
                i = 0
                Work.data.append({})
                for key in Work.data[0].keys():
                    Work.data[j + 1][key] = ""
                j += 1


    print("=== Education ===")
    create_edu = input("Add a education experience? [Y/n] > ")
    if create_edu.lower() == 'y':
        i = 0; j = 0; edu = 0
        while edu < j + 1:
            while i < len(Education.data[j]):
                query = "Education %s? > "
                each_entry = list(Education.data[j])[i]
                answer = input(query % each_entry) 
                if answer == '/b':
                    i -= 1
                    continue
                Education.data[j][each_entry] = answer
                i += 1
            edu += 1
            answer = input("Add another? [Y/n] > ")
            if answer.lower() == 'y': 
                i = 0
                Education.data.append({})
                for key in Education.data[0].keys():
                    Education.data[j + 1][key] = ""
                j += 1


    print("=== Project ===")
    create_project = input("Add a project experience? [Y/n] > ")
    if create_project.lower() == 'y':
        i = 0; j = 0; project = 0
        while project < j + 1:
            while i < len(Project.data[j]):
                query = "Project %s? > "
                each_entry = list(Project.data[j])[i]
                answer = input(query % each_entry) 
                if answer == '/b':
                    i -= 1
                    continue
                Project.data[j][each_entry] = answer
                i += 1
            project += 1
            answer = input("Add another? [Y/n] > ")
            if answer.lower() == 'y': 
                i = 0
                Project.data.append({})
                for key in Project.data[0].keys():
                    Project.data[j + 1][key] = ""
                j += 1


    print("=== Awards ===")
    create_award = input("Add an award? [Y/n] > ")
    if create_award.lower() == 'y':
        i = 0; j = 0; awards = 0
        while awards < j + 1:
            while i < len(Awards.data[j]):
                query = "Award %s? > "
                each_entry = list(Awards.data[j])[i]
                answer = input(query % each_entry) 
                if answer == '/b':
                    i -= 1
                    continue
                Awards.data[j][each_entry] = answer
                i += 1
            awards += 1
            answer = input("Add another? [Y/n] > ")
            if answer.lower() == 'y': 
                i = 0
                Awards.data.append({})
                for key in Awards.data[0].keys():
                    Awards.data[j + 1][key] = ""
                j += 1


    print("=== Publication ===")
    create_pub= input("Add a publication? [Y/n] > ")
    if create_pub.lower() == 'y':
        i = 0; j = 0; pub = 0
        while pub < j + 1:
            while i < len(Publication.data[j]):
                query = "Publication %s? > "
                each_entry = list(Publication.data[j])[i]
                answer = input(query % each_entry) 
                if answer == '/b':
                    i -= 1
                    continue
                Publication.data[j][each_entry] = answer
                i += 1
            pub += 1
            answer = input("Add another? [Y/n] > ")
            if answer.lower() == 'y': 
                i = 0
                Publication.data.append({})
                for key in Publication.data[0].keys():
                    Publication.data[j + 1][key] = ""
                j += 1

    
    print("=== Skills ===")

    i = 0
    while i < len(Skills.data):
        query = "All %s skills (Seperated by ',')? > "
        entry = list(Skills.data)[i]
        answer = input(query % entry)
        if answer == '/b': 
            i -= 1
            continue
        Skills.data[entry] = answer
        i += 1

    print("=== Language ===")

    i = 0
    while i < len(Language.data):
        query = "%s language (Seperated by ',')? > "
        entry = list(Language.data)[i]
        answer = input(query % entry)
        if answer == '/b': 
            i -= 1
            continue
        Language.data[entry] = answer
        i += 1

    print("=== Interests ===")
    create_interest = input("Add an interest ? [Y/n] > ")
    if create_interest.lower() == 'y':
        i = 0; j = 0; interest = 0
        while interest < j + 1:
            while i < len(Interests.data[j]):
                query = "Interest %s? > "
                each_entry = list(Interests.data[j])[i]
                answer = input(query % each_entry) 
                if answer == '/b':
                    i -= 1
                    continue
                Interests.data[j][each_entry] = answer
                i += 1
            interest += 1
            answer = input("Add another? [Y/n] > ")
            if answer.lower() == 'y': 
                i = 0
                Interests.data.append({})
                for key in Interests.data[0].keys():
                    Interests.data[j + 1][key] = ""
                j += 1



    print("=== References ===")
    create_ref = input("Add a reference? [Y/n] > ")
    if create_ref.lower() == 'y':
        i = 0; j = 0; ref = 0
        while ref < j + 1:
            while i < len(References.data[j]):
                query = "%s? > "
                each_entry = list(References.data[j])[i]
                answer = input(query % each_entry) 
                if answer == '/b':
                    i -= 1
                    continue
                References.data[j][each_entry] = answer
                i += 1
            ref += 1
            answer = input("Add another? [Y/n] > ")
            if answer.lower() == 'y': 
                i = 0
                References.data.append({})
                for key in References.data[0].keys():
                    References.data[j + 1][key] = ""
                j += 1
    
    resume_data = {}
    resume_data['Basic'] = Basic.data
    resume_data['Work'] = Work.data
    resume_data['Education'] = Education.data
    resume_data['Project'] = Project.data
    resume_data['Awards'] = Awards.data
    resume_data['Publication'] = Publication.data
    resume_data['Skills'] = Skills.data
    resume_data['Language'] = Language.data
    resume_data['Interest'] = Interests.data
    resume_data['References'] = References.data

    with open(Basic.data['last_name'] + "_resume.json", "w") as outfile:
        json.dump(resume_data, outfile)

if __name__ == '__main__':
    usage = '''Usage:
    " Help
        resume h
        resume help
    " Generate cv_data.py (to edit)
        resume i
        resume init
    " Take CLI fill-in form
        resume
    " Compile cv_data.py to json
        resume c
        resume compile
    " Resume generate
        resume g
        resume generate
    " Sample usage
        1. By live editing
            resume init
            resume compile
            vim settings.json
            resume generate
        2. By form fill-in
            resume
            vim settings.json
            resume generate
    '''
    if len(sys.argv) == 1:
        fillin_guide()
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'h' or sys.argv[1] == 'help':
            print(usage)
        if sys.argv[1] == 'i' or sys.argv[1] == 'init':
            file = open('./cv_data.py', 'a')
            file.write(template_py)
            file.close()
            os.system('vi cv_data.py')
        if sys.argv[1] == 'g' or sys.argv[1] == 'generate':
            import socket
            SERVER_HOST = '0.0.0.0'
            SERVER_PORT = 2333
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((SERVER_HOST, SERVER_PORT))
            server_socket.listen(1)
            print("[Resume Generator] Start server at http://localhost:%s" % SERVER_PORT)
            print("Press <Ctrl - C> to shutdown")
            while True:
                client_connection, client_address = server_socket.accept()
                request = client_connection.recv(1024).decode()
                response = 'HTTP/1.0 200 OK\n\n'
                file = open('template.html', 'r')
                data = file.read()
                response += data
                client_connection.sendall(response.encode())
                client_connection.close()
            # Close socket
            server_socket.close()


    else:
        print(usage)

