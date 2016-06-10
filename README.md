# birthmark_server

## 使い方
特徴抽出機を持ってきてbirth_searcher.pyと同じ階層に置きます。
その後、
```python birth_searcher.py```
で実行

## スクリプトの役割
- jar/find_jar.sh
  - 同じディレクトリにあるjarファイルを見つけて、barthmark,fuzzyディレクトリにcsvファイルを書く
- jar/fuzzy/find_csv_tofuzzy.sh
  - csvファイルをファジーハッシュ化してfuzzy_csvに書く
- jar/fuzzy/fuzzy_csv/fuzzy_xml_create.py
  - xml作成
- birthmark/fuzzy_search.py,birth_search.py
  - 検索用スクリプト
