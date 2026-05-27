
import json
import datetime

# LIST OF DICTIONARIES
All_sessions = []

filename = "all_sessions.json"

# ---------------- LOAD ----------------
try:
    with open(filename, "r") as file:
        All_sessions = json.load(file)

        # convert date string → datetime object
        for session in All_sessions:
            session["date"] = datetime.datetime.strptime(
                session["date"], "%Y-%m-%d"
            )

except FileNotFoundError:
    All_sessions = []
except json.JSONDecodeError:
    print("Warning!!! JSON file is corrupted.")
    print("Starting with a new empty  list.")
    All_sessions = []    

#error handling functions
def full_input(user_input99): 
  while True:
    try:
        value =input(user_input99).strip()
        if value == '':
         print('Cannot be empty.Enter something')
        else:
         return value  
    except EOFError:
         print("No input received. Try again.")
      
def get_positive_int(the_input2):  
    while True:        
        try:  
         value =  int(input(the_input2).strip())  
      
         if value >= 0:
            return value
         else:
            print('Enter positive number or 0')            
      
        except ValueError:
            print("Enter right number.")

        except EOFError:
            print("No input received. Try again.")

def get_valid_text(the_input3):
    while True:       
        try:                                   
            value = input(the_input3).strip().lower()
            value = ' '.join(value.split())

            if value == "":
             print("Cannot be empty")
            elif value.isdigit():
             print("Cannot be only numbers")  
            else: 
                
              return value
           
        except EOFError:
            print("No input received. Try again.")

      
#main function. 
def main():

  def create_study_list():

    go_on = 1

    while go_on == 1:

     subject =  get_valid_text('Enter the subject: ').lower().strip()
     direction =  get_valid_text('Enter the direction of particular subject: ').lower().strip()
     
     duration = get_positive_int('Enter duration of given subject: ')
     while True:
      print('Enter when subject starts - day month and year ')
      try:                                                          # we try to create a datetime object.if user enters invalid date like 45.43.2026
       input_day = get_positive_int('Enter day: ')               # we will ask him to enter again the valid date.plus we handle other invalid inputs.
       input_month = get_positive_int('Enter month: ')
       input_year = get_positive_int('Enter year: ')
      
       date_object = datetime.datetime(input_year, input_month, input_day)
       break
      except ValueError:
         print('Enter correct date')
      except EOFError:
         print("No input received. Try again.")
                  
     note =  full_input('Write some notes about the subject: ')

     All_sessions.append({
         'subject': subject,
         'direction': direction,
         'duration': duration,
         'date': date_object,
         'note': note
     })
     while True:
      print('Shall we go on?')
      print('1 - yes,2 - no')
  
      go_on = get_positive_int('Enter here: ')
      if go_on == 2:
       break
      elif go_on != 1:
       print('Choose from given options ')
       
   


  def show_study_list(All_sessions):

     for subject in All_sessions:
        print("\n----------------------")
        print(f"Subject: {subject['subject']}")
        print(f"Direction: {subject['direction']}")
        print(f"Duration: {subject['duration']} min")
        print(f"Date: {subject['date'].date()}")
        print(f"Note: {subject['note']}")
        print()


  def save_list():

    with open('all_sessions.json', 'w') as file:

        temp_list = []

        for session in All_sessions:
            session_copy = session.copy()

            # convert datetime → string
            session_copy["date"] = session_copy["date"].strftime("%Y-%m-%d")

            temp_list.append(session_copy)

        json.dump(temp_list, file)


  def delete_session(user_input2, user_input3, user_input4, user_input5):

    found = False

    for list_member in All_sessions:
     if list_member['subject'] == user_input2 and\
        list_member['direction'] == user_input3 and\
        (list_member['duration']) == user_input4 and\
        list_member['date'] == user_input5:

        found = True
        All_sessions.remove(list_member)
        print()
        print('Particular subject was succssesfully deleted!')
        print()
        save_list()
        break

    if not found:
       print()
       print('Such subject cannot be deleted.Check your inputs!')
       print()


  def edit_session(user_input6, user_input7, user_input8, user_input9, user_input10, user_input11):
    # here we try to edit particular field

    found = False

    for list_member in All_sessions:
                                                                       # So we got inputs from user - they have to fully match with what we have in our list already.and if they match 
                                                                       #we allow to make edit. input10 is key and input 11 is new value.
     if list_member['subject'] == user_input6 and\
        list_member['direction'] == user_input7 and\
        (list_member['duration']) == user_input8 and\
        list_member['date'] == user_input9:

        found = True
        list_member[user_input10] = user_input11

        print('Operation was successful')
        save_list()
        break

    if not found:
       print('Such operation cannot happen.Check your inputs!')

  


  def total_std_time_per_sub(time_subject):  
   # we calculate total study time for subject -All weeks!
   total_time = 0

   for list_member in All_sessions:
     if list_member['subject'] == time_subject:
       total_time += (list_member['duration'])

   print()
   print(f'{total_time/60:,.3f} hours in total for given subject')
   print()

  
  def total_std_time_dw(subject_to_calculate,end_date):
   #total study time day and week 
    
    seven_days = datetime.timedelta(days=7)   # using a  datetime module,creating a 7-day time period.
   
    seven_days_ago = end_date - seven_days    
    weekly_total = 0
    daily_total = 0
    for list_member in All_sessions:
      if list_member['subject'] == subject_to_calculate and\
        seven_days_ago<= list_member['date'] <= end_date:
         weekly_total += (list_member['duration'])
    print(f'Total weekly time: {weekly_total/60:,.3f} hours')

    for list_member in All_sessions:
      if list_member['subject'] == subject_to_calculate and\
       list_member['date'].date() == end_date.date():
       daily_total += (list_member['duration'])
    if daily_total == 0:
     print("Total daily time: 0")
    else:
     print(f"Total daily time: {daily_total/60:,.3f} hours")
    
   
   # this part actually controlls the program         
  while True:

   print('Choose what you want')
   print('Add session - 1 \nView all sessions - 2\nDelete session - 3\nEdit session - 4\nTotal study time per subject - 5\nTotal study time per day/week(of subject) - 6\nExit program - 7')
   print()
   while True:
    list_of_numbers =[1,2,3,4,5,6,7]  
    user_input1 = get_positive_int('Enter here: ')   # user has to choose from given menu which is a list.
    if user_input1 not in list_of_numbers:
     print()
     print('Enter the number from menu.')
     print()
    else:
      break 
   
    

   if user_input1 == 1:
    create_study_list()
    save_list()

   elif user_input1 == 2:
    show_study_list(All_sessions)

   elif user_input1 == 3:

     user_input2 = get_valid_text('Enter which subject you want to delete: ').lower().strip()
     user_input3 = get_valid_text('Enter direction of a subject: ').lower().strip()
     user_input4 = get_positive_int('Enter duration: ')

     while True:
      print('Enter date of subject - day month and year')
      try:                                                          
       input_day = get_positive_int('Enter day: ')              
       input_month = get_positive_int('Enter month: ')
       input_year = get_positive_int('Enter year: ')
      
       user_input5 = datetime.datetime(input_year, input_month, input_day)
       break
      except ValueError:
         print('Enter correct date')
      except EOFError:
         print("No input received. Try again.")
  
     delete_session(user_input2, user_input3, user_input4, user_input5)
     save_list()

   elif user_input1 == 4:

     user_input6 = get_valid_text('Enter which subject you want to edit: ').lower().strip()
     user_input7 = get_valid_text('Enter direction of a subject: ').lower().strip()
     user_input8 = get_positive_int('Enter duration: ')

     while True:
      print('Enter date of subject - day month and year')                                           # here we try to find the particular member of list we want to edit
      try:                                                                                         # we have to go through all checks before we proceed
       input_day = get_positive_int('Enter day: ')               
       input_month = get_positive_int('Enter month: ')
       input_year = get_positive_int('Enter year: ')
      
       user_input9 = datetime.datetime(input_year, input_month, input_day)
       break
      except ValueError:
         print('Enter correct date')
      except EOFError:
         print("No input received. Try again.")

     while True:
      right_choices =['subject','direction','duration','date','note']
      user_input10 = input('Enter field to edit (subject|direction|duration|date|note): ').lower().strip()   
      if user_input10.lower().strip() not in right_choices:
        print('Choose from given menu please')
      else:
         break 
     if user_input10.lower().strip() =='subject':
        user_input11 = get_valid_text('Enter new value')
     elif user_input10.lower().strip() =='direction':
        user_input11 = get_valid_text('Enter new value')  
     elif user_input10.lower().strip() == 'note':
        user_input11 = full_input('Enter new note')    

    
     elif user_input10.lower().strip() == 'date':
      while True:
        
        try:  
            print('Enter date of subject - day month and year')                                                        
            input_day = get_positive_int('Enter day: ')               
            input_month = get_positive_int('Enter month: ')
            input_year = get_positive_int('Enter year: ')
      
            user_input11 = datetime.datetime(input_year, input_month, input_day)
            break
        except ValueError:
         print('Enter correct date')
        except EOFError:
         print("No input received. Try again.")
              
     elif user_input10.lower().strip() == 'duration':
        while True:
         try:
          user_input11 = get_positive_int('Enter new duration value: ')
          break
         except ValueError:
          print('Enter correct duration value')
         except EOFError:
          print("No input received. Try again.")
      
               
     
     edit_session(user_input6, user_input7, user_input8, user_input9, user_input10, user_input11)

   elif user_input1 == 5:
     time_subject = get_valid_text('Enter the name of subject: ').lower().strip()
     total_std_time_per_sub(time_subject)

   elif user_input1 == 6:
     subject_to_calculate = get_valid_text('Enter the name of subject: ').lower().strip()
     while True:
      print('Enter date of subject - day month and year')
      try:                                                     
       input_day = get_positive_int('Enter day: ')             
       input_month = get_positive_int('Enter month: ')
       input_year = get_positive_int('Enter year: ')
      
       end_date = datetime.datetime(input_year, input_month, input_day)
       break
      except ValueError:
         print('Enter correct date')
      except EOFError:
         print("No input received. Try again.")
            
     print()
     total_std_time_dw(subject_to_calculate,end_date)
     print()


   elif user_input1 == 7:
     break

   save_list()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:                         # if user presses cntrl + c - we handle error globally.
        print("\nProgram stopped by user.")

