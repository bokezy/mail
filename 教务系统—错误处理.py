# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from school_api import SchoolClient
from school_api.exceptions import SchoolException, LoginException, IdentityException
from datetime import datetime
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 将use_ex_handle 设置为False时，模块将抛出异常信息。
school = SchoolClient('http://jw1.gdsdxy.cn:81/', use_ex_handle=False)
# 异常处理装饰器
def service_resp():
    def decorator(func):
        def warpper(*args, **kwargs):
            try:
                client = school.user_login(*args, **kwargs)
                data = func(client)
            except IdentityException as reqe:
                # 账号密码错误
                return {'error': reqe}
            except LoginException as reqe:
                # 登录失败 (包含以上错误)
                return {'error': reqe}
            except SchoolException as reqe:
                # 请求失败 (包含以上错误)
                return {'error': reqe}
            except Exception:
                # 模块报错 (包含以上错误)
                return {'error': '教务请求失败'}
            else:
                # 数据处理 (如：缓存)
                return data

        return warpper
    return decorator


def  eail(txt):
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '2334769547@qq.com'
    password = ''

    # from_addr = ''
    # password = '123456789zy'

    # 收信方邮箱
    to_addr = '2334769547@qq.com'
    # 发信服务器
    smtp_server = 'smtp.qq.com'
    TXT = ''
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(txt, 'plain', 'utf-8')
    # 邮件头信
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('从前有五座山')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(host=smtp_server)
    server.connect(host=smtp_server, port=465)
    # smtplib.SMTP_SSL(host=smtp_server ).connect(host=smtp_server , port=465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
@service_resp()
def bind_account(user):
    # 绑定用户，并保存用户信息
    return user.get_info()
@service_resp()
def get_schedule(user):
    # 获取课表
    return user.get_schedule()
@service_resp()
def get_score(user):
    # 获取成绩
    return user.get_score()
if __name__ == '__main__':
    account = '181210243'
    password = '440882199802104057'
    data =get_schedule(account, password, use_cookie_login=False)
    while len(data)==1:
        data = get_schedule(account, password, use_cookie_login=False)
    dayOfWeek = datetime.now().isoweekday()
    week_num = 5
    what_day = dayOfWeek
    txt='郑杨同学今天的课程：\n'
    rr=''
    ee=''
    day_schedule = data['schedule'][what_day - 1]
    for section_schedule in day_schedule:
        for schedule in section_schedule:
            #if week_num in schedule['weeks_arr']:  # 过滤周数
            print(schedule['name'], schedule['teacher'], schedule['time'], schedule['place'],sep=',')  # time  place
            ee=schedule['name']+schedule['teacher']+schedule['time']+schedule['place']+'\n'
            rr=rr+ee
    eail(txt+rr)