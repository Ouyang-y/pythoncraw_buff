import requests
import re
import pandas as pd
import time
from get_steam_text import get_steam_text


def csgo(headers, cookies, price_max, price_min, craw_page, steam_24h_qty_min):
    time_start = time.time()
    # 标准url_steam:https://steamcommunity.com/market/priceoverview/?country=CN&currency=23&appid=730&market_hash_name=Operation%20Wildfire%20Case
    # steam appid=730 为 CSGO
    url = r'https://steamcommunity.com/market/priceoverview/?country=CN&currency=23&appid=730&market_hash_name='

    # 初始化
    name_list = []
    price_list = []
    price_steam_list = []
    sell_num_list = []
    soldprice = []
    percentage = []

    for i in range(craw_page):
        time_page_start = time.time()
        dec = time_page_start - time_start
        minute = int(dec / 60)
        second = dec % 60
        print("%02d:%02d page" % (minute, second), i)
        # 标准url:https://buff.163.com/api/market/goods?game=csgo&page_num=1&min_price=35&max_price=300
        buff_csgo_url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=' + str(
            i + 1) + '&min_price=' + str(price_min) + '&max_price=' + str(price_max)
        buff_csgo_text = requests.get(url=buff_csgo_url, headers=headers, cookies=cookies).text
        print(buff_csgo_text)
        # 饰品名
        names_list_temp = re.findall(r'"steam_market_url": "https://steamcommunity.com/market/listings/730/(.*)",',
                                     buff_csgo_text, re.M)
        # BUFF售价
        price_list_temp = re.findall(r'"sell_min_price": "(.*)",', buff_csgo_text, re.M)

        cleanlist = []
        price_steam_temp = []
        soldprice_temp = []
        percentage_temp = []
        sell_num_list_temp = []
        print("BUFF当前页爬取完成，开始访问steam")
        steam_time = len(names_list_temp)
        # 取steam价格和在售数量
        for k in range(steam_time):
            item = names_list_temp[k]
            try:
                steam_item_text = get_steam_text(url + item)
            except:
                cleanlist.append(k)
                continue
            print(k + 1, "/", steam_time, ":", steam_item_text, item)
            time.sleep(1)
            try:
                steam_24h_qty_temp = int(re.findall(r'"volume":"([0-9]*)",', steam_item_text, re.M)[0])
            except IndexError:
                steam_24h_qty_temp = 0
            if steam_24h_qty_temp < steam_24h_qty_min:
                cleanlist.append(k)
            else:
                try:
                    price_steam_temp0 = re.findall(r'"lowest_price":"¥ ([0-9]*.[0-9]*)",', steam_item_text, re.M)[0]
                    price_steam_temp.append(price_steam_temp0)
                    sell_num_list_temp.append(steam_24h_qty_temp)
                except IndexError:
                    cleanlist.append(k)
        for k in range(len(cleanlist) - 1, -1, -1):
            names_list_temp.pop(cleanlist[k])
            price_list_temp.pop(cleanlist[k])
        for k in range(len(names_list_temp)):
            soldprice_temp0 = float(price_steam_temp[k]) / 1.15
            percentage_temp0 = float(price_list_temp[k]) / soldprice_temp0
            soldprice_temp.append(soldprice_temp0)
            percentage_temp.append(percentage_temp0)
        # 饰品名
        name_list.extend(names_list_temp)
        # BUFF价格
        price_list.extend(price_list_temp)
        # steam价格
        price_steam_list.extend(price_steam_temp)
        # steam 24小时销售数量
        sell_num_list.extend(sell_num_list_temp)
        # 按steam市场最低价售出税后价格
        soldprice.extend(soldprice_temp)
        # 折值
        percentage.extend(percentage_temp)
        time_page_end = time.time()
        dec = time_page_end - time_page_start
        minute = int(dec / 60)
        second = dec % 60
        print("page_cost: %02dmin%02dsec" % (minute, second))
        # print(names_list_temp)
        # print(price_list_temp)
        # print(price_steam_temp)
        # print(sell_num_list_temp)
    # 汇合信息写成表格并保存
    csv_name = ["name", "BUFF price", "steam price", "steam 24hour sold qty", "steam sellprice", "percentage"]
    csv_data = zip(name_list, price_list, price_steam_list, sell_num_list, soldprice, percentage)
    items_information = pd.DataFrame(columns=csv_name, data=csv_data)
    items_information.to_csv("csgo.csv")
    time_end = time.time()
    dec = time_end - time_start
    minute = int(dec / 60)
    second = dec % 60
    return "总用时：%02d分%02d秒" % (minute, second)
