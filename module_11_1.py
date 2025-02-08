import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

data_conc= {
    'первый ярус 1 участка камеры шлюза': ('05-04-2025', '05-07-2025'),
    'второй ярус 1 участка камеры шлюза': ('05-05-2025', '05-08-2025'),
    'третий ярус 1 участка камеры шлюза': ('05-06-2025', '05-08-2025'),
    'стены второй секции 1 участка камеры шлюза': ('15-06-2025', '25-07-2025'),
    'стены третьей секции 1 участка камеры шлюза': ('15-07-2025', '25-08-2025'),
    'стены четвёртой секции 1 участка камеры шлюза': ('25-06-2025', '10-08-2025'),
    'стены пятой секции 1 участка камеры шлюза': ('25-07-2025', '10-09-2025'),
    'стены шестой секции 1 участка камеры шлюза': ('25-08-2025', '05-10-2025'),
    'стены седьмой секции 1 участка камеры шлюза': ('15-08-2025', '25-09-2025'),
    'первый ярус НГ': ('05-05-2025', '20-07-2025'),
    'второй ярус НГ': ('05-06-2025', '30-09-2025'),
    'третий ярус НГ': ('25-07-2025', '15-10-2025'),
    'четвёртый ярус (скольз. опалубка)': ('15-10-2025', '15-12-2025'),
    'четвёртый ярус (ячейки)': ('15-11-2025', '15-02-2026'),
    'пятый ярус': ('03-01-2026', '10-04-2026'),
    'шестой ярус': ('15-02-2026', '10-05-2026'),
    'первый ярус 2 участка камеры шлюза': ('05-07-2025', '20-09-2025'),
    'второй ярус 2 участка камеры шлюза': ('25-07-2025', '25-10-2025'),
    'третий ярус 2 участка камеры шлюза': ('25-08-2025', '25-10-2025'),
    'стены восьмой секции 2 участка камеры шлюза': ('25-12-2025', '25-01-2026'),
    'стены девятой секции 2 участка камеры шлюза': ('01-10-2025', '10-11-2025'),
    'стены десятой секции 2 участка камеры шлюза': ('01-11-2025', '10-12-2025'),
    'стены одинадцатой секции 2 участка камеры шлюза': ('10-10-2025', '20-11-2025'),
    'стены двенадцатой секции 2 участка камеры шлюза': ('10-11-2025', '15-12-2025'),
    'стены тринадцатой секции 2 участка камеры шлюза': ('05-12-2025', '20-01-2026'),
    'стены первой секции 2 участка камеры шлюза': ('20-09-2025', '20-10-2025')
}

data_gmo = {
    'левобережная ОВГ': ('20-05-2025', '05-07-2025'),
    'правобережная ОВГ': ('25-06-2025', '10-08-2025'),
    'пазовые конструкции и закладные части ОВГ': ('10-05-2026', '10-07-2026'),
    'гидроприводы и затворы ОВГ': ('10-07-2026', '30-08-2026'),
    'пороги, пазовые конструкции и решётки СУР': ('10-05-2026', '10-06-2026'),
    'пороги и монтажные рамы подпятников ОДВ НГ': ('15-10-2025', '30-10-2025'),
    'вертикальная облицовка, вереяльные колонны, подушки закладные, анкера гальсбантов ОДВ НГ': ('25-03-2026', '15-05-2026'),
    'створки ОДВ НГ': ('08-04-2026', '05-09-2026'),
    'гидроприводы ОДВ НГ': ('05-09-2026', '15-09-2026'),
    'пороги, колонны кронштейна, кронштейн закладной РДВ НГ': ('15-10-2025', '30-10-2025'),
    'закладные уголки, колонны подушек, рамы подпятников, пятовые устройства, подушки РДВ НГ': ('15-03-2026', '30-03-2026'),
    'створки РДВ НГ': ('25-02-2026', '15-07-2026'),
    'приспособление для подъёма створок в ремонтное положение': ('10-05-2026', '10-08-2026'),
    'закладные части плавучих рымов': ('25-07-2026', '25-02-2026'),
    'рым плавучий, швартовые тумбы': ('25-02-2026', '30-03-2026'),
    'система майнообразования и льдоотгона': ('15-07-2026', '05-08-2026'),
    'реконструкция двустворчатых ворот 30,0-14,04-13,14': ('30-03-2026', '10-05-2026'),
    'монтаж накатной платформы': ('25-06-2026', '25-09-2026')
}


def parse_date(date_str):
    return datetime.strptime(date_str, '%d-%m-%Y').date()

def sort_key(e):
    for start_date in e[1]:
        return parse_date(start_date)

event_names_conc = []
start_dates_conc = []
end_dates_conc = []
event_names_gmo = []
start_dates_gmo = []
end_dates_gmo = []


for event, dates in sorted(data_conc.items(), key=sort_key, reverse=True):
    start_date, end_date = map(parse_date, dates)
    event_names_conc.append(event)
    start_dates_conc.append(start_date)
    end_dates_conc.append(end_date)

for event, dates in sorted(data_gmo.items(), key=sort_key, reverse=True):
    start_date, end_date = map(parse_date, dates)
    event_names_gmo.append(event)
    start_dates_gmo.append(start_date)
    end_dates_gmo.append(end_date)

fig, ax = plt.subplots()

width = 0.5

for i, events in enumerate(event_names_gmo):
    color = 'tab:blue' 
    ax.broken_barh([(start_dates_gmo[i], end_dates_gmo[i] - start_dates_gmo[i])],
                   (i - width / 2, width),
                   facecolors=color)
    days_word = 'день' if int((end_dates_gmo[i] - start_dates_gmo[i]).days) % 10 == 1 and int((end_dates_gmo[i] - start_dates_gmo[i]).days) != 11 \
        else ('дня' if int((end_dates_gmo[i] - start_dates_gmo[i]).days) % 10 in range(2, 5) and int((end_dates_gmo[i] - start_dates_gmo[i]).days)
        not in range(11, 16) else 'дней')
    x_text = start_dates_gmo[i] + (end_dates_gmo[i] - start_dates_gmo[i])/2
    y_text = i + 0.5
    ax.text(x_text, y_text, f'{start_dates_gmo[i].strftime("%d-%m-%Y")} - {end_dates_gmo[i].strftime("%d-%m-%Y")}, '
                            f'{(end_dates_gmo[i] - start_dates_gmo[i]).days} {days_word}', ha='center', va='center', fontsize=5)

for i, events in enumerate(event_names_conc):
    color = 'tab:red'
    ax.broken_barh([(start_dates_conc[i], end_dates_conc[i] - start_dates_conc[i])],
                   (len(event_names_gmo), width),
                   facecolors=color)
    days_word = 'день' if int((end_dates_conc[i] - start_dates_conc[i]).days) % 10 == 1 and int((end_dates_conc[i] - start_dates_conc[i]).days) != 11 \
        else ('дня' if int((end_dates_conc[i] - start_dates_conc[i]).days) % 10 in range(2, 5) and int((end_dates_conc[i] - start_dates_conc[i]).days)
        not in range(11, 16) else 'дней')
    x_text = start_dates_conc[i] + (end_dates_conc[i] - start_dates_conc[i])/2
    y_text = i + 0.5
    ax.text(x_text, y_text, f'{start_dates_conc[i].strftime("%d-%m-%Y")} - {end_dates_conc[i].strftime("%d-%m-%Y")}, '
                            f'{(end_dates_conc[i] - start_dates_conc[i]).days} {days_word}', ha='center', va='center', fontsize=5)

# Добавляем фиктивные элементы для легенды
ax.barh(-1, 0, height=0, color='tab:blue', label='Устройство бетонных конструкций')
ax.barh(-1, 0, height=0, color='tab:red', label='Монтаж ГМО')
ax.legend(fontsize=8, loc='upper right',frameon=True ,framealpha=1)

# Настройки графика
ax.set_yticks(range(len(event_names_conc + event_names_gmo)))
ax.set_yticklabels(event_names_conc + event_names_gmo)
start_date = datetime(2025, 4, 1)
ax.set_xlim(left=start_date, right=max(event_names_conc + event_names_gmo))
ax.set_title('График монтажа ГМО Городецкого гидроузла')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
# Показать график
plt.xticks(rotation=90, fontsize=8)
plt.yticks( fontsize=8)
plt.grid(True, which='both', color='black', linewidth=1)
plt.grid(True, which='minor', linestyle=':', color='grey', linewidth=0.5)
plt.plot()
plt.show()