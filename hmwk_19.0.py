team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_2 + score_1
time_avg = (team1_time + team2_time) / tasks_total
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'{team1_name}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'{team2_name}!'
else:
    challenge_result = 'Ничья!'
print('В команде %s участников : %s !' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('Команда {} решила задач: {} !'.format(team2_name, score_2))
print('{} решили задачи за {} c !'.format(team2_name, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: победа команды {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 2)} секунды на задачу!')
