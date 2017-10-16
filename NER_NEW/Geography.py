from translate import google
print(google('hello world',dst = 'zh-CN', proxies = {'http':'127.0.0.1:1080'}))


