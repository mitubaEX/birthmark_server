# birthmark_server

## 使い方
特徴抽出機を持ってきてbirth_searcher.pyと同じ階層に置きます。
その後、
```python birth_searcher.py```
で実行

## 各ディレクトリの役割
- data/jar: 全てのjarファイルの置き場
- data/birthmark: 全てのバースマークの置き場
- data/fuzzy: 全てのバースマークをfuzzy_hash化したものの置き場
- data/fuzzy_nob: 全てのバースマークをfuzzy_hash化(-bなし）したものの置き場
- data/class_list: クラスファイルの置き場
- data/birth_xml: 全てのバースマークのxmlの置き場
- data/fuzzy_xml: 全てのfuzzyのxmlの置き場
- data/fuzzy_nob_xml: 全てのfuzzy(-bなし)のxmlの置き場
- data/class_compare: stigmataの0.75位上のクラスをいろいろする
