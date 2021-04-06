from pathlib import Path

def AtCoderContestsMakeFile(send_number, contest_number):
    contest_name = ["abc", "arc", "agc", "past"] # コンテスト名
    number_length = [6, 6, 6, 15] # 各コンテストの問題数

    if send_number != 3:
        contest_folder = Path(F"{contest_name[send_number].upper()}{contest_number}")
        contest_folder.mkdir(exist_ok = True)
    else: # PAST用
        contest_folder = Path(F"第{contest_number}回アルゴリズム実技検定")
        contest_folder.mkdir(exist_ok = True)

    for i in range(number_length[send_number]):
        if send_number != 3:
            # Pathの設定
            make_py_file = Path(F"/Users/######/{contest_name[send_number].upper()}/{contest_folder}/{chr(65 + i)}.py")
        else: # PAST用
            # Pathの設定
            make_py_file = Path(F"/Users/######/{contest_name[send_number].upper()}/{contest_folder}/{chr(65 + i)}.py")            

        # Pythonのファイルを生成
        make_py_file.touch()



# 0 -> ABC,  1 -> ARC,  2 -> AGC,  3 -> PAST
AtCoderContestsMakeFile(0, 200) # コンテスト名・第⚪️回   ※ 今回の場合だと ABC200 の場合です

"""
〜操作方法〜
⓵ ファイルを作りたい階層に移動する
⓶ 27行目の引数を設定する
⓷ 17, 20 行目に各自でPathを設定する
④ Pythonコードを実行
"""