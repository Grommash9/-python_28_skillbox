import file_m
# ну оно же и так открывает файл если он не найден
with open('ssd.txt', 'w') as file:
    file.write('s')
# можно сделать так
file_m.open_file('ssasd.txt')
