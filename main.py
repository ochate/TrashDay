import datetime

today = datetime.date.today()
weekday = today.weekday()

trash_day = {
    0: "可燃ごみ",  # 月曜日
    1: "プラごみ",  # 火曜日
    2: "不燃ごみ",  # 水曜日
    3: "可燃ごみ",  # 木曜日
    4: "なし",      # 金曜日
    5: "なし",      # 土曜日
    6: "なし",      # 日曜日
}

for i in range(7):
    if weekday == i:
        print(f'今日は{trash_day[i]}の日')
