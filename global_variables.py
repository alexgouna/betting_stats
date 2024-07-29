import time
import requests
from bs4 import BeautifulSoup

list_tables=["table_team_games"]

link_main_page =["https://www.totalcorner.com/league/view/12995"]

last_page_custom_bool = False
last_page_custom_page = 2


def get_last_page(my_link):

    if last_page_custom_bool:
        return last_page_custom_page
    else:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(my_link, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            my_data=str(soup)
            # print(my_data)
            last_pos = my_data.find('last')
            temp = my_data[last_pos-50:last_pos]
            temp = temp[temp.find(':')+1:temp.find('"',temp.find(':')+1)]
            try:
                return int(temp)+1
            except:
                return 1

        except Exception as error:
            print(error)
            print("Try again to get the total pages")
            time.sleep(20)
            get_last_page(my_link)




