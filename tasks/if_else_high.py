# 1 
'''
Робота світлофора для водіїв запрограмована таким чином: на початку кожної години протягом трьох хвилин горить зелений сигнал, потім протягом однієї хвилини - жовтий, потім протягом двох хвилин - червоний, а далі протягом трьох хвилин - знову зелений і т. д. Дано ціле число t, що позначає час у хвилинах, що минув з початку чергової години. Визначити, сигнал якого кольору горить для водіїв в цей момент.

Вхідні дані:

4
3
5
Вихідні дані:

yellow
green
red
'''
def traffic_light(time: int) -> str:
    cyrcle_length = 6
    time_in_cycle = time % cyrcle_length

    if 0 <= time_in_cycle < 3:
        return "green"
    elif 3 <= time_in_cycle < 4:
        return "yellow"
    else:
        return "red"

input_times = int(input("Enter time number: "))


result = traffic_light(input_times)
print(result)

time = 3 % 6
print(time) # 3

time = 4 % 6
print(time) # 4




