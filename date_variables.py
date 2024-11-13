import datetime

# Get the current date
today = datetime.datetime.today()
week_num = today.isocalendar()[1]
 
# Get all needed dates for alerts
today = datetime.date.today()
formatted_date = today.strftime("%Y-%m-%d")

today_plus_fourteen = today + datetime.timedelta(days=14)
formatted_date_fourteen = today_plus_fourteen.strftime("%Y-%m-%d")

today_plus_fourteen_minus_one = today + datetime.timedelta(days=13)
formatted_date_fourteen_minus_one = today_plus_fourteen_minus_one.strftime("%Y-%m-%d")

today_plus_seven = today + datetime.timedelta(days=7)
formatted_date_seven = today_plus_seven.strftime("%Y-%m-%d")

today_minus_thirty = today + datetime.timedelta(days=-30)
formatted_date_minus_thirty = today_minus_thirty.strftime("%Y-%m-%d")

today_minus_seven = today + datetime.timedelta(days=-7)
formatted_date_minus_seven = today_minus_seven.strftime("%Y-%m-%d")

today_minus_one = today + datetime.timedelta(days=-1)
formatted_date_minus_one = today_minus_one.strftime("%Y-%m-%d")

today_plus_one = today + datetime.timedelta(days=1)
formatted_date_one = today_plus_one.strftime("%Y-%m-%d")

today_minus_three = today + datetime.timedelta(days=-3)
formatted_date_minus_three = today_minus_three.strftime("%Y-%m-%d")

today_minus_twenty = today + datetime.timedelta(days=-20)
formatted_date_minus_twenty = today_minus_twenty.strftime("%Y-%m-%d")

# Week number
week_num = today.isocalendar()[1]
# Last week number
last_week_num = today_minus_seven.isocalendar()[1]
# Next week number
next_week_num = today_plus_fourteen_minus_one.isocalendar()[1]


formatted_date_minus_three ,formatted_date, formatted_date_one, formatted_date_seven, formatted_date_fourteen_minus_one, formatted_date_minus_seven, formatted_date_minus_thirty, formatted_date_fourteen,\
   last_week_num, week_num, next_week_num
