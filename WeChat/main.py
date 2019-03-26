from scrapy import cmdline
from WeChat.login import login_sogou

# 搜狗买房  登陆微信号扫描的二维码在这个网址
house_url = 'https://open.weixin.qq.com/connect/qrconnect?appid=wx6634d697e8cc0a29&scope=snsapi_login&response_type=code&redirect_uri=https%3A%2F%2Faccount.sogou.com%2Fconnect%2Fcallback%2Fweixin&state=22a363ff-6f78-4d2a-892c-a969d87da69e&href=https%3A%2F%2Fdlweb.sogoucdn.com%2Fweixin%2Fcss%2Fweixin_join.min.css%3Fv%3D20170315&lang=zh_CN'

#登陆并且获取cookie
login_sogou(house_url)

#运行scrapy项目 将网址替换成自己需要的 关键词网址（买房、保险等）
cmdline.execute('scrapy crawl wechat_article'.split())