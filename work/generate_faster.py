"""
windows 환경에서는 적합하지 않은 코드입니다.
"""
from faker import Faker
import random
import concurrent.futures
from datetime import timedelta
from dateutil.parser import parse

directory_list = ['/a', '/b', '/c', '/d', '/e', '/f', '/g', '/h', '/i', '/j', '/k', '/l', '/m', '/n', '/o', '/p', '/q', '/r', '/s', '/t', '/u',
'/v', '/w', '/x', '/y', '/z']
html_list =  ['/a.html', '/b.html', '/c.html']
jpg_list = ['/d.jpg', '/e.jpg', '/f.jpg']
mp4_list = ['/g.mp4', '/h.mp4', '/i.mp4']

procs = []
pool = concurrent.futures.ProcessPoolExecutor()
def generate_iu():
  faker = Faker()
  return faker.ipv4_public(), faker.user_agent()
for _ in range(1000):
    procs.append(pool.submit(generate_iu))    
iu_list = [p.result() for p in concurrent.futures.as_completed(procs)]

def generate_path(depth = 2):
    """

    Parameters
    ----------
    depth : TYPE, optional
        DESCRIPTION. The default is 2.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    path = []
    for _ in range(random.randrange(depth + 1)):
        path.append(directory_list[random.randrange(0, 26)])
    
    file = ((html_list, jpg_list, mp4_list)[random.randrange(0, 3)])[random.randrange(0, 3)]
    path.append(file)
    
    return "".join(path), random.randrange(100, 7000)



def generate_log(date):
    """
    generate web log

    Parameters
    ----------
    date : str
        Date the log was created

    Returns
    -------
    log : str
        web log format: {ip_address} - - {date} "{method} {path}" 200 {size} "{user_agent}"

    """
    path, size = generate_path()
    method = ["GET", "POST"][random.gauss(0.4, 0.1) > 0.6]
    ip_address, user_agent = iu_list[random.randrange(len(iu_list))]

    log = f'{ip_address} - - [{date}] "{method} {path}" 200 {size} "{user_agent}"'
    return log

#################################################

pool = concurrent.futures.ProcessPoolExecutor()

procs = []
log_list = []

for _ in range(3000):
    procs.append(pool.submit(generate_log, "****"))

for p in concurrent.futures.as_completed(procs):
    log_list.append(p.result())

now = parse("1997-04-11 00:00:00")
logs = []
td = timedelta(seconds = 1)

while now < parse("1997-04-12 00:00:00"):
    logs.append(log_list[random.randrange(3000)].replace("****", now.strftime("%Y-%m-%d %H:%M:%S")))
    now += td

with open("access_970411.log", "w") as log_file:
    for log in logs:
        log_file.write(log)
        log_file.write("\n")