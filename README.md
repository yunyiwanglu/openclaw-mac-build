# OpenClaw桌面版 macOS DMG 构建指南

## 文件说明

```
├── .github/
│   └── workflows/
│       └── build-dmg.yml    # GitHub Actions workflow
├── dmg_settings.py          # DMG 构建设置
└── README.md               # 本文件
```

## 使用步骤

### 1. 创建 GitHub 仓库

在 GitHub 上创建一个新仓库（例如 `openclaw-mac-build`）

### 2. 上传文件

将以下文件上传到仓库：

```bash
# 方式一：通过 GitHub 网页上传
# 方式二：通过 git 命令

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/openclaw-mac-build.git
git push -u origin main
```

### 3. 上传 .app 文件

由于 `.app` 文件较大（~350MB），推荐使用 **GitHub Release** 或 **Git LFS**：

**方式一：Git LFS（推荐）**
```bash
git lfs install
git lfs track "*.app"
git lfs track "*.zip"
git add .gitattributes
git add OpenClaw桌面版.app
git commit -m "Add app"
git push
```

**方式二：先创建 Release，再上传**
1. 先推送代码（不含 .app）
2. 在 GitHub 创建 Release
3. 上传 ZIP 文件作为 Release asset
4. 修改 workflow 添加下载步骤

### 4. 触发构建

- **自动触发**：推送到 main 分支时自动构建
- **手动触发**：在 Actions 页面点击 "Run workflow"

### 5. 下载 DMG

构建完成后：
- 在 **Actions → Artifacts** 下载（保留 30 天）
- 或在 **Releases** 页面下载（如果启用了 Release 步骤）

## 注意事项

1. **文件大小限制**：GitHub 单文件限制 100MB，仓库总大小建议 < 1GB
2. **Actions 时间限制**：macOS runner 每月有免费额度（2000 分钟）
3. **签名问题**：未签名的 DMG 在 macOS 上打开时需要右键 → 打开

## 自定义

修改 `dmg_settings.py` 可以：
- 更改 DMG 窗口大小
- 添加背景图片
- 调整图标位置
- 更改压缩级别
