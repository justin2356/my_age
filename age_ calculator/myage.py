from datetime import datetime

d_o_b = input('enter year of birth(YYYY): ')
try:
    #convert input to date time object
    dob_date = datetime.strptime(d_o_b,  '%Y')
except ValueError:
    print('enter only the year of birth (YYYY)')  

    #input name
name = input('enter your name: ')

    # calculate age 
current_year = datetime.now().year 
age = current_year - dob_date.year

    # output age and name


print(f'hello, {name}! you are {age} years old.')

# wtite to a text file
file_name = 'user_info.txt'
with open(file_name, 'w') as file:
      file.write(f'name: {name}\n') 
      file.write(f'age: {age}\n') 

# read from a text file and print its contents
with open(file_name, 'r')as file:
    print('\ncontents of the file:')
    for line in file:
          print(line.strip())

