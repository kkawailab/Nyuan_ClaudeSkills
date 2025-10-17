# Nyuan (ニャン) Claude Code Custom Skill

Claude Codeのすべての応答文末に「ニャン」をつけて、猫のような話し方にするカスタムスキルです🐱

## 概要

このカスタムスキルは、以下の2つの方法で使用できます：

1. **Claude.ai Skills**: `SKILL.md`ファイルをClaude.aiにアップロードして使用
2. **Claude Code Hooks**: `UserPromptSubmit`フックを使用して自動的に指示を注入

どちらの方法でも、Claudeが猫のような話し方で応答するようになります。

## 特徴

- ✨ すべての応答が「ニャン」で終わる
- 🔧 簡単なセットアップ（設定ファイル1つ）
- 🎯 プロジェクト単位またはグローバルで有効化可能
- 🐍 Python3で実装（依存関係なし）
- 🔄 いつでも有効/無効の切り替えが可能

## 必要要件

- Claude Code（最新版推奨）
- Python 3.6以上

## インストール方法

以下の2つの方法から選択できます：

### 方法A: Claude.ai Skills（推奨・最も簡単）

Claude.ai Pro/Max/Team/Enterpriseプランで利用可能な公式のSkills機能を使用します。

#### ステップ1: SKILL.mdファイルをダウンロード

```bash
# リポジトリ全体をクローン
git clone https://github.com/kkawailab/Nyuan_ClaudeSkills.git

# または、SKILL.mdファイルのみダウンロード
curl -O https://raw.githubusercontent.com/kkawailab/Nyuan_ClaudeSkills/main/SKILL.md
```

#### ステップ2: Claude.aiにアップロード

1. [Claude.ai](https://claude.ai)にログイン
2. 設定（Settings）を開く
3. 「Skills」セクションに移動
4. 「Add Skill」または「Upload Skill」をクリック
5. `SKILL.md`ファイルを選択してアップロード

#### ステップ3: スキルを有効化

1. アップロードされた「Nyuan (ニャン)」スキルを確認
2. 必要に応じてスキルを有効化
3. 新しい会話を開始

これだけで、Claudeが「ニャン」をつけて応答するようになります！

**メリット：**
- 設定ファイル不要
- スクリプト実行不要
- Claude.ai上で簡単にON/OFF切り替え可能
- すべてのClaude.ai会話で使用可能

---

### 方法B: Claude Code Hooks（上級者向け）

Claude CodeのUserPromptSubmitフック機能を使用します。

#### ステップ1: リポジトリをクローン

```bash
git clone https://github.com/kkawailab/Nyuan_ClaudeSkills.git
cd Nyuan_ClaudeSkills
```

#### ステップ2: スクリプトに実行権限を付与

```bash
chmod +x add_nyuan.py
```

#### ステップ3: 設定ファイルを作成

以下のいずれかの方法で設定します。

### 方法1: プロジェクト固有の設定

特定のプロジェクトでのみこのスキルを有効にしたい場合に使用します。

1. プロジェクトのルートディレクトリに`.claude`ディレクトリを作成：

```bash
mkdir -p .claude
```

2. `.claude/config.json`ファイルを作成し、以下の内容を記述：

```json
{
  "hooks": {
    "UserPromptSubmit": {
      "command": "python3 /absolute/path/to/Nyuan_ClaudeSkills/add_nyuan.py"
    }
  }
}
```

**注意**: `/absolute/path/to/Nyuan_ClaudeSkills/`の部分は、実際のクローンしたディレクトリの絶対パスに置き換えてください。

**パスの確認方法**:
```bash
cd Nyuan_ClaudeSkills
pwd  # 絶対パスが表示されます
```

3. Claude Codeを再起動するか、新しいセッションを開始

### 方法2: グローバル設定

すべてのプロジェクトでこのスキルを有効にしたい場合に使用します。

1. Claude Codeのグローバル設定ディレクトリを作成（存在しない場合）：

```bash
mkdir -p ~/.config/claude
```

2. `~/.config/claude/config.json`ファイルを作成または編集し、以下の内容を追加：

```json
{
  "hooks": {
    "UserPromptSubmit": {
      "command": "python3 /absolute/path/to/Nyuan_ClaudeSkills/add_nyuan.py"
    }
  }
}
```

**注意**: パスは絶対パスで指定してください。

3. Claude Codeを再起動

## 使い方

### 基本的な使い方

設定完了後、Claude Codeを起動して普通に質問すると、すべての応答が「ニャン」で終わるようになります。

**例：**

```
あなた: ファイルを読み込んで
Claude: ファイルを読み込みますニャン

あなた: このコードを説明して
Claude: このコードは配列をソートする関数ですニャン。時間計算量はO(n log n)ですニャン

あなた: ありがとう
Claude: どういたしましてニャン。他に何かお手伝いできることはありますかニャン？
```

### 動作確認

スキルが正しく動作しているか確認するには：

```bash
# Claude Codeを起動
claude

# 簡単な質問をしてみる
> こんにちは

# 応答が「こんにちはニャン」のように「ニャン」で終われば成功
```

### トラブルシューティング

**「ニャン」がつかない場合：**

1. 設定ファイルのパスが正しいか確認
```bash
# スクリプトを直接実行してテスト
echo "test" | python3 /path/to/add_nyuan.py
# JSON出力が表示されればOK
```

2. Claude Codeを完全に再起動
```bash
# すべてのClaude Codeプロセスを終了してから再起動
pkill claude
claude
```

3. 設定ファイルのJSON構文が正しいか確認
```bash
# JSONの構文チェック
python3 -m json.tool ~/.config/claude/config.json
# またはプロジェクト固有の場合
python3 -m json.tool .claude/config.json
```

**パーミッションエラーが出る場合：**

```bash
chmod +x add_nyuan.py
```

## 無効化する方法

### 一時的に無効化

`config.json`の該当部分をコメントアウト（JSONはコメント非対応なので削除が必要）：

```json
{
  "hooks": {
  }
}
```

または、config.jsonファイルをリネーム：

```bash
# プロジェクト固有の場合
mv .claude/config.json .claude/config.json.bak

# グローバル設定の場合
mv ~/.config/claude/config.json ~/.config/claude/config.json.bak
```

### 完全に削除

```bash
# プロジェクト固有の設定を削除
rm -rf .claude

# グローバル設定から削除
rm ~/.config/claude/config.json
```

## 仕組みの詳細

### アーキテクチャ

```
ユーザー入力
    ↓
UserPromptSubmitフック発火
    ↓
add_nyuan.py実行
    ↓
追加の指示を注入
    ↓
Claude Codeが処理（「ニャン」付きで応答）
    ↓
ユーザーに応答表示
```

### UserPromptSubmitフックとは

`UserPromptSubmit`は、Claude Codeが提供するフックの1つで、ユーザーがプロンプトを送信した直後、Claudeが処理を開始する前に実行されます。

このフックでできること：
- ユーザーのプロンプトに追加のコンテキストを注入
- プロンプトの内容を検証
- 特定の条件でプロンプトをブロック

### スクリプトの動作

`add_nyuan.py`は以下の処理を行います：

1. ユーザーのプロンプトを標準入力から読み込み
2. 「すべての文末にニャンをつける」という指示を準備
3. JSON形式で以下を出力：
   - `approval`: "approved"（プロンプトを承認）
   - `additionalContext`: 追加の指示

この出力により、Claude Codeは元のプロンプトに加えて、追加の指示も考慮して応答を生成します。

### コードの詳細

```python
# JSON形式で結果を返す
result = {
    "approval": "approved",  # プロンプトを承認
    "additionalContext": additional_context  # 追加の指示
}
```

`additionalContext`に含まれる指示が、Claudeの応答スタイルを変更します。

## カスタマイズ

このスキルをベースに、他のカスタマイズも可能です：

### 語尾を変更する例

`add_nyuan.py`の`additional_context`を編集：

```python
# 「です・ます」調に変更
additional_context = """
IMPORTANT: 丁寧な敬語で応答してください。
"""

# 関西弁に変更
additional_context = """
IMPORTANT: 関西弁で応答してください。語尾に「やで」「やねん」をつけてください。
"""
```

### 複数のフックを組み合わせる

`config.json`で複数のフックを設定可能：

```json
{
  "hooks": {
    "UserPromptSubmit": {
      "command": "python3 /path/to/add_nyuan.py"
    },
    "PreToolUse": {
      "command": "python3 /path/to/validate_tools.py"
    }
  }
}
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 貢献

プルリクエストや問題報告を歓迎します！

## 作者

[@kkawailab](https://github.com/kkawailab)

## 参考リンク

- [Claude Code公式ドキュメント](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Hooks](https://docs.claude.com/en/docs/claude-code/hooks)
