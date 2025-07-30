# QQ 相册导出工具

📥 自动下载 QQ 空间相册（包括“仅自己可见”），并打包为 ZIP，支持上传到 GitHub。

## 使用步骤

1. 编辑 `config.py`，填入你自己的 QQ Cookie 和 QQ 号
2. 安装依赖：

```bash
pip install -r requirements.txt
```

3. 运行抓取和打包脚本：

```bash
python download_qq_album.py
```

4. （可选）上传到你的 GitHub 仓库：

```bash
python upload_to_github.py
```

## 安全提示

此工具仅供本人备份自己的相册使用，严禁用于访问他人隐私数据。
