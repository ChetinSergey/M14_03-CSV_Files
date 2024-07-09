import csv

name = set()
name_visited = set()
name_want_to_visit = set()
next_city_to_visit = name_want_to_visit


def write_holiday_cities(first_letter):
    with open(file='travel_notes.csv', mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for column in csv_reader:
            print(column)
            if first_letter.lower() in column[0][0].lower():
                for row in column[0].split(','):
                    name.add(row)
                for row in column[1].split(';'):
                    name_visited.add(row)
                for row in column[2].split(';'):
                    name_want_to_visit.add(row)

    with open(file='holiday.csv', mode='w', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(['Имя студента(ки):  ' + str(sorted(name))])
        writer.writerow(['Города, которые посетил(а) студент(ка):  ' + str(sorted(name_visited))])
        writer.writerow(['Города, в которых ещё не был(а):  ' + str(sorted(name_want_to_visit))])
        writer.writerow(['Города, которые хочется посетить:  ' + str(sorted(name_want_to_visit))])
        writer.writerow(['Следующим городом будет:  ' + sorted(next_city_to_visit.difference(name_visited))[0]])


write_holiday_cities(first_letter='R')
