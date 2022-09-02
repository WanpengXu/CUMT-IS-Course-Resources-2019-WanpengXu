postcode={"北京":100000,"天津":300000,"重庆":401400,"济南":250000,"南京":210000,"西安":710000,"郑州":450000,"长沙":410000,"武汉":430000}
while True:
    city=input()
    if city=="exit" :
        break
    print(postcode[city])
