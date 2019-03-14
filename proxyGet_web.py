#-*- coding: utf-8 -*-
import flask
import urllib.request as u
import base64

app = flask.Flask(__name__)
@app.route("/")

def getList():
    #f = open("proxyList.log",'w',encoding='utf-8')
    url="https://raw.githubusercontent.com/AmazingDM/sub/master/ssrshare.com"
    page = u.urlopen(url)
    html = page.read().decode('UTF-8')

    SSR_list=base64.b64decode(html).decode('utf-8')
    SSR_list=SSR_list.strip()   
    lst=SSR_list.splitlines()
    list_sum="<h4>嗨，我是少华，以下代理服务器信息每三天更新一次。Shadowsocks的获取地址: https://github.com/shadowsocks/shadowsocks-windows/releases。如果有问题请联系我：shi.sh@foxmail.com. 翻墙快乐！</h4>"
    for i in lst:
        try:
            base64_encode_str = i[6:]
            decode_str = base64_decode(base64_encode_str)
            parts = decode_str.split(':')
            if len(parts) != 6:
                print('不能解析SSR链接: %s' % base64_encode_str)

            server = parts[0]
            port = parts[1]
            protocol = parts[2]
            method = parts[3]
            obfs = parts[4]
            password_and_params = parts[5]

            password_and_params = password_and_params.split("/?")

            password_encode_str = password_and_params[0]
            password = base64_decode(password_encode_str)
            params = password_and_params[1]

            param_parts = params.split('&')

            param_dic = {}
            for part in param_parts:
               key_and_value = part.split('=')
               param_dic[key_and_value[0]] = key_and_value[1]

            obfsparam = base64_decode(param_dic['obfsparam'])
            protoparam = base64_decode(param_dic['obfsparam'])
            remarks = base64_decode(param_dic['remarks'])
            group = base64_decode(param_dic['group'])

            lst_item='服务器地址: %s, 端口: %s, 协议: %s, 加密方法: %s, 密码: %s, 混淆: %s, 混淆参数: %s, 协议参数: %s, 备注: %s, 分组: %s\r\n'% (server, port, protocol, method, password, obfs, obfsparam, protoparam, remarks, group)
            list_sum+=lst_item
            
        except Exception as e:
            print (e)
            continue
    print (list_sum)
    return list_sum
def fill_padding(base64_encode_str):

   need_padding = len(base64_encode_str) % 4 != 0

   if need_padding:
       missing_padding = 4 - need_padding
       base64_encode_str += '=' * missing_padding
   return base64_encode_str


def base64_decode(base64_encode_str):
   base64_encode_str = fill_padding(base64_encode_str)
   return base64.urlsafe_b64decode(base64_encode_str).decode('utf-8')


if __name__ == '__main__':
    app.debug = True
    app.run().getList()
    print("All finished")    


