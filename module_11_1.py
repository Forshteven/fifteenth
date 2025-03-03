import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates


data_conc= {
    'первый ярус фундаментной плиты камеры шлюза': ('18-12-2024', '12-05-2025'),
    'второй ярус фундаментной плиты камеры шлюза': ('27-02-2025', '22-06-2025'),
    'третий ярус фундаментной плиты камеры шлюза': ('20-03-2025', '15-06-2025'),
    'стены камеры шлюза': ('02-04-2025', '14-10-2025'),
    'первый ярус НГ блок I-1': ('31-03-2025', '30-04-2025'),
    'первый ярус НГ блок I-2': ('03-04-2025', '05-05-2025'),
    'первый ярус НГ блок I-3': ('22-04-2025', '18-05-2025'),
    'первый ярус НГ блок I-4': ('21-04-2025', '17-05-2025'),
    'первый ярус НГ блок I-5': ('03-04-2025', '26-04-2025'),
    'первый ярус НГ блок I-6': ('14-04-2025', '24-04-2025'),
    'первый ярус НГ блок I-7': ('07-05-2025', '17-05-2025'),
    'первый ярус НГ блок I-8': ('07-05-2025', '17-05-2025'),
    'второй ярус НГ блок II-1': ('03-06-2025', '03-07-2025'),
    'второй ярус НГ блок II-2': ('01-05-2025', '30-05-2025'),
    'второй ярус НГ блок II-3': ('10-05-2025', '11-06-2025'),
    'второй ярус НГ блок II-4': ('15-06-2025', '15-07-2025'),
    'третий ярус НГ блок III-1-1': ('15-06-2025', '03-07-2025'),
    'третий ярус НГ блок III-1-2': ('09-06-2025', '27-06-2025'),
    'третий ярус НГ блок III-1-3': ('15-06-2025', '03-07-2025'),
    'третий ярус НГ блок III-1-4': ('09-06-2025', '27-06-2025'),
    'третий ярус НГ блок III-2': ('13-07-2025', '31-07-2025'),
    'третий ярус НГ блок III-3': ('01-07-2025', '19-07-2025'),
    'третий ярус НГ блок III-4': ('28-05-2025', '15-06-2025'),
    'третий ярус НГ блок III-5': ('03-06-2025', '21-06-2025'),
    'демонтаж распорной системы НГ': ('16-07-2025', '25-07-2025'),
    'четвёртый ярус НГ (скольз. опалубка) блок IV-3-1': ('26-07-2025', '29-08-2025'),
    'четвёртый ярус НГ (скольз. опалубка) блок IV-3-2': ('26-07-2025', '29-08-2025'),
    'четвёртый ярус НГ (скольз. опалубка) блок IV-3-3': ('25-08-2025', '28-09-2025'),
    'четвёртый ярус НГ (скольз. опалубка) блок IV-3-4': ('25-08-2025', '28-09-2025'),
    'четвёртый ярус НГ (ячейки)': ('29-08-2025', '02-12-2025'),
    'пятый ярус НГ': ('18-10-2025', '17-01-2026'),
    'шестой ярус НГ': ('31-10-2025', '18-02-2026'),
}

data_gmo = {
    'левобережная ОВГ': ('20-04-2025', '30-05-2025'),
    'правобережная ОВГ': ('08-05-2025', '15-06-2025'),
    'пазовые конструкции и закладные части ОВГ': ('18-02-2026', '18-03-2026'),
    'гидроприводы и затворы ОВГ': ('18-03-2026', '30-04-2026'),
    'пороги, пазовые конструкции и решётки СУР': ('18-02-2026', '18-03-2026'),
    'пороги и монтажные рамы подпятников ОДВ НГ': ('31-07-2025', '25-08-2025'),
    'пятовые устройства и первые два яруса вереяльных колонн ОДВ НГ': ('29-09-2025', '31-10-2025'),
    'вертикальная облицовка ОДВ НГ (1 ярус), подушки закладные (1-4 яруса)': ('31-10-2025', '30-11-2025'),
    'поддерживающие конструкции для сборки створок ОДВ НГ': ('01-12-2025', '15-12-2025'),
    'вертикальная облицовка ОДВ НГ (2 ярус), подушки закладные (5-8 яруса)': ('19-02-2026', '20-03-2026'),
    'анкера гальсбантов ОДВ НГ': ('21-03-2026', '20-04-2026'),
    'створки ОДВ НГ': ('15-12-2025', '25-04-2026'),
    'гидроприводы ОДВ НГ': ('25-04-2026', '10-05-2026'),
    'пороги, колонны кронштейна, кронштейн закладной РДВ НГ': ('03-07-2025', '31-07-2025'),
    'закладные уголки': ('29-09-2025', '10-10-2025'),
    'колонны подушек, рамы подпятников, пятовые устройства, подушки РДВ НГ': ('11-10-2025', '15-11-2025'),
    'поддерживающие конструкции для сборки створок РДВ НГ': ('16-11-2025', '01-12-2025'),
    'створки РДВ НГ': ('01-12-2025', '25-04-2026'),
    'приспособление для подъёма створок в ремонтное положение': ('19-02-2026', '31-03-2026'),
    'закладные части плавучих рымов': ('14-05-2025', '14-11-2025'),
    'рым плавучий, швартовые тумбы': ('14-06-2025', '20-11-2025'),
    'система майнообразования и льдоотгона': ('26-04-2026', '20-05-2026'),
    'реконструкция двустворчатых ворот 30,0-14,04-13,14': ('20-02-2026', '30-03-2026'),
    'монтаж накатной платформы': ('30-03-2026', '20-05-2026')
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

fig, ax = plt.subplots()


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
                            f'{(end_dates_gmo[i] - start_dates_gmo[i]).days} {days_word}', ha='center', va='center', fontsize=5)

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
                            f'{(end_dates_conc[i] - start_dates_conc[i]).days} {days_word}', ha='center', va='center', fontsize=5)

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
plt.xticks(rotation=90, fontsize=8)
plt.yticks(fontsize=8)
plt.grid(True, which='both', color='black', linewidth=1)
plt.grid(True, which='minor', linestyle=':', color='grey', linewidth=0.5)
plt.plot()
plt.show()