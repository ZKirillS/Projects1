from utils import unzip_with_7z
import string

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------

for letter1 in string.ascii_lowercase:
    for letter2 in string.ascii_lowercase:
        password = letter1 + letter2 + 'bcmpda'
        if unzip_with_7z(zip_file_path, dest_path, password): 
            print('You win')
            break

