import re
import requests

input_f_name = "contents.txt" # 入力ファイルの名前
basic_info_template_pattern = r'''
    ^\{\{基礎情報.*\n    # 基礎情報の先頭
    (.*\n)*?            # 基礎情報の中身を非貪欲
    ^\}\}$              # 基礎情報の終了
    '''

def get_basic_info_dict():
    # 格納する辞書の定義
    basic_info_dict = {}

    # 入力ファイルの読み込み
    with open(input_f_name, encoding="utf-8") as target:
        
        # 行をまたがって認識する必要があるのでreadを使う
        text = target.read()    

        # 基礎情報のテンプレートの抜き出し
        basic_info_text = re.search(basic_info_template_pattern, text, re.MULTILINE + re.VERBOSE)

        # フィールドと値の抽出
        fields_and_values = basic_info_text[0].split("\n|")

        # フィールドと値を辞書に格納
        for field_and_value in fields_and_values[1:]:
            field, value = re.split(r"\s+=\s+",field_and_value)
            basic_info_dict[field] = value.rstrip("}")
        
    return basic_info_dict

def delete_emphasis(basic_info_dict):

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"'(')+", "", value)

    return basic_info_dict


def delete_internal_links(basic_info_dict):

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"\[\[(?!ファイル:|Category:)([^\]]+\|)?([^\|]+?)\]\]", r"\2", value)

    return basic_info_dict

def delete_files(basic_info_dict):
    
    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"\[\[ファイル:([^\]|]+).*?\]\]", r"\1", value)

    return basic_info_dict

def delete_external_links(basic_info_dict):

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"\[([^\]\s]+?\s)?([^\]]+)\]", r"\2", value)

    return basic_info_dict

def delete_categories(basic_info_dict):

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"\[\[Category:([^\]|]+).*?\]\]", r"\1", value)

    return basic_info_dict

def delete_redirects(basic_info_dict):

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"#REDIRECT \[\[([^\]]+)\]\]", r"\1", value)

    return basic_info_dict

def delete_comments(basic_info_dict):

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"<!-- [.\s]+ -->", "", value)

    return basic_info_dict

def delete_unordered_lists(basic_info_dict):

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"^\*+(.+)", r"\1", value,re.MULTILINE)

    return basic_info_dict
    
def delete_ordered_lists(basic_info_dict):

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"^#+(.+)", r"\1", value,re.MULTILINE)

    return basic_info_dict

def delete_define_lists(basic_info_dict):

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"^(:|;)(.+)", r"\1", value,re.MULTILINE)

    return basic_info_dict
    

def extract_basic_info(basic_info_dict):
    
    basic_info_dict = delete_emphasis(basic_info_dict)
    basic_info_dict = delete_internal_links(basic_info_dict)
    basic_info_dict = delete_files(basic_info_dict)
    basic_info_dict = delete_external_links(basic_info_dict)
    basic_info_dict = delete_categories(basic_info_dict)
    basic_info_dict = delete_comments(basic_info_dict)
    basic_info_dict = delete_redirects(basic_info_dict)
    basic_info_dict = delete_unordered_lists(basic_info_dict)
    basic_info_dict = delete_ordered_lists(basic_info_dict)
    basic_info_dict = delete_unordered_lists(basic_info_dict)
    basic_info_dict = delete_define_lists(basic_info_dict)

    return basic_info_dict

def _29():

    basic_info_dict = get_basic_info_dict()

    basic_info_dict = extract_basic_info(basic_info_dict)

    flag_image_name = basic_info_dict["国旗画像"]

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": "File:{0}".format(flag_image_name),
        "iiprop": "url"
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    
    PAGES = DATA["query"]["pages"]

    IMAGEINFO = list(PAGES.values())[0]["imageinfo"]

    print(IMAGEINFO[0]["url"])

if __name__ == "__main__":
    _29()
