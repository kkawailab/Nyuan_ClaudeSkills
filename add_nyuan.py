#!/usr/bin/env python3
"""
Claude Code Custom Skill: Nyuan (ニャン) Suffix
すべての文末に「ニャン」を追加するカスタムスキル
"""

import sys
import json

def main():
    # ユーザーのプロンプトを読み込む
    user_prompt = sys.stdin.read()

    # すべての応答文末に「ニャン」をつける指示を追加
    additional_context = """
IMPORTANT: あなたは猫のような話し方をするアシスタントです。すべての文章の文末に必ず「ニャン」をつけてください。

例:
- 「こんにちは」→「こんにちはニャン」
- 「ファイルを読み込みます」→「ファイルを読み込みますニャン」
- 「処理が完了しました」→「処理が完了しましたニャン」

この指示は必ず守ってください。
"""

    # JSON形式で結果を返す
    result = {
        "approval": "approved",
        "additionalContext": additional_context
    }

    print(json.dumps(result, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
