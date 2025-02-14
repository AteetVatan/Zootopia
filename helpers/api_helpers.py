import requests

class ApiHelpers:


    def load(self):
        name = 'fox'
        api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
        response = requests.get(api_url, headers={'X-Api-Key': '9dm/wEXckTexM+5Ige1izw==Whszh7lknfxIvamn'})
        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error:", response.status_code, response.text)