import requests
class RequestHandler:
    @staticmethod
    def get_json_cesar(token):
      print("get_json_cesar")
      url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token="+token
      r = requests.get(url)
      return r.json()
  
    @staticmethod
    def post_file(token):
      print("post_file")
      url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token="+token

      answer = {'answer': open('answer.json', 'rb')}

      r = requests.post(url, files=answer)
      return r
