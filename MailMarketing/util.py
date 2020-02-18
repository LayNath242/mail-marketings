# https://python.gotrained.com/scraping-telegram-group-members-python-telethon/
import csv

async def write_csv(all_participants, filename):
    with open(filename,"w",encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['No','username','user_id', 'name'])
        n = 0
        for user in all_participants:
            n +=1
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
            writer.writerow([n,username ,user.id ,name])


async def read_csv(filename):
    user_id = []
    for d in csv.DictReader(open(filename)):
        user_id.append(int(d['user_id']))
    return user_id

async def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS