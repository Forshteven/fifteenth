import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.ticker import MultipleLocator, FixedFormatter

data = {
    'первый ярус 1 участка камеры шлюза': ('2025-04-05', '2025-07-05'),
    'второй ярус 1 участка камеры шлюза': ('2025-05-05', '2025-08-05'),
    'третий ярус 1 участка камеры шлюза': ('2025-06-05', '2025-08-05'),
    'стены второй секции 1 участка камеры шлюза': ('2025-06-15', '2025-07-25'),
    'стены третьей секции 1 участка камеры шлюза': ('2025-07-15', '2025-08-25'),
    'стены четвёртой секции 1 участка камеры шлюза': ('2025-06-25', '2025-08-10'),
    'стены пятой секции 1 участка камеры шлюза': ('2025-07-25', '2025-09-10'),
    'стены шестой секции 1 участка камеры шлюза': ('2025-08-25', '2025-10-05'),
    'стены седьмой секции 1 участка камеры шлюза': ('2025-08-15', '2025-09-25'),
    'первый ярус НГ': ('2025-05-05', '2025-07-20'),
    'второй ярус НГ': ('2025-06-05', '2025-09-30'),
    'третий ярус НГ': ('2025-07-25', '2025-10-15'),
    'четвёртый ярус (скольз. опалубка)': ('2025-10-15', '2025-12-15'),
    'четвёртый ярус (ячейки)': ('2025-11-15', '2026-02-15'),
    'пятый ярус': ('2026-01-03','2026-04-10'),
    'шестой ярус': ('2026-02-15', '2026-05-10'),
    'первый ярус 2 участка камеры шлюза': ('2025-07-05', '2025-09-20'),
    'второй ярус 2 участка камеры шлюза': ('2025-07-25', '2025-10-25'),
    'третий ярус 2 участка камеры шлюза': ('2025-08-25', '2025-10-25'),
    'стены восьмой секции 2 участка камеры шлюза': ('2025-12-25', '2026-01-25'),
    'стены девятой секции 2 участка камеры шлюза': ('2025-10-01', '2025-11-10'),
    'стены десятой секции 2 участка камеры шлюза': ('2025-11-01', '2025-12-10'),
    'стены одинадцатой секции 2 участка камеры шлюза': ('2025-10-10', '2025-11-20'),
    'стены двенадцатой секции 2 участка камеры шлюза': ('2025-11-10', '2025-12-15'),
    'стены тринадцатой секции 2 участка камеры шлюза': ('2025-12-05', '2026-01-20'),
    'стены первой секции 2 участка камеры шлюза': ('2025-09-10', '2025-10-20'),
    'левобережная ОВГ': ('2025-05-20', '2025-07-05'),
    'правобережная ОВГ': ('2025-06-25', '2025-08-10'),
    'пазовые конструкции и закладные части ОВГ': ('2026-05-10', '2026-07-10'),
    'гидроприводы и затворы ОВГ': ('2026-07-10', '2026-08-30'),
    'пороги, пазовые конструкции и решётки СУР': ('2026-05-10', '2026-06-10'),
    'пороги и монтажные рамы подпятников ОДВ НГ': ('2025-10-15', '2025-10-30'),
    'вертикальная облицовка, вереяльные колонны, подушки закладные, анкера гальсбантов ОДВ НГ': ('2026-03-25', '2026-05-15'),
    'створки ОДВ НГ': ('2026-04-08', '2026-09-05'),
    'гидроприводы ОДВ НГ': ('2026-09-05', '2026-09-15'),
    'пороги, колонны кронштейна, кронштейн закладной РДВ НГ': ('2025-10-15', '2025-10-30'),
    'закладные уголки, колонны подушек, рамы подпятников, пятовые устройства, подушки РДВ НГ': ('2026-03-15', '2026-03-30'),
    'створки РДВ НГ': ('2026-02-25', '2026-07-15'),
    'приспособление для подъёма створок в ремонтное положение': ('2026-05-10', '2026-08-10'),
    'закладные части плавучих рымов': ('2025-07-25', '2026-02-25'),
    'рым плавучий, швартовые тумбы': ('2026-02-25', '2026-03-30'),
    'система майнообразования и льдоотгона': ('2026-11-15', '2026-12-05'),
    'реконструкция двустворчатых ворот 30,0-14,04-13,14': ('2026-03-30', '2026-05-10'),
    'монтаж накатной платформы': ('2026-06-25', '2026-09-25')
}


def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()

event_names = []
start_dates = []
end_dates = []

for event, dates in data.items():
    start_date, end_date = map(parse_date, dates)
    event_names.append(event)
    start_dates.append(start_date)
    end_dates.append(end_date)

fig, ax = plt.subplots()

width = 0.8

for i, event_name in enumerate(event_names):
    ax.broken_barh([(start_dates[i], end_dates[i] - start_dates[i])],
                   (i - width / 2, width),
                   facecolors=('tab:blue'))

# Настройки графика
ax.set_yticks(range(len(event_names)))
ax.set_yticklabels(event_names)
ax.set_xlim(min(start_dates), max(end_dates))
ax.set_xlabel('Даты')
ax.set_title('График монтажа ГМО Городецкого гидроузла')
ax.xaxis.set_major_locator(MultipleLocator(30))
ax.xaxis.set_minor_locator(MultipleLocator(10))

# Показать график
plt.xticks(rotation=90)
plt.grid(True, which='both', color='black', linewidth=1)
plt.grid(True, which='minor', linestyle=':', color='grey', linewidth=0.5)
plt.show()