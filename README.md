# birthmark_server

## 使い方
特徴抽出機を持ってきてbirth_searcher.pyと同じ階層に置きます。
その後、
```python birth_searcher.py```
で実行

## 各ディレクトリの役割
- data
	- birth\_search\_result: 検索結果の出力の置き場
	- search_birthmark: 検索に使用したバースマークの置き場
	- jar: 全てのjarファイルの置き場
	- birthmark: 全てのバースマークの置き場
	- fuzzy: 全てのバースマークをfuzzy_hash化したものの置き場
	- fuzzy_nob: 全てのバースマークをfuzzy_hash化(-bなし）したものの置き場
	- class_list: クラスファイルの置き場
	- birth_xml: 全てのバースマークのxmlの置き場
	- fuzzy_xml: 全てのfuzzyのxmlの置き場
	- fuzzy_nob_xml: 全てのfuzzy(-bなし)のxmlの置き場
	- class_compare: stigmataの0.75位上のクラスの組が書かれたcsvの置き場
	- class\_compare\_before: stigmataのcompareで出力されたものの置き場

- script: mainを実行すると全て実行する
	- birth_search: バースマークを利用した検索をする
	- fuzzy_search: ファジーハッシュを利用した検索をする
	- jar_compare: jarファイルの組を比較し、0.75位上の組での検索
	- once_search: 一回の検索時間を測定する
	- xml_create: xmlを作成する
- views: htmlの置き場

## Usage

バースマークサーバーに入れるためのデータを作成するところまでをやります．
検索は [ToolForResearch](https://github.com/mitubaEX/ToolForResearch) を使ってください

```sh
# clone stigmata
git clone https://github.com/tamada/stigmata.git
cd stigmata && mvn package

# get apache solr
curl -o solr-6.4.1.zip http://archive.apache.org/dist/lucene/solr/6.4.1/solr-6.4.1.zip
unzip solr-6.4.1.zip

# mv jar files
mkdir data/jar
cp ${jar_files} data/jar

# extract birthmark from jar files
cd script/xml_create && sh find_jar_ext_birthmark.sh 2gram 3gram 4gram 5gram 6gram uc

# create birthmark_xml
mkdir data/birth_xml
cd ./script/xml_create && for i in 2gram 3gram 4gram 5gram 6gram uc ; do python birthmark_xml_create_python3.py "$i";done

# solr dir
## create core
for i in 2gram 3gram 4gram 5gram 6gram uc ; do bin/solr create -c "$i" ;done

## fix strings field of managed-schema
<fieldType name="strings" class="solr.TextField" multiValued="false">
      <analyzer type="index">
          <tokenizer class="solr.PatternTokenizerFactory" pattern="\s*,\s*"/>
          <filter class="solr.StopFilterFactory" ignoreCase="true" words="stopwords.txt" />
         <filter class="solr.LowerCaseFilterFactory"/>
     </analyzer>
     <analyzer type="query">
         <tokenizer class="solr.PatternTokenizerFactory" pattern="\s*,\s*"/>
         <filter class="solr.StopFilterFactory" ignoreCase="true" words="stopwords.txt" />
         <filter class="solr.SynonymFilterFactory" synonyms="synonyms.txt" ignoreCase="true" expand="true"/>
         <filter class="solr.LowerCaseFilterFactory"/>
     </analyzer>
 </fieldType>

## post to solr ( core -> 2gram 3gram 4gram 5gram 6gram uc )
for i in 2gram 3gram 4gram 5gram 6gram uc ; do find ${birth_xml_dir} -name "*$i*" | xargs -I% bin/post -c "$i" ;done
```
