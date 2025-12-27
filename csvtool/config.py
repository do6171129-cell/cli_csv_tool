import os
import json

CONFIG_PATH = "data/config.json"


def save_config(path):
    #  保存する内容を dict にする
    config = {
        "last_path": path
    }

    #  config.json を置くディレクトリを保証する
    config_dir = os.path.dirname(CONFIG_PATH)
    os.makedirs(config_dir, exist_ok=True)

    #  CONFIG_PATH に JSON として書き込む
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def load_config():
    if not os.path.exists(CONFIG_PATH):
        return None

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
        return config.get("last_path")
