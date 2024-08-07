
import sqlite3
import my_table_connection.sql_string as sql_string
import config
import my_table_connection.retreive_data
import my_table_connection.show_detailed_data


def drop_create_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    for table_name in config.list_tables:
        try:
            c.execute(sql_string.drop_table(table_name))
        except:
            pass
        try:
            c.execute(sql_string.create_table(table_name))
        except:
            pass
    conn.commit()
    conn.close()


def name_player(my_string):
    return my_string[my_string.find('(') + 1:len(my_string) - 1]

def name_team(my_string):
    if 'me">' in my_string:
        return my_string[4:my_string.find('(') - 1]
    return my_string[:my_string.find('(') - 1]


#  returning the team names and the links for each.
def get_first_page_data(my_link):
    return retreive_data.get_first_page_data(my_link)

def get_detail_team_games(my_link):
    return retreive_data.get_detail_team_games(my_link)

def show_all_detailed_data():
    return show_detailed_data.main()



# getting a total page from one game and insert it page by page. also check if record exist
def import_my_data_to_database(my_data):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    for line in my_data:
        try:
            c.execute(sql_string.import_data_to_table(line))
        except Exception as error:
            print(error.args)
    conn.commit()
    conn.close()

