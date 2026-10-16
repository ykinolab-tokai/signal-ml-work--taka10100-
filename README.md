# 基礎勉強会の作業リポジトリ

基礎勉強会で書いたコードと、レビューに使う実行結果を保存する場所です。作業途中のコードも保存・共有できます。

教材は [signal-ml-training](https://github.com/ykinolab-tokai/signal-ml-training) を参照します。このリポジトリは学生本人の解答用です。

## 最初に一度だけ行うこと

### 1. 自分用リポジトリをPCに用意する

[第1回](https://github.com/ykinolab-tokai/signal-ml-training/blob/main/handouts/01-environment-and-workflow.md)に従ってGit・GitHub CLI・VS Codeを準備し、GitHub CLIの認証を済ませます。WindowsではWSLのUbuntu、Macではターミナルを使います。教材は配布資料やGitHub上で参照できます。

第1回で作成した**自分用リポジトリ**を、`~/workspace` の下へcloneします。GitHub上では `ykinolab-tokai` 所有の非公開 `signal-ml-work-<GitHubユーザー名>`、PC上のフォルダ名は `signal-ml-work` です。次の `REPOSITORY_URL` は、GitHubの自分用リポジトリの「Code」からコピーしたSSH URLに置き換えてください。すでに取得済みならcloneを省き、`cd ~/workspace/signal-ml-work` と `code .` で開きます。

```bash
mkdir -p ~/workspace
cd ~/workspace
git clone REPOSITORY_URL signal-ml-work
cd signal-ml-work
code .
```

これで `~/workspace/signal-ml-work` がVS Codeで開きます。教材リポジトリをcloneする必要はありません。

### 2. 作業リポジトリ内にPython環境を作り、保存先を確認する

[第1回のPython環境の構築](https://github.com/ykinolab-tokai/signal-ml-training/blob/main/handouts/01-environment-and-workflow.md#python-環境の構築)に従って `uv` をインストールします。
テンプレートには `pyproject.toml` と `uv.lock` が含まれています。この2ファイルに従い、**自分用リポジトリの一番上のフォルダ**でPython 3.12環境を作成します。
環境はこのリポジトリ内の `.venv` に保存されます。WindowsではWSL2のUbuntu、MacではApple Silicon（Mシリーズ）を使用します。

```bash
cd ~/workspace/signal-ml-work
pwd
uv python install 3.12
uv sync --locked
source .venv/bin/activate
python exercise/check_environment.py
```

次の3点を確認できれば準備は完了です。

- 表示されたPythonのパスが `signal-ml-work/.venv/bin/python` を指している。
- `outputs/setup/sine.png` に正弦波の図が保存された。
- `outputs/setup/sine.csv` に図と同じ数値が保存された。

VS Codeの実行ボタンを使う場合は、同梱の設定が作業リポジトリ内のPythonを初期候補にします。別のPythonが使われる場合は、コマンドパレットの `Python: Select Interpreter` で、作業リポジトリ内の `.venv/bin/python` を選び直してください。Python拡張機能が必要です。

## 毎回の作業

1. 今回のNotionページから教材と取り組む演習を確認する。
2. 標準では `exercise/` にコードを保存し、自分用リポジトリの一番上のフォルダから実行する。各回が保存先を指定した場合はその指定を優先する。
3. レビューで使う図や短い数値結果を `outputs/` に保存する。
4. 変更をcommitし、pushする。通常は `main` を使う。

第2回・第6問のファイル名の例は `exercise/exc02_06.py` です。課題の相対パスは、この作業repoのルートを基準にします。`scripts/sessionXX_名前.py` の指定があればその場所へ、フォルダなしのファイル名だけが指定されていればルートへ保存します。レビューには、ここに保存したコードと結果を使います。

説明や結果の解釈はコードコメントまたは既存の結果ファイルに残し、数値には項目名と条件を添えます。別レポートは必要な課題がファイル名と記載内容を指定した場合だけ作り、同じ内容を転記しません。詳細は教材の [作業場所と保存先](https://github.com/ykinolab-tokai/signal-ml-training/blob/main/handouts/README.md#作業場所と保存先)を参照します。

新しいターミナルを開いたときは、作業リポジトリのルートに移動し、そのPython環境を有効にしてから実行します。

```bash
cd ~/workspace/signal-ml-work
source .venv/bin/activate
python exercise/exc02_06.py
```

変更を共有するときの例です。ファイル名は、今回作成・変更したものに置き換えます。

```bash
git status
git add exercise/exc02_06.py
git commit -m "第2回: 条件分岐の演習"
git push
```

図や結果も共有する場合は、commitの前に対象ファイルを `git add` します。VS Codeのソース管理から同じ操作をしても構いません。修正後も同じ手順で変更を記録します。

PR練習の宛先はこの作業repoの `main` です。練習中の修正は練習ブランチへcommit・pushし、次回の通常作業の前に [PR練習後の手順](https://github.com/ykinolab-tokai/signal-ml-training/blob/main/handouts/README.md#pr練習後に通常作業へ戻る)で `main` への切り替えと同期を行います。レビュー待ちの変更は練習ブランチに残ります。

## 保存するもの

| 場所 | 内容 |
| --- | --- |
| `exercise/` | 各回の解答コード。`check_environment.py` は最初の動作確認用 |
| `outputs/` | レビューで使う図や短い数値結果 |
| `.vscode/` | 作業リポジトリ内のPython環境を使うための初期設定 |
| `pyproject.toml` | Pythonのバージョン条件と依存パッケージの定義 |
| `uv.lock` | 依存パッケージの解決結果。再現可能な環境構築に使用 |

この表は標準の配置です。各回が指定する `scripts/` やルートのファイルも作業repo内で管理します。

Python環境、キャッシュ、入力データ用の `data/`、大きなモデルを置く `checkpoints/` はGitの保存対象から除外しています。入力データが必要な課題は、教材の案内に従って準備してください。`pyproject.toml` と `uv.lock` はGitで管理し、`.venv/` は管理しません。授業で環境定義の更新が案内された場合は、このリポジトリの2ファイルを更新してから、次を実行します。テンプレートの変更は、作成済みの作業リポジトリには自動反映されません。

```bash
cd ~/workspace/signal-ml-work
uv sync --locked
source .venv/bin/activate
```

## うまく動かないとき

- `.venv/bin/activate` が見つからない場合は、作業リポジトリのルートで `uv sync --locked` が成功したか確認する。
- `numpy` や `matplotlib` が見つからない場合は、作業リポジトリ内のPython環境を使っているか確認する。`source .venv/bin/activate` の後、`which python` で確認できる。
- `push` に失敗した場合は、エラーメッセージを残し、今回の作業内容と一緒に相談する。

レビューの依頼方法は、各回のNotionページの案内に従います。

## 環境定義の出典

`pyproject.toml` と `uv.lock` は [signal-ml-training（f85b81d）](https://github.com/ykinolab-tokai/signal-ml-training/tree/f85b81dab328803dd34a39811c37b476e044363d) の環境定義を基に、プロジェクト名と説明を作業用に変更したものです。依存パッケージの条件・固定バージョンは引き継いでいます。これらのファイルの著作権表示とライセンス条件は [LICENSE.training-environment](LICENSE.training-environment) に記載しています。
