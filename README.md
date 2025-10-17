# Nyuan (ニャン) Claude Code Custom Skill

すべてのClaude Codeの応答文末に「ニャン」をつけるカスタムスキルです。

## セットアップ方法

### 1. プロジェクト固有の設定（推奨）

このディレクトリで作業する時のみ有効にする場合：

```bash
# .claude/config.jsonを作成
mkdir -p .claude
```

`.claude/config.json`に以下を追加：

```json
{
  "hooks": {
    "UserPromptSubmit": {
      "command": "python3 add_nyuan.py"
    }
  }
}
```

### 2. グローバル設定

すべてのプロジェクトで有効にする場合：

`~/.config/claude/config.json`に以下を追加：

```json
{
  "hooks": {
    "UserPromptSubmit": {
      "command": "python3 /home/katzkawai/Nyuan_ClaudeSkills/add_nyuan.py"
    }
  }
}
```

## 使い方

設定後、Claude Codeを起動すると、すべての応答が「ニャン」で終わるようになります。

例：
- 「ファイルを読み込みますニャン」
- 「処理が完了しましたニャン」
- 「こんにちはニャン」

## 無効化する方法

config.jsonから該当のhook設定を削除するか、コメントアウトしてください。

## 仕組み

`UserPromptSubmit`フックを使用して、ユーザーのプロンプトが送信される前に追加の指示を注入します。この指示により、Claudeは自動的にすべての文末に「ニャン」をつけるようになります。
