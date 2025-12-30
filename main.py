import datetime

def main():
    # 現在時刻を取得（日本時間に調整も可能ですが、まずはUTCで）
    now = datetime.datetime.now()
    
    print("="*30)
    print(f"SEO Analysis Job Started at: {now}")
    print("Hello, GitHub Actions! The environment is ready.")
    print("="*30)

if __name__ == "__main__":
    main()
