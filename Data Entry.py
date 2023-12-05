import tkinter.messagebox
from tkinter import *
from tkinter import ttk


def enter_data():
    accepted = accept_var.get()

    if accepted == 'Accepted':
        # User Info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title_name = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            print('First name: ', firstname, 'Last name: ', lastname)
            print('Title: ', title_name, 'Age: ', age, 'Nationality', nationality)

            # Course Info
            registration_status = reg_status_var.get()
            numcourse = numcourses_spinbox.get()
            numsemester = numsemesters_spinbox.get()

            print('# Courses: ', numcourse, '#Semesters: ', numsemester)
            print('Registration status: ', registration_status)
            print('-------------------------------------')
        else:
            tkinter.messagebox.showwarning(title='Error', message='First name and last name are required ')
    else:
        tkinter.messagebox.showwarning(title='Error', message='You have not accepted the terms !')


root = Tk()
root.title('Data Entry Form')

frame = Frame(root)
frame.pack()

# Saving User Info
user_info_frame = LabelFrame(frame, text='User Informations')
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

# First name label
first_name_label = Label(user_info_frame, text='First Name')
first_name_label.grid(row=0, column=0)

# Last name label
last_name_label = Label(user_info_frame, text='Last Name')
last_name_label.grid(row=0, column=1)

# First name entry

first_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

# Title label and combobox
title = Label(user_info_frame, text='Title')
title.grid(row=0, column=2)
options = ['', 'Mr.', 'Ms.', 'Dr.']
title_combobox = ttk.Combobox(user_info_frame, values=options)
title_combobox.grid(row=1, column=2)

# age label and spinbox

age_label = Label(user_info_frame, text='Age')
age_label.grid(row=2, column=0)

age_spinbox = ttk.Spinbox(user_info_frame, from_=18, to=110)
age_spinbox.grid(row=3, column=0)

# Nationality label and combobox

nationality_label = Label(user_info_frame, text='Nationality')
nationality_label.grid(row=2, column=1)

nationality_options = ['North America',
                       'South America',
                       'Oceania',
                       'Australia',
                       'Europe',
                       'Asia',
                       'Africa',
                       'Middle East',
                       'Antarctica']

nationality_combobox = ttk.Combobox(user_info_frame, values=nationality_options)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info

course_frame = LabelFrame(frame)
course_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

registered_label = Label(course_frame, text='Registration Status')
registered_label.grid(row=0, column=0)

reg_status_var = StringVar(value='Not Registered')
registered_check = Checkbutton(course_frame, text='Currently Registered',
                               variable=reg_status_var,
                               onvalue='Registered',
                               offvalue='Not Registered')
registered_check.grid(row=1, column=0)

numcourses_label = Label(course_frame, text='# Completed Courses')
numcourses_label.grid(row=0, column=1)

numcourses_spinbox = Spinbox(course_frame, from_=0, to=500)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = Label(course_frame, text='# Semesters')
numsemesters_label.grid(row=0, column=2)

numsemesters_spinbox = Spinbox(course_frame, from_=0, to=16)
numsemesters_spinbox.grid(row=1, column=2)

for widgets in course_frame.winfo_children():
    widgets.grid_configure(padx=10, pady=5)


# Accepted Terms

terms_frame = LabelFrame(frame, text='Terms and Conditions')
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

accept_var = StringVar(value='Not Accepted')

terms_check = Checkbutton(terms_frame, text='I accept terms and confitions.',
                          variable=accept_var,
                          onvalue='Accepted',
                          offvalue='Not Accepted')
terms_check.grid(row=0, column=0)

# Button

button = Button(frame, text='Enter data', command=enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=10)


root.mainloop()
