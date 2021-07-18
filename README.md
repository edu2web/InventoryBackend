# Kivy Sheets Inventory Manage

Google spread sheets を在庫管理の　Backend　として　利用する Kivy サンプルです。

# Backend

Google spread sheets 

## API 設定

Google Cloud Platformのプロジェクトを作成  
Google Drive APIを有効に  
Google Sheets APIを有効に  
外部アプリからスプレッドシートにアクセスするための認証情報を設定  
（JSONを作成、このプロジェクトのフォルダに入れてください）

## スプレッドシートを作成
InventoryBackend シート作成 
client_emailに共有

# Frontend

Python Kivyを利用する

スプレッドシートを操作するには、2つのライブラリを使います。pipでインストールしてください。
	
pip install gspread
pip install oauth2client

# 実行

python main.py

## Ref

* https://stackoverflow.com/questions/66897185/take-user-input-from-kivy-app-and-append-to-google-sheets-using-python
