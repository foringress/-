if douban_nickname in check_response_text.text:成功    else:失败

使用豆瓣ID判断是否登陆成功

当然用requests.Session().get.text的文本

目前是失败的

于是怀疑是不是post环节出了问题
post=session.post(url=login_post_url, data=login_form_data, headers=headers)
text情况如下
{"status":"failed","message":"parameter_missing","description":"参数缺失","payload":{}}

这时候还需要cookies

F12走起
得到
cookies={
    	'ap_v':'0,6.0' ,
		'bid':'Dmha1rYraOc',
		'ct ':'y ',
		'll': "118301" ,
		'ps' :'y' ,
		'push_doumail_num': '0' ,
		'push_noty_num':' 0' ,
    }
    添加cookie到post里面即可成功登陆
