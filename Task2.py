import requests
import yadisk

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def put_folder(self, folder_name):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": folder_name}
        requests.put(files_url, params=params, headers=headers)
        print('Папка создана!')

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, path_to_file):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        responce = requests.put(href, data=open(link_to_file, 'rb'))
        print("Файл записан!")


if __name__ == '__main__':
    TOKEN = input("Введите токен Яндекс.Диск: ")
    check = yadisk.YaDisk(token=TOKEN)
    # Проверяет, валиден ли токен
    if check.check_token() == True:
        folder = input("Введите имя папки на Яндекс.Диск: ")
        path_to_file = input("Введите путь до файла на компьютере: ")
        name_file = input("Введите полное имя файла (с расширением): ")
        link_to_file = path_to_file + '/' + name_file
        ya = YandexDisk(TOKEN)
        ya.put_folder(folder_name=folder)
        try:
            ya.upload_file_to_disk(f"{folder}/{name_file}", link_to_file)
        except:
            print("Ошибка, введите корректный путь и/или имя файла!")
    else:
        print("Некорректный токен!")