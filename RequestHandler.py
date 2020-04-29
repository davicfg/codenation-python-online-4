import requests
class RequestHandler:
    @staticmethod
    def get_json_cesar(token):
      url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token="+token
      print(url)
      r = requests.get(url)
      return r.json()
