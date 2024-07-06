import requests
from bs4 import BeautifulSoup
from colorama import Fore
y = Fore.YELLOW
g = Fore.GREEN
b = Fore.BLUE
m = Fore.MAGENTA
r = Fore.RED
class Generate:
    @staticmethod
    def get_email():
        response = requests.get("https://yopmail.com/email-generator")
        soup = BeautifulSoup(response.text, 'html.parser')
        email = soup.find('div', {'id': "geny"}).text.strip()
        return email
def main():
    ascii = '''
                                                          ███  ████                                 
                                                         ░░░  ░░███                                 
 █████ ████  ██████  ████████  █████████████    ██████   ████  ░███      ███████  ██████  ████████  
░░███ ░███  ███░░███░░███░░███░░███░░███░░███  ░░░░░███ ░░███  ░███     ███░░███ ███░░███░░███░░███ 
 ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███   ███████  ░███  ░███    ░███ ░███░███████  ░███ ░███ 
 ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███  ███░░███  ░███  ░███    ░███ ░███░███░░░   ░███ ░███ 
 ░░███████ ░░██████  ░███████  █████░███ █████░░████████ █████ █████   ░░███████░░██████  ████ █████
  ░░░░░███  ░░░░░░   ░███░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░░░     ░░░░░███ ░░░░░░  ░░░░ ░░░░░ 
  ███ ░███           ░███                                               ███ ░███                    
 ░░██████            █████                                             ░░██████                     
  ░░░░░░            ░░░░░                                               ░░░░░░                      
'''
    print(f"{Fore.LIGHTCYAN_EX}{ascii}")
    emails = []
    ask = int(input(f"{y}How many emails to generate? {g}> "))
    save = 0
    try:
        for i in range(ask):
            generated_email = Generate.get_email()
            print(f"{b}Your generated email {m}> {generated_email}")
            emails.append(generated_email)
            save += 1
            if save == ask:
                emails_to_list = '\n'.join(emails)
                with open("generated_emails.txt", 'w') as file:
                    file.write(emails_to_list)
                    print(f"{y}Generated {g}{ask} {y}emails")
    except Exception as e:
        print(f"{r}Error > {e}")
main()