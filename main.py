def prompt_user_for_data ( ):
  file_name = input ("Enter the file name:")
  first_name = input ( "Enter your name:")
  street_address = input ("Enter your street address: ")
  phone_number = input ( "Enter your phone number:")

  with open (file_name, 'w') as file:
    file.write(f"{first_name},{street_address},  {phone_number}") 
    
def read_file_and_display_contents ( ):
    file_name = input ( "Enter the file name to read:")

    with open (file_name,'r') as file:
      contents = file.read ( )
      print ( "Contents of the file:")
      print (contents)
def main ( ):
    prompt_user_for_data()
    read_file_and_display_contents()
if __name__== "__main__" :
    main()