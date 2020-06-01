import re

input_f_name = "contents.txt" # 入力ファイルの名前
basic_info_template_pattern = r'''
    ^\{\{基礎情報.*\n    # 基礎情報の先頭
    (.*\n)*?            # 基礎情報の中身を非貪欲
    ^\}\}$              # 基礎情報の終了
    '''

"""
略名 : イギリス
日本語国名 : グレートブリテン及び北アイルランド連合王国
公式国名 : United Kingdom of Great Britain and Northern Ireland英語以外での正式国名:
An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath（スコットランド・ゲール語）
Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon（ウェールズ語）
Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann（アイルランド語）
An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh（コーンウォール語）
Unitit Kinrick o Great Breetain an Northren Ireland（スコットランド語）
Claught Kängrick o Docht Brätain an Norlin Airlann、Unitet Kängdom o Great Brittain an Norlin Airlann（アルスター・スコットランド語）
国旗画像 : Flag of the United Kingdom.svg
国章画像 : Royal Coat of Arms of the United Kingdom.svg
国章リンク : （国章）
標語 : Dieu et mon droit（フランス語:神と私の権利）
国歌 : 神よ女王陛下を守り給え
位置画像 : Location_UK_EU_Europe_001.svg
公用語 : 英語（事実上）
首都 : ロンドン
最大都市 : ロンドン
元首等肩書 : 女王
元首等氏名 : エリザベス2世
首相等肩書 : 首相
首相等氏名 : デーヴィッド・キャメロン
面積順位 : 76
面積大きさ : 1 E11
面積値 : 244,820
水面積率 : 1.3%
人口統計年 : 2011
人口順位 : 22
人口大きさ : 1 E7
人口値 : 63,181,775United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population
人口密度値 : 246
GDP統計年元 : 2012
GDP値元 : 1兆5478億IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom
GDP統計年MER : 2012
GDP順位MER : 5
GDP値MER : 2兆4337億
GDP統計年 : 2012
GDP順位 : 6
GDP値 : 2兆3162億
GDP/人 : 36,727
建国形態 : 建国
確立形態1 : イングランド王国／スコットランド王国（両国とも1707年連合法まで）
確立年月日1 : 927年／843年
確立形態2 : グレートブリテン王国建国（1707年連合法）
確立年月日2 : 1707年
確立形態3 : グレートブリテン及びアイルランド連合王国建国（1800年連合法）
確立年月日3 : 1801年
確立形態4 : 現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
確立年月日4 : 1927年
通貨 : UKポンド (&pound;)
通貨コード : GBP
時間帯 : ±0
夏時間 : +1
ISO 3166-1 : GB / GBR
ccTLD : .uk / .gb使用は.ukに比べ圧倒的少数。
国際電話番号 : 44
注記 : 
"""

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
    """
    基礎情報の強調マークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_emphasis_markup_basic_info_dict : dict[str, str]
        基礎情報の本文から強調マークアップを削除した辞書
    """

    deleted_emphasis_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_emphasis_markup_basic_info_dict[key] = re.sub(r"''+", "", value)

    return deleted_emphasis_markup_basic_info_dict


def delete_internal_links(basic_info_dict):
    """
    基礎情報の内部リンクマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_internal_link_markup_basic_info_dict : dict[str, str]
        基礎情報の本文から内部リンクマークアップを削除した辞書
    """

    deleted_internal_link_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_internal_link_markup_basic_info_dict[key] = re.sub(r"\[\[(?!ファイル:|Category:)([^\]]+\|)?([^\|]+?)\]\]", r"\2", value)

    return deleted_internal_link_markup_basic_info_dict

def delete_files(basic_info_dict):
    """
    基礎情報のファイルマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_file_markup_basic_info_dict : dict[str, str]
        基礎情報の本文からファイルマークアップを削除した辞書
    """

    deleted_file_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_file_markup_basic_info_dict[key] = re.sub(r"\[\[ファイル:([^\]|]+).*?\]\]", r"\1", value)

    return deleted_file_markup_basic_info_dict

def delete_external_links(basic_info_dict):
    """
    基礎情報の外部リンクマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_external_link_markup_basic_info_dict : dict[str, str]
        基礎情報の本文から外部リンクマークアップを削除した辞書
    """

    deleted_external_link_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_external_link_markup_basic_info_dict[key] = re.sub(r"\[([^\]\s]+?\s)?([^\]]+)\]", r"\2", value)

    return deleted_external_link_markup_basic_info_dict

def delete_categories(basic_info_dict):
    """
    基礎情報のカテゴリマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_categories_markup_basic_info_dict : dict[str, str]
        基礎情報の本文からカテゴリマークアップを削除した辞書
    """

    deleted_categories_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_categories_markup_basic_info_dict[key] = re.sub(r"\[\[Category:([^\]|]+).*?\]\]", r"\1", value)

    return deleted_categories_markup_basic_info_dict

def delete_redirects(basic_info_dict):
    """
    基礎情報のリダイレクトマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_redirect_markup_basic_info_dict : dict[str, str]
        基礎情報の本文からリダイレクトマークアップを削除した辞書
    """

    deleted_redirect_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_redirect_markup_basic_info_dict[key] = re.sub(r"#REDIRECT \[\[([^\]]+)\]\]", r"\1", value)

    return deleted_redirect_markup_basic_info_dict

def delete_comments(basic_info_dict):
    """
    基礎情報のコメントアウトのマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_comment_markup_basic_info_dict : dict[str, str]
        基礎情報の本文からリダイレクトマークアップを削除した辞書
    """

    deleted_comment_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_comment_markup_basic_info_dict[key] = re.sub(r"<!-- [.\s]+ -->", "", value)

    return deleted_comment_markup_basic_info_dict

def delete_unordered_lists(basic_info_dict):
    """
    基礎情報の箇条書きのマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_unordered_list_markup_basic_info_dict : dict[str, str]
        基礎情報の本文から箇条書きのマークアップを削除した辞書
    """

    deleted_unordered_list_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        
        deleted_unordered_list_markup_basic_info_dict[key] = re.sub(r"\n\*+", "\n", value, re.MULTILINE)

    return deleted_unordered_list_markup_basic_info_dict
    
def delete_ordered_lists(basic_info_dict):
    """
    基礎情報の番号付き箇条書きのマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_ordered_list_markup_basic_info_dict : dict[str, str]
        基礎情報の本文から番号付き箇条書きのマークアップを削除した辞書
    """

    deleted_ordered_list_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_ordered_list_markup_basic_info_dict[key] = re.sub(r"^#+(.+)", r"\1", value,re.MULTILINE)

    return deleted_ordered_list_markup_basic_info_dict

def delete_define_lists(basic_info_dict):
    """
    基礎情報の定義の箇条書きのマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_define_list_markup_basic_info_dict : dict[str, str]
        基礎情報の本文から定義の箇条書きのマークアップを削除した辞書
    """

    deleted_define_list_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_define_list_markup_basic_info_dict[key] = re.sub(r"^(:|;)(.+)", r"\1", value,re.MULTILINE)

    return deleted_define_list_markup_basic_info_dict


def delete_ref(basic_info_dict):
    """
    基礎情報の定義の注釈のマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_ref_markup_basic_info_dict : dict[str, str]
        基礎情報の本文から注釈のマークアップを削除した辞書
    """

    deleted_ref_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_ref_markup_basic_info_dict[key] = re.sub(r"<.+?>", "", value)

    return deleted_ref_markup_basic_info_dict
    

def delete_lang(basic_info_dict):
    """
    基礎情報のlangのマークアップを削除

    Parameters
    ----------
    basic_info_dict : dict[str, str]
        基礎情報を格納した辞書
    
    Returns
    -------
    deleted_lang_markup_basic_info_dict : dict[str, str]
        基礎情報の本文から注釈のマークアップを削除した辞書
    """

    deleted_lang_markup_basic_info_dict = {}

    for key, value in basic_info_dict.items():
        deleted_lang_markup_basic_info_dict[key] = re.sub(r"\{\{lang(?:[^|]*?\|)*?([^|]*?)\}\}", r"\1", value, re.MULTILINE)

    return deleted_lang_markup_basic_info_dict

def _28():

    basic_info_dict = get_basic_info_dict()
    
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
    basic_info_dict = delete_ref(basic_info_dict)
    basic_info_dict = delete_lang(basic_info_dict)

    for key, value in basic_info_dict.items():
        print(key, ":", value)

if __name__ == "__main__":
    _28()
