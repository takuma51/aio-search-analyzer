import os
from serpapi import GoogleSearch
import pandas as pd

def main():
    # GitHub Secretsから鍵を取り出す
    api_key = os.getenv("SERPAPI_KEY")
    
    if not api_key:
        print("Error: API Keyが見つかりません。GitHub Secretsを設定してください。")
        return

    print("Google検索を開始します...")

    # 検索パラメータの設定
    params = {
        "engine": "google",
        "q": "Technical SEO",  # 検索したいキーワード
        "gl": "us",            # 国: アメリカ (AIOの分析ならUSが面白い)
        "hl": "en",            # 言語: 英語
        "api_key": api_key
    }

    # 検索実行
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results.get("organic_results", [])

    # データを整理して表示
    print(f"\n検索キーワード: {params['q']}")
    print("-" * 50)
    
    data = []
    for result in organic_results[:5]: # 上位5件だけ表示
        title = result.get("title")
        link = result.get("link")
        position = result.get("position")
        
        print(f"{position}位: {title}")
        print(f"URL: {link}\n")
        
        data.append({"rank": position, "title": title, "url": link})

    print("-" * 50)
    print("✅ 分析完了！このデータを保存・分析して記事に使います。")

if __name__ == "__main__":
    main()
