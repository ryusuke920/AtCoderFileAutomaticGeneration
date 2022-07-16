from pathlib import Path
import os
import input_path

def AtCoderContestsMakeFile(input_path: str, contest_genre: int, contest_number: int) -> None:
    contest_name = ["ABC", "ARC", "AGC", "PAST"]
    contest_length = [8, 6, 6, 15]

    if contest_genre != 3:
        contest_folder = Path(f"{input_path}/{contest_name[contest_genre]}/{contest_name[contest_genre]}{contest_number}")
    else:
        contest_folder = Path(f"{input_path}/{contest_name[contest_genre]}/第{contest_number}回アルゴリズム実技検定")
    
    contest_folder.mkdir(exist_ok=True)
    
    # テンプレートの読み込み
    with open("./template.py") as f:
        template_py = f.read()
    
    # 各問題の作成
    for i in range(contest_length[contest_genre]):
        contest_problem_folder = Path(f"{input_path}/{contest_name[contest_genre]}/{contest_name[contest_genre]}{contest_number}/{chr(65 + i)}")
        contest_problem_folder.mkdir(exist_ok=True)
        make_py_file = Path(f"{contest_folder}/{chr(65 + i)}/{chr(65 + i)}.py")

        # 上書きしたくない場合
        if os.path.exists(make_py_file):
            continue

        # 上書きしたい場合（既にファイルがありコードが書かれていても全て消えて上書きするので注意！）
        # if os.path.exists(make_py_file): continue
        

        # Pythonのファイルを生成
        make_py_file.touch(exist_ok=True)

        attention = "※test/ が既に作成されている場合は下記コマンドで test/ を削除する\n" \
                    "rm -rf test/\n"

        flow = "oj（online-judge-tools）の使い方について\n\n" \
               "1. テストケースをダウンロード\n" \
               "2. サンプルが合っているかジャッジする\n" \
               "3. 提出する\n\n"
    
        problem_url = contest_name[contest_genre].lower() + str(contest_number)
        problem_download = f"oj d https://atcoder.jp/contests/{problem_url}/tasks/{problem_url}_{chr(97 + i)}\n"
        judge_testcase = 'oj t -c "python3 A.py"\n'
        code_submit = f"oj d https://atcoder.jp/contests/{problem_url}/tasks/{problem_url}_{chr(97 + i)} " \
                      f"{chr(65 + i)}.py --guess-python-interpreter pypy\n\n"
        
        # テンプレートを書き込む
        with open(make_py_file, mode='w') as f:
            f.write("'''\n")
            f.write(flow)
            f.write(problem_download)
            f.write(judge_testcase)
            f.write(code_submit)
            f.write(attention)
            f.write("'''\n\n")
            f.write(template_py)


'''
0 -> ABC,  1 -> ARC,  2 -> AGC,  3 -> PAST
コンテスト名・第⚪️回   ※ 下記の場合だと ARC001~ARC500回まで作成します

for i in range(200, 501):
    AtCoderContestsMakeFile(input_path, 1, str(i).zfill(3))

上記のようなコードだと ABC200~ABC500までのファイルを自動作成します
'''

input_path = input_path.input_path
for i in range(500, 501):
    AtCoderContestsMakeFile(input_path, 0, str(i).zfill(3))