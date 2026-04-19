import json

def load_json(path="data.json"):
    with open(path, "r") as f:
        return json.load(f)     # f 안에 적힌 텍스트 내용이 JSON 형식인지 확인하고, 이를 **파이썬의 딕셔너리(dict)나 리스트(list)**로 변환하여 가져온다.
    
# 이 코드는 저장된 json 파일을 읽어서 파이썬에서 사용할 수 있는 데이터 형식(주로 딕셔너리나 리스트)으로 변환해주는 파일 불러오기 함수.
# 만약 지정한 경로에 파일이 없으면 FilePathError가 발생.