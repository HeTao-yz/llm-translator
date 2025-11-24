# llm-translator

使用大语言模型进行游戏内不同语种玩家的对话翻译，插件默认使用 deepseek-chat 大语言模型进行翻译工作。

## 插件适用场景/优势

当服务器内有不同语种玩家时，使用此插件可以良好改善沟通情况。
使用大语言模型翻译，精准度相较传统机器翻译准确率更高，适应性更强。

## 如何配置

1. 插件第一次加载成功后，将在 `/config/llm-translator/` 文件夹下生成配置文件
  
2. 配置文件默认使用 `deepseek-chat` 模型进行中英翻译，若符合此需求，仅需在api_key处填写你的api密钥即可使用。否则请参考下方配置文件进行修改。
  

### 配置文件

```json
{
    # 第一语言，默认值 zh_cn
    "first_language": "zh_cn",
    # 第二语言，默认值 en_us
    "secondary_language": "en_us",
    # base_url地址接口，默认值 https://api.deepseek.com
    "base_url": "https://api.deepseek.com",
    # 模型，默认值 https://api.deepseek.com
    "model": "deepseek-chat",
    # api密钥，默认情况下仅需配置此条即可 
    "api_key": "请在此处填写API",
}
```

## 如何使用

游戏内输入 `t [翻译信息]` 即可使用,发送信息时，信息将提交至模型进行翻译后再次发出。
<img width="651" height="219" alt="屏幕截图 2025-11-24 185838" src="https://github.com/user-attachments/assets/55e57abb-eeff-4ff3-9071-4aeeebee9b98" />

## 灵感

本插件的开发灵感来源于 MCDR插件 [SimpleTranslator](https://github.com/skuzow/simple-translator)
