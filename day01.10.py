import hashlib
email = input ("请输入你的邮箱：")
hash = hashlib.md5()
hash.update(email.encode('utf-8')) 
res = hash.hexdigest()
print(res)

