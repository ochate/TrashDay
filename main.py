import datetime
# import calendar

trash_day = {
    0: "可燃ごみ",  # 月曜日
    1: "プラごみ",  # 火曜日
    2: "不燃ごみ",  # 水曜日
    3: "可燃ごみ",  # 木曜日
    4: "回収なし",  # 金曜日
    5: "回収なし",  # 土曜日
    6: "回収なし",  # 日曜日
}

# 今日は何曜日かを判定
today = datetime.date.today()
weekday = today.weekday()

for i in range(7):
    if weekday == i:
        print(f'今日は{trash_day[i]}の日')


# 第何週目の何曜日かを判定
# 今月1日が何曜日か調べる
first_day_of_month = datetime.date(today.year, today.month, 1)
