import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates


data_conc= {
    'первый ярус фундаментной плиты камеры шлюза': ('18-12-2024', '19-06-2025'),
    'второй ярус фундаментной плиты камеры шлюза': ('15-01-2025', '09-07-2025'),
    'третий ярус фундаментной плиты камеры шлюза': ('03-04-2025', '19-07-2025'),
    'устои 13 секции камеры шлюза': ('27-08-2025', '04-10-2025'),
    'устои 12 секции камеры шлюза': ('03-08-2025', '09-09-2025'),
    'устои 11 секции камеры шлюза': ('09-07-2025', '16-08-2025'),
    'устои 10 секции камеры шлюза': ('09-07-2025', '16-08-2025'),
    'устои 9 секции камеры шлюза': ('16-04-2025', '27-05-2025'),
    'устои 8 секции камеры шлюза': ('15-05-2025', '24-06-2025'),
    'устои 7 секции камеры шлюза': ('14-05-2025', '24-06-2025'),
    'устои 6 секции камеры шлюза': ('17-06-2025', '22-07-2025'),
    'устои 5 секции камеры шлюза': ('11-06-2025', '22-07-2025'),
    'устои 4 секции камеры шлюза': ('21-09-2025', '28-10-2025'),
    'устои 3 секции камеры шлюза': ('27-08-2025', '04-10-2025'),
    'устои 2 секции камеры шлюза': ('27-07-2025', '09-09-2025'),
    'устои 1 секции камеры шлюза': ('21-09-2025', '28-10-2025'),
    'первый ярус НГ отм. 53,000-56,000': ('15-05-2025', '19-06-2025'),
    'второй ярус НГ отм. 56,000-57,500': ('19-06-2025', '31-07-2025'),
    'третий ярус НГ отм. 57,500-59,000': ('31-07-2025', '18-08-2025'),
    'четвёртый ярус отм. 59,000-60,000': ('18-08-2025', '05-09-2025'),
    'пятый ярус НГ отм. 60,000-64,000': ('05-09-2025', '02-10-2025'),
    'шестой ярус НГ отм. 64,000-68,000': ('02-10-2025', '21-10-2025'),
    'седьмой ярус НГ отм. 68,000-72,000': ('21-10-2025', '09-11-2025'),
    'восьмой ярус НГ отм. 72,000-76,000': ('09-11-2025', '28-11-2025'),
    'девятый ярус НГ отм. 76,000-78,100': ('28-11-2025', '16-12-2025'),
}

data_gmo = {
    'левобережная ОВГ': ('04-06-2025', '14-07-2025'),
    'правобережная ОВГ': ('25-06-2025', '04-08-2025'),
    'пазовые конструкции и закладные части ОВГ': ('01-04-2026', '01-05-2026'),
    'гидроприводы и затворы ОВГ': ('01-05-2026', '10-06-2026'),
    'пороги, пазовые конструкции и решётки СУР': ('10-05-2026', '10-06-2026'),
    'пороги и монтажные рамы подпятников ОДВ НГ': ('14-07-2025', '08-08-2025'),
    'пятовые устройства и первые два яруса вереяльных колонн ОДВ НГ': ('12-11-2025', '12-12-2025'),
    'вертикальная облицовка ОДВ НГ (1 ярус), подушки закладные (1-4 яруса)': ('12-12-2025', '12-01-2026'),
    'поддерживающие конструкции для сборки створок ОДВ НГ': ('12-01-2026', '25-01-2026'),
    'вертикальная облицовка ОДВ НГ (2 ярус), подушки закладные (5-8 яруса)': ('04-04-2026', '04-05-2026'),
    'анкера гальсбантов ОДВ НГ': ('04-05-2026', '04-06-2026'),
    'створки ОДВ НГ': ('25-01-2026', '04-06-2026'),
    'гидроприводы и гальсбанты ОДВ НГ': ('04-06-2026', '10-06-2026'),
    'мостик пешеходный ОДВ НГ': ('10-07-2026', '22-07-2026'),
    'уплотнение ОДВ НГ': ('10-06-2026', '28-06-2026'),
    'рама отбойная ОДВ НГ': ('10-06-2026', '10-07-2026'),
    'пороги, колонны кронштейна, кронштейн закладной РДВ НГ': ('17-08-2025', '11-09-2025'),
    'закладные уголки РДВ НГ': ('12-11-2025', '23-11-2025'),
    'колонны подушек, рамы подпятников, пятовые устройства, подушки РДВ НГ': ('23-11-2025', '28-12-2025'),
    'поддерживающие конструкции для сборки створок РДВ НГ': ('28-12-2025', '15-01-2026'),
    'створки РДВ НГ': ('15-01-2026', '10-06-2026'),
    'мостик пешеходный РДВ НГ': ('10-07-2026', '22-07-2026'),
    'уплотнение РДВ НГ': ('10-06-2026', '28-06-2026'),
    'рама отбойная РДВ НГ': ('10-06-2026', '10-07-2026'),
    'приспособление для подъёма створок в ремонтное положение': ('22-07-2026', '07-09-2026'),
    'секция 2 КШ закладные и рым': ('15-10-2025', '15-11-2025'),
    'секция 3 КШ закладные и рым': ('15-11-2025', '15-12-2025'),
    'секция 4 КШ закладные и рым': ('15-12-2025', '15-01-2026'),
    'секция 5 КШ закладные и рым': ('04-08-2025', '04-09-2025'),
    'секция 6 КШ закладные и рым': ('28-07-2025', '28-08-2025'),
    'секция 7 КШ закладные и рым': ('28-06-2025', '28-07-2025'),
    'секция 8 КШ закладные и рым': ('28-06-2025', '28-07-2025'),
    'секция 9 КШ закладные и рым': ('28-05-2025', '28-06-2025'),
    'секция 10 КШ закладные и рым': ('28-07-2025', '28-08-2025'),
    'секция 11 КШ закладные и рым': ('28-08-2025', '28-09-2025'),
    'секция 12 КШ закладные и рым': ('28-08-2025', '28-09-2025'),
    'система майнообразования и льдоотгона': ('10-06-2026', '10-07-2026'),
    'реконструкция двустворчатых ворот 30,0-14,04-13,14': ('25-01-2026', '04-04-2026'),
    'монтаж накатной платформы': ('22-07-2026', '07-09-2026')
}


def parse_date(date_str):
    return datetime.strptime(date_str, '%d-%m-%Y').date()

# def sort_key(e):
#     for start_date in e[1]:
#         return parse_date(start_date)

event_names_conc = []
start_dates_conc = []
end_dates_conc = []
event_names_gmo = []
start_dates_gmo = []
end_dates_gmo = []


for event, dates in reversed(data_conc.items()):
    start_date, end_date = map(parse_date, dates)
    event_names_conc.append(event)
    start_dates_conc.append(start_date)
    end_dates_conc.append(end_date)

for event, dates in reversed(data_gmo.items()):
    start_date, end_date = map(parse_date, dates)
    event_names_gmo.append(event)
    start_dates_gmo.append(start_date)
    end_dates_gmo.append(end_date)

fig, ax = plt.subplots(figsize=(30,20))


width = 0.5

for i, events in enumerate(event_names_gmo):
    color = 'tab:red'
    ax.broken_barh([(start_dates_gmo[i], end_dates_gmo[i] - start_dates_gmo[i])],
                   (i - width / 2, width),
                   facecolors=color)
    days_word = 'день' if int((end_dates_gmo[i] - start_dates_gmo[i]).days) % 10 == 1 and int((end_dates_gmo[i] - start_dates_gmo[i]).days) != 11 \
        else ('дня' if int((end_dates_gmo[i] - start_dates_gmo[i]).days) % 10 in range(2, 5) and int((end_dates_gmo[i] - start_dates_gmo[i]).days)
        not in range(11, 16) else 'дней')
    x_text = start_dates_gmo[i] + (end_dates_gmo[i] - start_dates_gmo[i])/2
    y_text = i + 0.5
    ax.text(x_text, y_text, f'{start_dates_gmo[i].strftime("%d-%m-%Y")} - {end_dates_gmo[i].strftime("%d-%m-%Y")}, '
                            f'{(end_dates_gmo[i] - start_dates_gmo[i]).days} {days_word}', ha='center', va='center', fontsize=4)

for i, events in enumerate(event_names_conc):
    color = 'tab:blue'
    ax.broken_barh([(start_dates_conc[i], end_dates_conc[i] - start_dates_conc[i])],
                   (i - width / 2 + len(event_names_gmo), width),
                   facecolors=color)
    days_word = 'день' if int((end_dates_conc[i] - start_dates_conc[i]).days) % 10 == 1 and int((end_dates_conc[i] - start_dates_conc[i]).days) != 11 \
        else ('дня' if int((end_dates_conc[i] - start_dates_conc[i]).days) % 10 in range(2, 5) and int((end_dates_conc[i] - start_dates_conc[i]).days)
        not in range(11, 16) else 'дней')
    x_text = start_dates_conc[i] + (end_dates_conc[i] - start_dates_conc[i])/2
    y_text = i + len(event_names_gmo) + 0.5
    ax.text(x_text, y_text, f'{start_dates_conc[i].strftime("%d-%m-%Y")} - {end_dates_conc[i].strftime("%d-%m-%Y")}, '
                            f'{(end_dates_conc[i] - start_dates_conc[i]).days} {days_word}', ha='center', va='center', fontsize=4)

# Добавляем фиктивные элементы для легенды
ax.barh(-1, 0, height=0, color='tab:blue', label='Устройство бетонных конструкций')
ax.barh(-1, 0, height=0, color='tab:red', label='Монтаж ГМО')
ax.legend(fontsize=8, loc='upper right',frameon=True ,framealpha=1)

# Настройки графика
ax.set_yticks(range(len(event_names_conc + event_names_gmo)))
ax.set_yticklabels(event_names_gmo + event_names_conc)
start_date = datetime(2024, 12, 10)
ax.set_xlim(left=start_date, right=max(end_dates_gmo))
ax.set_title('График монтажа ГМО Городецкого гидроузла')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
# Показать график
plt.xticks(rotation=0, fontsize=5)
plt.ylim([-1, len(event_names_conc)+len(event_names_gmo)])
plt.yticks(fontsize=5)
plt.grid(True, which='both', color='black', linewidth=0.5)
plt.subplots_adjust(left=0.22, right=0.98, bottom=0.05, top=0.95)
plt.plot()
plt.show()