※python 3.6.7→最新バージョンうまく動かなかったのでサンプルにそろえた。
※windowのためpythonLuncher使ってますがその他のかたはpyenvとか？

準備
py -3.6 -m pip install paho-mqtt

実行時
py -3.6 pub.py [brockerIP] [port] [count] [json] 
