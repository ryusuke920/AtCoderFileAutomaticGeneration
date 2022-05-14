from pathlib import Path
import os
import input_path

def AtCoderContestsMakeFile(input_path: str, contest_genre: int, contest_number: int) -> None:
    contest_name = ["ABC", "ARC", "AGC", "PAST"] # コンテスト名
    number_length = [6, 6, 6, 15] # 各コンテストの問題数

    if contest_genre != 3:
        contest_folder = Path(f"{input_path}/{contest_name[contest_genre]}/{contest_name[contest_genre]}{contest_number}")
    else:
        contest_folder = Path(f"{input_path}/{contest_name[contest_genre]}/第{contest_number}回アルゴリズム実技検定")
    contest_folder.mkdir(exist_ok=True)
    
    # テンプレートの読み込み
    with open("./template.py") as f:
        template_py = f.read()
    
    # 各問題の作成
    for i in range(number_length[contest_genre]):
        make_py_file = Path(f"{contest_folder}/{chr(65 + i)}.py")

        # 既に存在する場合にはファイルを生成しない
        if os.path.exists(make_py_file):
            continue

        # Pythonのファイルを生成
        make_py_file.touch(exist_ok=True)
        
        # テンプレートを書き込む
        with open(make_py_file, mode='w') as f:
            f.write(template_py)

input_path = input_path.input_path
# 0 -> ABC,  1 -> ARC,  2 -> AGC,  3 -> PAST
# コンテスト名・第⚪️回   ※ 下記の場合だと ARC001~ARC500回まで作成します
for i in range(1000, 1001):
    AtCoderContestsMakeFile(input_path, 1, str(i).zfill(3))