from school_api import SchoolClient
# 实例化一个用户
school = SchoolClient(url='http://jw1.gdsdxy.cn:81/')
student = school.user_login('','',timeout=20,use_cookie_login=False)
# 获取最新的 【个人课表】
schedule_data = student.get_schedule()
# 获取 第5周，周三的课表
week_num = 5
what_day = 2
day_schedule = schedule_data['schedule'][what_day - 1]
for section_schedule in day_schedule:
    for schedule in section_schedule:
        if week_num in schedule['weeks_arr']:  # 过滤周数
            print(schedule['name'],schedule['teacher'],schedule['time'],schedule['place'],sep=',')#time  place