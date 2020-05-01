import re

input_f_name = "contents.txt" # 入力ファイルの名前
basic_info_template_pattern = r'''
    ^\{\{基礎情報.*\n    # 基礎情報の先頭
    (.*\n)*?            # 基礎情報の中身を非貪欲
    ^\}\}$              # 基礎情報の終了
    '''

def _25():
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
        
        # 確認
        for key, value in basic_info_dict.items():
            print(key,":", value)

if __name__ == "__main__":
    _25()

"""
この章で気づくのは遅いかもしれないが, 正規表現でよくありがちな間違えについての知見
    （ただし自分が間違えていただけ）
    （というかドキュメントにそう書いてある）
$は通常文字列の最終文字の後ろもしくは改行の直前にのみマッチする
    (この時その文字自体にマッチしているわけではなくて（表現が間違っているかも）
    ステータスにマッチしているため下のようになる
    Text = "aaa\n"
    r"aaa$"ならaaaが返ってくる)
^は通常文字列の最初文字の文字にのみマッチする
    (上記と同様のマッチング方法)
ここで注意したいのは\nそのものにマッチングする物は存在しないという点
つまり
aaa\nbbb\nccc\nddd\n
で
bbb\nccc
を取り出したい時に
r"bbb$ccc"とするのは間違え
ちなみにr"bbb$^ccc"はもちろんダメ
r"bbb\nccc"をしっかり使おう

改行コードを取り出すには\nと指定するのが一番妥当
ちなみに\sを使うと表示されない[ \t\n\r\f\v]が手に入る他
re.DOTALLをパラメータとして渡してあげれば.が\nにマッチする
    （上記で書かなかったが.は\nにマッチしない）
また, 複数行でまたがっている時はre.MULTILINEを指定してあげると$や^が
途中の改行コードに反応してくれる
    （ただし, 改行コードに反応するわけではないので注意）
"""