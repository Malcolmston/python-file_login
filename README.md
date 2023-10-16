# python-file_login
a python app that allows a user to creat accounts, log in, and store files to a "remote" / local location

## Loging in
1. there will be 2 types of users 
2. basic
3. admin

| Basic | Admin |
 ------- -------
| Store files | Vue other files that exist |
| soft remove files| permanently remove files or soft remove files|


## sign up

1. Create a new user account

| Basic | Admin |
 ------- -------
| Create a new user | X |




## validation
1. basic validation
    there must be 3 letters
    there must be 1 uppercase letter
    there must be 1 numbers
    there must be 0 to 3 symble
    length must be between 4 and 9

    '''reg-ex
    ([A-Z]{1,4})+([a-z]{3,7})+([0-9]{2,7})+(\w{0,3})
    '''

2. admin validation
    there must be 5 letters
    there must be 1 uppercase letter
    there must be 2 numbers
    there must be 1 symble
    length must be between 7 and 18
    ([A-Z]{1,4})+([a-z]{5,9})+([0-9]{2,7})+(\w{1,3})