#Sublime Text2の自作snippet,plugin,macro
##snippet
| カテゴリ| ファイル名| key| 内容| 
|:-----------|:------------|:------------|:------------|
| erb| scriptlet.sublime-snippet| sc| スクリプトレットを出力| 
| erb| scriptlet_if.sublime-snippet| scw| スクリプトレットのprintを出力| 
| erb| scriptlet_write.sublime-snippet| sci| if文のスクリプトレットを出力| 
| はてなブログ| super_hatena.sublime-snippet| hasu| はてなブログのスーパーはてな記法を出力| 
| ruby| ruby_encode_utf8.sublime-snippet| encode8| RubyのシェバングでのUTF8エンコード指定| 
| rails| pry_breakpoint.sublime-snippet| bp| pryでRailsをデバッグする際に利用するブレイクポイント | 
###scriptlet.sublime-snippet
出力
```erb:scriptlet.sublime-snippet
<% ruby_script %>
```
###scriptlet_write.sublime-snippet
出力
```erb:scriptlet_write.sublime-snippet
<% if ruby_script %>
  contents
<% end %>
```
###scriptlet_write.sublime-snippet
出力
```erb:scriptlet_write.sublime-snippet
<%= ruby_script %>
```
###super_hatena.sublime-snippet
```text:super_hatena.sublime-snippet
>| language| 
paste_source
| | <
```
###super_hatena.sublime-snippet
```text:super_hatena.sublime-snippet
>| language| 
paste_source
| | <
```
###ruby_encode_utf8.sublime-snippet
```ruby:ruby_encode_utf8.sublime-snippet
# encoding: utf-8
```
###pry_breakpoint.sublime-snippet
```rails:pry_breakpoint.sublime-snippet
binding.pry
```
##plugin
| ファイル名| 内容| 
|:-----------|:------------|
| BrowserOpenerCommand.py| Google検索,Google翻訳（日英）,Google翻訳（英日）,Wikipedia検索を呼び出し| 
| GetSystemDateCommand.py| 3形式のシステム日付を取得。年月日時分秒・年月日スラッシュ区切り・年月日区切りなしの3種| 
| ToCamelCommand.py| 選択中の文字列をキャメルケースに変換| 
| ToSnakeCommand.py| 選択中の文字列をスネークケースに変換| 
| TableJustifierCommand.py| テーブル構造の文字列をスペースパディングで整形| 
###BrowserOpenerCommand.py
選択中の文字列を利用してブラウザを開きます。

Google検索、Google翻訳（日英）、Google翻訳（英日）、Wikipedia検索が可能。

キー設定例
```json:key-config
  { "keys": ["ctrl+shift+alt+g"], "command": "browser_opener", "args": {"type": "search_google"} },
  { "keys": ["ctrl+shift+alt+e"], "command": "browser_opener", "args": {"type": "google_translate_en_ja"} },
  { "keys": ["ctrl+shift+alt+j"], "command": "browser_opener", "args": {"type": "google_translate_ja_en"} },
  { "keys": ["ctrl+shift+alt+w"], "command": "browser_opener", "args": {"type": "search_wikipedia"} },
```
上記のキー設定が前提の場合、例えばtbpgというテキストを選択して、ctrl+shift+alt+gを実行すれば

「tbpg」でGoogle検索した結果がブラウザに表示される
###GetSystemDateCommand.py| 
システム日付文字列を取得したい場合に利用。

キー設定例
```json:key-config
  { "keys": ["ctrl+alt+d", "1"], "command": "get_system_date", "args": {"format": "yyyy/mm/dd hh:mi:ss"} },
  { "keys": ["ctrl+alt+d", "2"], "command": "get_system_date", "args": {"format": "yyyy/mm/dd"} },
  { "keys": ["ctrl+alt+d", "3"], "command": "get_system_date", "args": {"format": "yyyymmdd"} },
```
```text:取得結果
2013/07/01 00:01:08
2013/07/01
20130701
```
###ToCamelCommand.py
選択中の文字列をキャメルケースに変換します。先頭1文字のキャピタライズの有無を選択可能。

先頭1文字のキャピタライズ指定なし

hoge hige => hogeHige

hoge_hige => hogeHige


先頭1文字のキャピタライズ指定あり

hoge hige => HogeHige

hoge_hige => HogeHige


キー設定例
```json:key-config
  { "keys": ["ctrl+shift+c"], "command": "to_camel", "args": {"capitalize": false }},
  { "keys": ["ctrl+alt+shift+c"], "command": "to_camel", "args": {"capitalize": true }},
```
###ToSnakeCommand.py
選択中の文字列をスネークケースに変換します。大文字にするか小文字にするか選択可能。

小文字指定時

hoge hige => hoge_hige

hogeHige => hoge_hige


大文字指定時

hoge hige => HOGE_HIGE

hogeHige => HOGE_HIGE


キー設定例
```json:key-config
  { "keys": ["ctrl+shift+o"], "command": "to_snake", "args": {"upper": false }},
  { "keys": ["ctrl+alt+shift+o"], "command": "to_snake", "args": {"upper": true }},
```

###TableJustifierCommand.py
テーブル構造の文字列をスペースパディングで整形します。

キー設定例
```json:key-config
  { "keys": ["alt+shift+j"], "command": "table_justifier", "args": {"separator": "|" }}
```
整形前例
```
    |column1|coln2|c3|
     |v1|value2|val3|
     |value1|v2|value3|
```
整形後例
```
      |column1|coln2 |c3    |
      |v1     |value2|val3  |
      |value1 |v2    |value3|
```
##macro
| ファイル名| 内容| 
|:-----------|:------------|
| Move Multi Forwrod Line.sublime-macro| 5行行下移動| 
| Move Multi Back Line.sublime-macro| 5行上移動| 
| Move Multi Forwrod Line Selection.sublime-macro| 5行下移動かつ範囲選択| 
| Move Multi Back Line Selection.sublime-macro| 5行上移動かつ範囲選択| 
