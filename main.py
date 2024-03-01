import requests
import os


def download_image(path, url):
    if not os.path.exists(path):
        os.mkdir(path)

    path_name = path + '/' + url.split('/')[-1]

    with open(path_name, 'wb') as image:
        image.write(requests.get(url).content)


MLB_BASE_URI = 'https://api.mercadolibre.com'
MLB_URI_ITEMS = 'items'

publication_id = 'MLB3510529559'

url = f'{MLB_BASE_URI}/{MLB_URI_ITEMS}/{publication_id}'

request = requests.get(url)

if request.ok and request.status_code == 200:

    mlb_publication = request.json()

    if mlb_publication['thumbnail']:
        download_image(mlb_publication['id'], mlb_publication['thumbnail'])

    if mlb_publication['pictures']:

        for picture in mlb_publication['pictures']:
            download_image(mlb_publication['id'], picture['url'])

print('Anúncio importado com sucesso!')
