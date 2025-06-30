
# 应用目录仓库规范

前后端应用统一存放于同一个仓库中，本文档定义了目录结构、构建流程、产物组织及部署规范，适用于 GM 系统一体化管理流程。

## 📁 仓库目录结构

```text
app/
├── web/             # 前端应用目录
│   └── build.sh     # 前端构建脚本
├── backend/         # 后端应用目录
│   └── build.sh     # 后端构建脚本
├── Makefile         # 根构建脚本
├── dist/            # 构建产物输出目录
├── README.md        # 项目说明文档
├── VERSION          # 项目版本号（可选）
├── CHANGELOG        # 项目变更日志（可选）
├── LICENSE.txt      # 开源协议文件（可选）
├── .gitignore       # Git 忽略规则（可选）
├── install.sh       # 应用安装脚本（可选）
```

## ⚙️ 构建要求

- `web/` 目录必须存在 `build.sh`，用于前端构建
- `backend/` 目录必须存在 `build.sh`，用于后端构建
- 根目录 `Makefile` 用于统一调度前后端构建流程

## 🧱 Makefile 模板

```makefile
# 项目构建Makefile

# 定义构建目标目录
DIST_DIR := dist

# 默认目标：执行完整构建
all: build-web build-backend

build-web:
	@echo "开始构建前端应用..."
	@chmod +x web/build.sh
	@cd web && ./build.sh
	@echo "前端应用构建完成!"

# 构建后端应用
build-backend:
	@echo "开始构建后端应用..."
	@chmod +x backend/build.sh
	@cd backend && ./build.sh
	@echo "后端应用构建完成!"

# 清理构建结果
clean:
	@echo "清理构建结果..."
	@rm -rf $(DIST_DIR)
	@cd web && ./build.sh clean
	@cd backend && ./build.sh clean
	@echo "清理完成!"

# 帮助信息
help:
	@echo "可用命令:"
	@echo "  make all       - 构建前端和后端应用"
	@echo "  make build-web - 仅构建前端应用"
	@echo "  make build-backend - 仅构建后端应用"
	@echo "  make clean     - 清理构建结果"
	@echo "  make help      - 显示此帮助信息"

.PHONY: all build-web build-backend clean help
```

## 🛠️ 构建指令

```bash
# 构建前后端
make all

# 构建前端
make build-web

# 构建后端
make build-backend

# 清理构建目录
make clean
```

## 📦 构建产物结构

执行 `make all` 后生成结构：

```text
dist/
├── web/
│   ├── index.html
│   ├── static/
│   └── icon.png
├── backend/
│   ├── main
│   └── install.sh
```

### 制品发布路径映射

| 构建产物路径      | 制品发布项目路径           |
|-------------------|--------------------|
| `dist/web/`       | `example/app/www/` |
| `dist/backend/`   | `example/app/bin/` |

### 制品项目结构示例规范

```text
example/
├── tmp/                    # 临时文件目录（必须）
├── cache/                  # 缓存目录（必须）
├── logs/                   # 日志目录（必须）
├── data/                   # 应用数据目录（必须）
│   └── config.yaml         # 应用配置文件（可选）
├── app/                    # 应用主目录（必须）
│   ├── www/                # 前端资源（必须）
│   │   ├── index.html
│   │   ├── static/
│   │   └── icon.png
│   ├── bin/                # 后端程序（必须）
│   │   ├── main
│   │   └── install.sh
│   └── app.json            # 应用元信息文件（必须）
```

## 🧾 app.json 元信息规范

```json
{
  "name": "official/example",
  "title": "示例应用",
  "icon": "./icon.png",
  "version": "1.0.0",
  "sys_req": ["centos", "ubuntu"],
  "app_req": ["nginx", "redis"],
  "conflict": ["old-webhook"],
  "icon_menu": [
    {
      "name": "打开所在文件夹",
      "icon": "./open.png",
      "call_func": "openWithPath"
    }
  ]
}
```

### 字段说明

| 字段名 | 类型 | 必填 | 示例 | 描述 |
|--------|------|------|------|------|
| name | string | ✅ | "xiaoming/webhook" | 应用唯一标识（建议加组织前缀） |
| title | string | ✅ | "Webhook 管理器" | 应用显示名称 |
| icon | string | ✅ | "./icon.png" | 图标路径（建议64x64 PNG/SVG） |
| version | string | ✅ | "1.0.0" | 语义化版本号 |
| sys_req | string[] | 否 | ["centos"] | 系统依赖要求 |
| app_req | string[] | 否 | ["nginx"] | 应用依赖要求 |
| conflict | string[] | 否 | ["old-webhook"] | 冲突应用列表 |
| icon_menu | object[] | 否 | - | 自定义快捷菜单 |

## 🧩 icon_menu 示例

```json
{
  "name": "打开所在文件夹",
  "icon": "./open.png",
  "call_func": "openWithPath"
}
```