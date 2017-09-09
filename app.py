import requests
from bs4 import BeautifulSoup


def sign():

    s = requests.session()
    log_data = {'loginPhone':'18209347100','loginPassword':'ssh19198918'} 
    sgn_data = {'translatorId':'WE16104633TR'}
    

    log = s.post('http://talent.woordee.com/front/truser/login', log_data) 
    html = s.get('http://talent.woordee.com/front/truser/userCenter')
    page = html.content
    #print page

    s.post('http://talent.woordee.com/front/truser/sign', sgn_data)

    soup = BeautifulSoup(page,"html.parser")
    txt1 = soup.find_all('a', attrs={"class":"btn-sign"})[0].get_text()
    txt2 = soup.find_all('p', attrs={"class":"p2"})[0].get_text() 
    return txt1+', '+txt2

sign()

