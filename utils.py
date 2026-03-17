import json

def read_html(Path):
    try:
        with open(Path,"r",encoding="utf-8") as f:
            data=f.read()
            return data
    except Exception as e:
        print("Error",read_html.__name__,e)    

def read_json(JSON_FILE_PATH):
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
            return json.loads(f)
    except Exception as e:
        print("Error in read_json:", e)
        return {}      