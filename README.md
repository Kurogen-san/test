# AIチャットアプリ

Djangoで構築されたAIチャットアプリケーションです。[digimatch.jp](https://digimatch.jp/)のデザインを参考に、モダンで美しいUIを実装しています。

## 機能

- 🤖 **AIチャット機能**: OpenAI APIを使用したリアルタイムチャット
- 📱 **レスポンシブデザイン**: モバイル・デスクトップ対応
- 🎨 **モダンUI**: Tailwind CSSを使用した美しいデザイン
- 📄 **3つのページ**: ホーム、アバウト、お問い合わせ
- 💾 **データベース保存**: チャット履歴の保存機能

## 技術スタック

- **バックエンド**: Django 5.2.4
- **フロントエンド**: HTML5, CSS3, JavaScript
- **UIフレームワーク**: Tailwind CSS
- **AI**: OpenAI API
- **データベース**: SQLite
- **アイコン**: Font Awesome

## セットアップ手順

### 1. リポジトリのクローン
```bash
git clone <repository-url>
cd aichat
```

### 2. 仮想環境の作成とアクティベート
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate  # Windows
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定
`.env`ファイルを作成し、以下の内容を設定してください：

```env
# OpenAI API設定
OPENAI_API_KEY=your_openai_api_key_here

# Django設定
SECRET_KEY=your_django_secret_key_here
DEBUG=True
```

### 5. データベースのマイグレーション
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 開発サーバーの起動
```bash
python manage.py runserver
```

ブラウザで `http://127.0.0.1:8000/` にアクセスしてください。

## プロジェクト構造

```
aichat/
├── aichat/                 # Djangoプロジェクト設定
│   ├── settings.py        # プロジェクト設定
│   ├── urls.py           # メインURL設定
│   └── wsgi.py           # WSGI設定
├── chat/                  # チャットアプリ
│   ├── models.py         # データベースモデル
│   ├── views.py          # ビュー関数
│   ├── urls.py           # アプリURL設定
│   └── migrations/       # データベースマイグレーション
├── templates/             # HTMLテンプレート
│   ├── base.html         # ベーステンプレート
│   └── chat/             # チャットアプリテンプレート
│       ├── home.html     # ホームページ
│       ├── about.html    # アバウトページ
│       └── contact.html  # お問い合わせページ
├── static/               # 静的ファイル
├── manage.py             # Django管理コマンド
├── requirements.txt      # Python依存関係
└── README.md            # このファイル
```

## ページ構成

### 1. ホームページ (`/`)
- AIチャット機能
- ヒーローセクション
- 特徴紹介
- モダンなチャットインターフェース

### 2. アバウトページ (`/about/`)
- 会社情報
- ミッション・ビジョン
- 技術スタック
- 実績紹介

### 3. お問い合わせページ (`/contact/`)
- お問い合わせフォーム
- 連絡先情報
- よくある質問

## API エンドポイント

### POST `/api/chat/`
AIチャットAPI

**リクエスト:**
```json
{
    "message": "ユーザーのメッセージ"
}
```

**レスポンス:**
```json
{
    "response": "AIの応答",
    "status": "success"
}
```

## 環境変数

| 変数名 | 説明 | 必須 |
|--------|------|------|
| `OPENAI_API_KEY` | OpenAI APIキー | はい |
| `SECRET_KEY` | Django秘密鍵 | はい |
| `DEBUG` | デバッグモード | いいえ |

## 開発者向け情報

### 新しい機能の追加
1. `chat/views.py`にビュー関数を追加
2. `chat/urls.py`にURLパターンを追加
3. `templates/chat/`にテンプレートを作成

### データベースの変更
```bash
python manage.py makemigrations
python manage.py migrate
```

### 静的ファイルの収集
```bash
python manage.py collectstatic
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 貢献

プルリクエストやイシューの報告を歓迎します。

## サポート

ご質問やご要望がございましたら、お気軽にお問い合わせください。 