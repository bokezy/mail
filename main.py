# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = ''
password = ''
# 收信方邮箱
to_addr = '2334769547@qq.com'
# 发信服务器
smtp_server = 'smtp.qq.com'
TXT=''
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText(TXT, 'plain', 'utf-8')
# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('从前有五座山')
# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(host=smtp_server)
server.connect(host=smtp_server,port=465)
#smtplib.SMTP_SSL(host=smtp_server ).connect(host=smtp_server , port=465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()