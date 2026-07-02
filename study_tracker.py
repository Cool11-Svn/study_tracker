
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

def full_input(user_input99): 
  while True:
    try:
        value =input(user_input99).strip()
        if value == '':
         print('Cannot be empty.Enter something')
        if value == "b":
         return "b"
        else:
         return value  
    except EOFError:
         print("No input received. Try again.")
      
def get_positive_int(the_input):
    while True:
        try:
            value = input(the_input).strip().lower()

            # universal back option
            if value == "b":
                return "b"

            value = int(value)

            if value >= 0:
                return value
            else:
                print("Enter positive number or 0")

        except ValueError:
            print("Enter right number.")

        except EOFError:
            print("No input received. Try again.")

def get_valid_text(the_input):
    while True:       
        try:
                                       
            value = input(the_input).strip().lower()
            value = ' '.join(value.split())
            if value =='b':
              return 'b'
            if value == "":
             print("Cannot be empty")
            elif value.isdigit():
             print("Cannot be only numbers")  
            else: 
                
              return value
           
        except EOFError:
            print("No input received. Try again.")

def main():

  def create_study_list():

   while True:

     subject =  get_valid_text('Enter the subject: ').lower().strip()
     if subject =='b':
       return
   
     direction =  get_valid_text('Enter the direction of particular subject: ').lower().strip()
     if direction == 'b':
       return
     
     duration = get_positive_int('Enter duration of given subject: ')
     if duration == 'b':
       return
     while True:
      print('Enter when subject starts - day month and year ')
      try:                                                         
       input_day = get_positive_int('Enter day: ')  
       if input_day =='b':
        return
                                                                   
       input_month = get_positive_int('Enter month: ')
       if input_month =='b':
         return
       input_year = get_positive_int('Enter year: ')
       if input_year =='b':
         return
      
       date_object = datetime.datetime(input_year, input_month, input_day)
       break
      except ValueError:
         print('Enter correct date')
      except EOFError:
         print("No input received. Try again.")
                  
     note =  full_input('Write some notes about the subject: ')
     if note =='b':
       return

     All_sessions.append({
         
         'subject': subject,
         'direction': direction,
         'duration': duration,
         'date': date_object,
         'note': note
     })
     save_list()
     while True:
      print('Shall we go on?')
      print('1 - yes,2 - no')
  
      go_on = get_positive_int('Enter here: ')
      if go_on != 1:
       return
      elif go_on==1:
        break
      
      else:
       print('Choose from given options ')
       
   


  def show_study_list(All_sessions):

     for i,subject in enumerate(All_sessions,start =1):
        print("\n----------------------")
        print(f"Id: {i}")
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

            # convert datetime -> string
            session_copy["date"] = session_copy["date"].strftime("%Y-%m-%d")

            temp_list.append(session_copy)

        json.dump(temp_list, file,indent=4)


  def delete_session():
    subject_id = get_positive_int('Enter the ID of subject you want to delete: ')
    
    if subject_id == 'b':
        return

    index = subject_id - 1

    if 0 <= index < len(All_sessions):
        del All_sessions[index]

        print()
        print('Particular subject was successfully deleted!')
        print()
        save_list()
    else:
        print()
        print('Such subject cannot be deleted. Check your inputs!')
        print()
    


  def edit_session():

    subject_id = get_positive_int('Enter the ID of subject you want to edit: ')
    if subject_id == 'b':
        return

    right_choices = ['subject', 'direction', 'duration', 'date', 'note']

    while True:

        field = input(
            'Enter field to edit (subject|direction|duration|date|note): '
        ).lower().strip()

        if field == 'b':
            return

        if field in right_choices:
            break

        print('Choose from given menu please')

    # get replacement value

    if field == 'subject':

        new_value = get_valid_text('Enter new value: ')
        if new_value == 'b':
            return

    elif field == 'direction':

        new_value = get_valid_text('Enter new value: ')
        if new_value == 'b':
            return

    elif field == 'note':

        new_value = full_input('Enter new note: ')
        if new_value == 'b':
            return

    elif field == 'duration':

        new_value = get_positive_int('Enter new duration value: ')
        if new_value == 'b':
            return

    elif field == 'date':

        while True:

            try:
                print('Enter new date - day month and year')

                day = get_positive_int('Enter day: ')
                if day == 'b':
                    return

                month = get_positive_int('Enter month: ')
                if month == 'b':
                    return

                year = get_positive_int('Enter year: ')
                if year == 'b':
                    return

                new_value = datetime.datetime(year, month, day)
                break

            except ValueError:
                print('Enter correct date')

            except EOFError:
                print("No input received. Try again.")

   

    index = subject_id - 1

    if 0 <= index < len(All_sessions):
        edit_session = All_sessions[index]

        edit_session[field] = new_value 
       

        print()
        print('Operation was successful')
        print()

        save_list()
        return
    else:

        print()
        print('Such operation cannot happen. Check your inputs!')
        print()
    

  


  def total_std_time_per_sub():  
    time_subject = get_valid_text('Enter the name of subject: ').lower().strip()
    if time_subject =='b':
       return
    total_time = 0

    for list_member in All_sessions:
     if list_member['subject'] == time_subject:
       total_time += (list_member['duration'])

    print()
    print(f'{total_time/60:,.3f} hours in total for given subject')
    print()

  
  def total_std_time_dw():
    subject_to_calculate = get_valid_text('Enter the name of subject: ').lower().strip()
    if subject_to_calculate =='b':
       return
    while True:
      print('Enter date of subject - day month and year')
      try:                                                     
       day = get_positive_int('Enter day: ')  
       if day == 'b':
         return             
       month = get_positive_int('Enter month: ')
       if month == 'b':
         return  
       year = get_positive_int('Enter year: ')
       if year == 'b':
         return  
      
       end_date = datetime.datetime(year, month, day)
       break
      except ValueError:
         print('Enter correct date')
      except EOFError:
         print("No input received. Try again.")

    
    seven_days = datetime.timedelta(days=7)   
   
    seven_days_ago = end_date - seven_days    
    weekly_total = 0
    daily_total = 0
    for list_member in All_sessions:
      if list_member['subject'] == subject_to_calculate and\
        seven_days_ago<= list_member['date'] <= end_date:
         weekly_total += (list_member['duration'])
    print()     
    print(f'Total weekly time: {weekly_total/60:,.3f} hours')

    for list_member in All_sessions:
      if list_member['subject'] == subject_to_calculate and\
       list_member['date'].date() == end_date.date():
       daily_total += (list_member['duration'])
    if daily_total == 0:
     print("Total daily time: 0")
    else:
     print()
     print(f"Total daily time: {daily_total/60:,.3f} hours")
     print()
    
        
  while True:

   print('Choose what you want')
   print()
   print('Add session - 1 \n' \
   'View all sessions - 2\n' \
   'Delete session - 3\n' \
   'Edit session - 4\n' \
   'Total study time per subject - 5\n' \
   'Total study time per day/week(of subject) - 6\n' \
   'Exit program - 7\n'
   'Go to main menu - b\n')
   print()
   while True:
    list_of_numbers =[1,2,3,4,5,6,7,'b']  
    user_input1 = get_positive_int('Enter here: ')   
    if user_input1 not in list_of_numbers:
     print()
     print('Enter the number from menu.')
     print()
    else:
      break 
   
    

   if user_input1 == 1:
    create_study_list()
  

   elif user_input1 == 2:
    show_study_list(All_sessions)

   elif user_input1 == 3:
     delete_session()
  

   elif user_input1 == 4:
    
     edit_session()
     

   elif user_input1 == 5:
    total_std_time_per_sub()

   elif user_input1 == 6:    
     total_std_time_dw()
     
   elif user_input1 == 7:
     break    



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:                         # if user presses cntrl + c - we handle error globally.
        print("\nProgram stopped by user.")

