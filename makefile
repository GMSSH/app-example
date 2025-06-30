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