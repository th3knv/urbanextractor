from bs4 import BeautifulSoup
import requests

while True:
    try:
        print('URBAN DICTIONARY SEARCH')
        url_choice =input('Enter a key word : ')


        urbansite_ ='https://www.urbandictionary.com/define.php?term=' + url_choice
        response = requests.get(urbansite_)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Word explain
        table_explain = soup.find('div', class_ = 'break-words meaning mb-4')
        #Some comment
        table_comment = soup.find('div', class_ = 'break-words example italic mb-4')
        #By who
        table_who = soup.find('div', class_ = 'contributor font-bold')
        #OUTPUTS
        text_explain = table_explain.get_text().strip()
        text_comment = table_comment.get_text().strip()
        text_bywho = table_who.get_text().strip()
        print(text_explain)
        print('')
        print(text_comment)
        print('')
        print(text_bywho)
        print('')
        print('--------------------------------------------------------------------------------------------------')
    except:
        print("Error / Invalid key word / Text doesn't exist")
