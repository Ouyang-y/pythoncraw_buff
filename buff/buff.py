from dota2 import dota2
from csgo import csgo

price_max = 300  # buff最高价格
price_min = 60  # buff最低价格
craw_page = 20  # 爬取页数
steam_24h_qty_min = 30  # 24h内steam成交数量最小值

if __name__ == "__main__":

    # 表头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52 '
    }

    # BUFF cookie
    cookie_str = "Device-Id=yFZJ64QHkCtznv0xgxqY; _ga=GA1.2.1833906180.1599195822; " \
                 "nts_mail_user=DICD2019@163.com:-1:1; mail_psc_fingerprint=7238c1c3a37dc7de06d91c993da5de4f; " \
                 "_ntes_nnid=204e0e32fcaf713d9e9d6b19d4ef2b0a,1602601777306; " \
                 "_ntes_nuid=204e0e32fcaf713d9e9d6b19d4ef2b0a; Locale-Supported=zh-Hans; game=csgo; " \
                 "_gid=GA1.2.1771289923.1607237138; _gat_gtag_UA_109989484_1=1; " \
                 "NTES_YD_SESS" \
                 "=0bkZmUIckOuadyZH4ANyRZ86ZjfaGNDBQJMSPezIaal4O1zGOBYERD2ySM4Nly5wzk_tKUELzk" \
                 "CE5u9QrH_I9jgiDjRNCyLQkUZ9tXsNTYPXX7wk4yAWo4codnYn1snGp0YGhNX.aRhch1WVBO3m.Q8" \
                 "BWD52raAlZ2eVqJ3UtNzl26FL9m7TV2ap_aWBEG322aSgoCX4grWpp2KelKJeIrfsbmbvbLVaoWexw" \
                 "gW39j89k; S_INFO=1607237155|0|3&80##|18581573728; P_INFO=18581573728|1607237155" \
                 "|1|netease_buff|00&99|null&null&null#jil&220100#10#0|&0|null|18581573728; reme" \
                 "mber_me=U1093767863|xqcEQWjkFCOASBlQWEG6CLNXn2zOy71r; session=1-lpl_QThXkALNQM6" \
                 "XQ8_VBNy9Qg1lNoFnfnqR_itRbdwP2046758383; csrf_token=IjE0MzFmZTZkNGJiZDA2YWIyMGFlM" \
                 "GI0ZjUzODRiMTQxZDYzYmIxMzIi.Eq4PqA.ss5yNERSwpiXMoKigepZCnQtKUI "
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
