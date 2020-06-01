import re

input_f_name = "contents.txt" # 入力ファイルの名前
basic_info_template_pattern = r'''
    ^\{\{基礎情報.*\n    # 基礎情報の先頭
    (.*\n)*?            # 基礎情報の中身を非貪欲
    ^\}\}$              # 基礎情報の終了
    '''

def get_basic_info_dict():    
    """
    入力ファイルから基礎情報を辞書型にしてその辞書を返す    

    Returns
    -------
    basic_info_dict : dict[str, str]
        ファイルからkeyとvalueを切り取ってその辞書を返す
    """ 
    
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

def _26():

    basic_info_dict = get_basic_info_dict()

    for key, value in basic_info_dict.items():
        basic_info_dict[key] = re.sub(r"''+", "", value)
    
    for key, value in basic_info_dict.items():
        print(key,":", value)

if __name__ == "__main__":
    _26()
