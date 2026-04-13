from services.openweather_api import get_weather
from services.excel_files import save_to_excel, read_excel
from services.dashboard import render_dashboard
import time

# while True:
#     weather = get_weather("Warszawa")
#     save_to_excel([weather])
#     print("Pobieram i zapisuje dane", weather)
#
#     time.sleep(5)  # cron, dziala z petla while -> zeby aplikacja wykonywala zapytanie do API co 5 sekund ->
#     # odkomentowac while i sformatowac kod

# result = read_excel("weather_data.xlsx")
# print(result)

render_dashboard("lisbon.xlsx")
