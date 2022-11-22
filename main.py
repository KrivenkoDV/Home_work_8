## Задание №1
# import requests
#
# heroes_data = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json').json()
# heroes = list(filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], heroes_data))
# int_dict = {hero['name']:hero['powerstats']['intelligence'] for hero in heroes}
#
# print('Самый умный супергерой:')
# print(max(int_dict, key=int_dict.get))

## Задание №2
import requests
class YaUploader:
    def __init__(self, _token: str):
        self.token = _token
    def upload(self, file_path):
        """Метод загружает файл file_path на Яндекс.Диск"""

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        filename = file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"} # Определяем параметры запроса (назначаем путь загрузки, имя файла и разрешаем перезапись)
        _response = requests.get(upload_url, headers=headers, params=params).json() # Выполняем запрос на получение ссылки для загрузки
        href = _response.get("href", "") # Выделяем ссылку для загрузки в отдельную переменную
        responce = requests.put(href, data=open(file_path, 'rb')) # Выполняем запрос на загрузку файла на Яндекс.Диск по полученной ссылке
        responce.raise_for_status() # Получаем статус отправки файла
        if responce.status_code == 201: # Проверяем успешность отправки по полученному статусу
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"

if __name__ == '__main__':
    path_to_file = 'files/file1.jpg' # Получаем путь к загружаемому файлу и токен от пользователя
    token = 'y0_AgAAAAA_Tu8vAADLWwAAAADUi9h2_aEharEcRIKJMsJmISrPFyjhcZA'
    uploader = YaUploader(token) # Определяем экземпляр класса для токена пользователя
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск") # Загружаем файл на диск
    result = uploader.upload(path_to_file)
    print(result)
