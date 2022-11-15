print(2+5)
print('Good bye')
print(4.0+1)
print(7/2)
print(6/2)
print(8 / 2)
print(8.0 // 2)
print(round(3.22,2))

print('\'응답하라 1988\'은 많은 시청자들에게 사랑을 받은 드라마예요.데카르트는 "나는 생각한다. 고로 존재한다."라고 말했다.')


print(10 /(10%6))
print(10%6)

print(2**3.0)
print(2*(3+1))

year = 2022
month = 10
day = 29

print('오늘은 {}년 {}월 {}일'.format(year,month,day))

day_string = '오늘은 {}년 {}월 {}일'

print(day_string.format(year,month,day+1))


name = "최지웅"
age = 32

print("제 이름은 %s이고 %d살입니다." % (name, age))
print(f"제 이름은 {name}이고 {age}살입니다.")


wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5, "달러"))  # 코드를 채워 넣으세요.

# "1시간에 5710.8원 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1 * exchange_rate, "원"))  # 코드를 채워 넣으세요.

# "5시간에 28554.0원 벌었습니다." 출력
print("{}시간에 {:0.1f}{} 벌었습니다.".format(5, wage * 5 * exchange_rate, "원"))  # 코드를 채워 넣으세요.


