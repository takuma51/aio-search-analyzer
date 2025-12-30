import os
import datetime
import pandas as pd
from serpapi import GoogleSearch

def main():
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        print("Error: API Keyが見つかりません。")
        return

    keyword = "Technical SEO"
    print(f"検索キーワード: {keyword} のデータを取得中...")

    params = {
        "engine": "google",
        "q": keyword,
        "gl": "us",
        "hl": "en",
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results.get("organic_results", [])

    # データをリストにまとめる
    data_list = []
    today = datetime.date.today()

    for result in organic_results[:10]: # 上位10件取得
        item = {
            "date": today,
            "rank": result.get("position"),
            "title": result.get("title"),
            "url": result.get("link"),
            "snippet": result.get("snippet")
        }
        data_list.append(item)

    # DataFrame（表形式）に変換
    df = pd.DataFrame(data_list)

    # CSVファイルに保存（追記モード）
    csv_filename = "seo_data.csv"
    
    if os.path.exists(csv_filename):
        # ファイルがすでにある場合は、ヘッダーなしで追記
        df.to_csv(csv_filename, mode='a', header=False, index=False)
        print(f"既存の {csv_filename} にデータを追記しました。")
    else:
        # 初回はヘッダー付きで新規作成
        df.to_csv(csv_filename, mode='w', header=True, index=False)
        print(f"新しく {csv_filename} を作成しました。")

if __name__ == "__main__":
    main()
