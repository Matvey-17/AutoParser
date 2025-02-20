# **AutoParser API**  

API для получения данных об автомобилях и курсах валют (иены, воны и юаня).  

# **Валюты**  

Курсы валют обновляются **раз в сутки** в **11:00 по Владивостоку (GMT+10)**.  

**Формат курса валют** — число с плавающей запятой, представляющее **отношение данной валюты к рублю (RUB)**.  

### **Источники данных**  
Курсы валют берутся из вкладок _«Купить»_ банков:  

- **Иена (JPY)** — _АТБ Банк_  
- **Юань (CNY)** — _ВТБ Банк_  
- **Вона (KRW)** — _Солид Банк_  
- **Евро (EUR)** - _ЦБ РФ_
- **Доллар (USD)** - _ЦБ РФ_

---

## **API**  

### **Получение курсов валют**  
**`GET /currencies/get-exchange-rates/`**  

- **Описание**: Возвращает актуальные курсы валют к рублю.  
- **Формат ответа**: JSON  

#### **Пример ответа**  

```json
{
  "JPY": {
    "exchange_rate": 0.6784,
    "updated_at": "2025-02-18T14:24:15.929Z"
  },
  "CNY": {
    "exchange_rate": 12.528,
    "updated_at": "2025-02-18T14:24:20.350Z"
  },
  "KRW": {
    "exchange_rate": 0.072,
    "updated_at": "2025-02-18T14:23:22.669Z"
  }
}
```

---

## **Дополнительно**  

- **`exchange_rate`** — текущий курс валюты к рублю  
- **`updated_at`** — дата и время последнего обновления курса (в формате UTC)  

💡 **Примечание**: Данные обновляются раз в сутки, поэтому в течение дня курс остается неизменным.


--- 

# Автомобили 

Парсинг автомобилей реализован в виде периодической задачи, начинающейся **раз в неделю**, например, в субботу. Общий объём данных составляет около **130 тысяч строк** и занимает порядка **11 часов**. 

Данные берутся по 250 автомобилей за запрос, интервал между запросами составляет от 20 до 30 секунд (нужно увеличить до 40-60 секунд). 

Для каждого автомобиля вычисляется пошлина. Перерасчёт пошлины происходит ежедневно после обновления курсов валют.

Аутентификация происходит по IP-адресу пользователя.

## Структура базы данных 

Автомобили разных стран хранятся в пяти соответствующих таблицах: 

- Корея 
- Китай
- Япония
- Европа
- Остальные

--- 

## **API**  

### **Получение автомобилей**  
**`GET /cars?ip={ip}/`**  

- **Описание**: Возвращает информацию об автомобилях в соответствии с указанными фильтрами.
- **Формат ответа**: JSON 

### **Аутентификация** 

Аутентификация происходит по IP-адресу, его нужно указывать при каждом обращении к API.

### **Пагинация**  

Пагинация должна быть реализована через следующие query-параметры: 

- **offset** - смещение от начала на указанное количество страниц. По умолчанию - 0
- **limit** - ограничение количества автомобилей, выдаваемых за один запрос. По умолчанию - 250

Пример

### **Фильтрация** 

Фильтрация происходит через следующие query-параметры: 
- **auc_table** - таблица во внешнем API 
- **lot - номер** лота 
- **auc_name** - название аукциона 
- **auc_date** - дата аукциона 
- **api_id** - ID автомобиля 
- **brand_country** - страна производитель 
- **brand - бренд** 
- **model - модель** автомобиля 
- **year** - год выпуска
- **mileage** - пробег 
- **toll** - пошлина 
- **kuzov** - тип кузова 
- **transmission** - тип КПП 
- **engine_volume** - объём двигателя 
- **drive** - тип привода 
- **color** - цвет 
- **rate** - рейтинг 
- **finish** - цена в валюте экспортёра 
- **power_volume** - мощность двигателя 
- **parsing_date** = дата парсинга 
- **rubber** - руль 
- **engine** - тип двигателя 

#### **Примеры запроса**

##### Получить все автомобили с брендом Тойота

**`GET /cars?brand=Toyota`** 

##### Получить все автомобили с пробегом, большим 50 000

**`GET /auc-cars?mileage__gte=50000`** 

##### Получить все автомобили с годом выпуска от 2010 до 2020

**`GET /auc-cars?year__gte=2010&year__lte=2020`** 

##### Получить все автомобили, в названии моделей которых есть "Corolla"

**`GET /auc-cars?model__icontains=Corolla`**

##### Получить все красные автомобили с правым рулём

**`GET /auc-cars?color=red&rubber=Правый руль`**

💡 **Примечание**

В приведённых выше примерах ради наглядности опущена аутентификация по IP. Полный запрос должен выглядеть так: 

**`GET /cars?ip=194.129.176.54&brand=Toyota`** 

Этот же запрос с пагинацией: 

**`GET /cars?ip=194.129.176.54&brand=Toyota&offset=10&limit=250`** 

