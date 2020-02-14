# https://python.gotrained.com/scraping-telegram-group-members-python-telethon/
import csv

async def write_csv(all_participants, filename):
    with open(filename,"w",encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['username','user_id', 'name'])
        for user in all_participants:
            if user.username:
                username= user.username
            else:
                username= ""
            if user.first_name:
                first_name= user.first_name
            else:
                first_name= ""
            if user.last_name:
                last_name= user.last_name
            else:
                last_name= ""
            name= (first_name + ' ' + last_name).strip()
            writer.writerow([username ,user.id ,name])

async def read_csv(filename):
    user_id = []
    for d in csv.DictReader(open(filename)):
        user_id.append(int(d['user_id']))
    return user_id