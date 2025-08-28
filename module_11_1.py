import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates


data_conc= {
    'первый ярус фундаментной плиты камеры шлюза': ('18-12-2024', '07-06-2025'),
    'второй ярус фундаментной плиты камеры шлюза': ('15-01-2025', '09-07-2025'),
    'третий ярус фундаментной плиты камеры шлюза': ('03-04-2025', '19-07-2025'),
    'устои 13 секции камеры шлюза': ('04-09-2025', '30-09-2025'),
    'устои 12 секции камеры шлюза': ('10-08-2025', '04-09-2025'),
    'устои 11 секции камеры шлюза': ('24-07-2025', '17-08-2025'),
    'устои 10 секции камеры шлюза': ('06-09-2025', '30-09-2025'),
    'устои 9 секции камеры шлюза': ('10-06-2025', '04-07-2025'),
    'устои 8 секции камеры шлюза': ('18-10-2025', '01-11-2025'),
    'устои 7 секции камеры шлюза': ('02-07-2025', '26-07-2025'),
    'устои 6 секции камеры шлюза': ('28-09-2025', '22-10-2025'),
    'устои 5 секции камеры шлюза': ('01-08-2025', '25-08-2025'),
    'устои 4 секции камеры шлюза': ('19-10-2025', '12-11-2025'),
    'устои 3 секции камеры шлюза': ('31-10-2025', '23-11-2025'),
    'устои 2 секции камеры шлюза': ('19-10-2025', '14-11-2025'),
    'устои 1 секции камеры шлюза': ('01-11-2025', '26-11-2025'),
    'первый ярус НГ отм. 53,000-56,000': ('15-05-2025', '19-06-2025'),
    'второй ярус НГ отм. 56,000-57,500': ('19-06-2025', '31-07-2025'),
    'третий ярус НГ отм. 57,500-59,000': ('01-07-2025', '18-08-2025'),
    'четвёртый ярус отм. 59,000-60,000': ('25-07-2025', '05-09-2025'),
    'пятый ярус НГ отм. 60,000-64,000': ('20-08-2025', '02-10-2025'),
    'шестой ярус НГ отм. 64,000-68,000': ('01-09-2025', '21-10-2025'),
    'седьмой ярус НГ отм. 68,000-72,000': ('01-10-2025', '09-11-2025'),
    'восьмой ярус НГ отм. 72,000-76,000': ('09-10-2025', '28-11-2025'),
    'девятый ярус НГ отм. 76,000-78,100': ('01-11-2025', '16-12-2025'),
}

data_gmo = {
    'левобережная ОВГ': ('12-06-2025', '22-07-2025'),
    'правобережная ОВГ': ('04-06-2025', '14-07-2025'),
    'пазовые конструкции и закладные части ОВГ': ('24-02-2026', '17-05-2026'),
    'гидроприводы и затворы ОВГ': ('18-05-2026', '30-06-2026'),
    'пороги, пазовые конструкции и решётки СУР': ('01-06-2026', '30-06-2026'),
    'пороги и монтажные рамы подпятников, пятовые устройства, первые яруса вертикальных облицовок и монтажных колонн '
    'ОДВ НГ': ('01-10-2025', '10-11-2025'),
    'второй и третий ярусы монтажных колонн ОДВ НГ': ('11-11-2025', '21-11-2025'),
    'вертикальная облицовка ОДВ НГ (2 ярус), подушки закладные (1-4 яруса)': ('22-11-2025', '22-12-2025'),
    'поддерживающие конструкции для сборки створок ОДВ НГ': ('11-11-2025', '30-11-2025'),
    'вертикальная облицовка (3, 4 ярус) ОДВ НГ (2 ярус), подушки закладные (5-9 яруса)': ('23-12-2025', '23-01-2026'),
    'анкера гальсбантов ОДВ НГ': ('24-01-2026', '24-02-2026'),
    'створки ОДВ НГ': ('23-12-2025', '31-05-2026'),
    'гидроприводы и гальсбанты ОДВ НГ': ('01-06-2026', '18-06-2026'),
    'мостик пешеходный ОДВ НГ': ('20-07-2026', '31-07-2026'),
    'уплотнение ОДВ НГ': ('19-06-2026', '05-07-2026'),
    'рама отбойная ОДВ НГ': ('19-06-2026', '19-07-2026'),
    'пороги, колонны кронштейна, кронштейн закладной РДВ НГ': ('01-10-2025', '25-10-2025'),
    'закладные уголки РДВ НГ': ('01-12-2025', '09-12-2025'),
    'колонны подушек, рамы подпятников, пятовые устройства, подушки РДВ НГ': ('23-11-2025', '28-12-2025'),
    'поддерживающие конструкции для сборки створок РДВ НГ': ('01-11-2025', '09-12-2025'),
    'створки РДВ НГ': ('10-12-2025', '18-06-2026'),
    'мостик пешеходный РДВ НГ': ('20-07-2026', '31-07-2026'),
    'уплотнение РДВ НГ': ('19-06-2026', '05-07-2026'),
    'рама отбойная РДВ НГ': ('19-06-2026', '19-07-2026'),
    'приспособление для подъёма створок в ремонтное положение': ('01-08-2026', '28-09-2026'),
    'секция 2 КШ закладные и рым': ('03-02-2026', '03-03-2026'),
    'секция 3 КШ закладные и рым': ('02-01-2026', '02-02-2026'),
    'секция 4 КШ закладные и рым': ('30-11-2025', '30-12-2025'),
    'секция 5 КШ закладные и рым': ('26-08-2025', '26-09-2025'),
    'секция 6 КШ закладные и рым': ('30-10-2025', '30-11-2025'),
    'секция 7 КШ закладные и рым': ('26-07-2025', '26-08-2025'),
    'секция 8 КШ закладные и рым': ('17-11-2025', '17-12-2025'),
    'секция 9 КШ закладные и рым': ('04-07-2025', '04-08-2025'),
    'секция 10 КШ закладные и рым': ('17-10-2025', '17-11-2025'),
    'секция 11 КШ закладные и рым': ('17-08-2025', '17-09-2025'),
    'секция 12 КШ закладные и рым': ('17-09-2025', '17-10-2025'),
    'система майнообразования и льдоотгона': ('19-06-2026', '19-07-2026'),
    'реконструкция двустворчатых ворот 30,0-14,04-13,14': ('03-02-2026', '16-05-2026'),
    'монтаж накатной платформы': ('01-08-2026', '28-09-2026')
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

fig, ax = plt.subplots(dpi=140)


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
                            f'{(end_dates_gmo[i] - start_dates_gmo[i]).days} {days_word}', ha='center', va='center', fontsize=3)

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
                            f'{(end_dates_conc[i] - start_dates_conc[i]).days} {days_word}', ha='center', va='center', fontsize=3)

# Добавляем фиктивные элементы для легенды
ax.barh(-1, 0, height=0, color='tab:blue', label='Устройство бетонных конструкций')
ax.barh(-1, 0, height=0, color='tab:red', label='Монтаж ГМО')
ax.legend(fontsize=8, loc='upper right',frameon=True ,framealpha=1)

# Настройки графика
ax.set_yticks(range(len(event_names_conc + event_names_gmo)))
ax.set_yticklabels(event_names_gmo + event_names_conc)
start_date = min(start_dates_conc) - timedelta(days=10)
ax.set_xlim(left=start_date, right=max(end_dates_gmo) + timedelta(days=10))
ax.set_title('График монтажа ГМО Городецкого гидроузла')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
# Показать график
plt.xticks(rotation=0, fontsize=4)
plt.ylim([-1, len(event_names_conc)+len(event_names_gmo)])
plt.yticks(fontsize=4)
plt.grid(True, which='both', color='black', linewidth=0.5)
plt.subplots_adjust(left=0.38, right=0.98, bottom=0.05, top=0.95)
plt.plot()
plt.show()