from dota2 import dota2
from csgo import csgo

price_max = 300  # buff最高价格
price_min = 60  # buff最低价格
craw_page = 20  # 爬取页数
steam_24h_qty_min = 30  # 24h内steam成交数量最小值

if __name__ == "__main__":

    # 表头
    headers = {
        'User-Agent': ''
    }

    # BUFF cookie
    cookie_str = ""
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

    cost_time_dota2 = dota2(headers, cookies, price_max, price_min, craw_page, steam_24h_qty_min)
    cost_time_csgo = csgo(headers, cookies, price_max, price_min, craw_page, steam_24h_qty_min)
    print("dota2:", cost_time_dota2)
    print("https://steamcommunity.com/market/listings/570/")
    print("csgo:", cost_time_csgo)
    print("https://steamcommunity.com/market/listings/730/")
