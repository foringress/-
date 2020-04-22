import requests,string
from urllib.parse import quote

douban_nickname = "Test_bot_ing"  # 
#passnmae_prompt = "请输入您的登录帐号："
#password_prompt = "请输入您的登录密码："
passname = ""
password = ""

login_form_data = {
    "ck":"",
    "name":passname,
    "password":password,
    "remember":"false",
    "ticket":"",
}

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"}

session = requests.Session()

login_post_url = "https://accounts.douban.com/j/mobile/login/basic"
post=session.post(url=login_post_url, data=login_form_data, headers=headers)

print("post文本:\n"+post.text)#似乎不成功

home_url = "https://accounts.douban.com/passport/setting"
check_response_text = session.get(url=home_url, headers=headers)

if douban_nickname in check_response_text.text:
    print("登录成功\n")
    #return session
else:
    print()
    print("登录失败,请重新尝试.\n")