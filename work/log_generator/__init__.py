from faker import Faker
import random

directory_list = ['/a', '/b', '/c', '/d', '/e', '/f', '/g', '/h', '/i', '/j', '/k', '/l', '/m', '/n', '/o', '/p', '/q', '/r', '/s', '/t', '/u',
'/v', '/w', '/x', '/y', '/z']
html_list =  ['/a.html', '/b.html', '/c.html']
jpg_list = ['/d.jpg', '/e.jpg', '/f.jpg']
mp4_list = ['/g.mp4', '/h.mp4', '/i.mp4']

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
    faker = Faker()
    path, size = generate_path()
    method = ["GET", "POST"][random.gauss(0.4, 0.1) > 0.6]
    ip_address = faker.ipv4_public()
    user_agent = faker.user_agent()
    log = f'{ip_address} - - [{date}] "{method} {path}" 200 {size} "{user_agent}"'
    return log
