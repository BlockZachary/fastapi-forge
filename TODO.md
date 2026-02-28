# FastAPI-Forge 开发任务跟踪

> 项目版本: v0.1.0 (MVP)  
> 开始日期: 2026-02-28

---

## 📋 任务状态说明

- ⬜ **TODO** - 待开始
- 🔄 **IN PROGRESS** - 进行中
- ✅ **DONE** - 已完成
- ❌ **BLOCKED** - 阻塞中

---

## 阶段一：项目初始化 (Project Setup)

### Issue #1: 初始化 uv 项目结构

- **状态**: ✅ DONE
- **描述**: 使用 uv 创建项目基础结构，配置 pyproject.toml
- **任务**:
  - [x] 创建 `fastapi_forge/` 包目录
  - [x] 配置 `pyproject.toml` (项目元数据、依赖、CLI 入口)
  - [x] 创建 `README.md`
  - [x] 创建 `.gitignore`
  - [x] 创建 `LICENSE` (MIT)
- **Git Commit**: `feat: initialize uv project structure with pyproject.toml`

### Issue #2: 实现基础 CLI 框架

- **状态**: ✅ DONE
- **描述**: 使用 Typer 搭建 CLI 基础框架
- **任务**:
  - [x] 安装 Typer, Rich 依赖
  - [x] 创建 `fastapi_forge/cli.py` CLI 入口
  - [x] 实现 `forge version` 命令
  - [x] 实现 `forge --help` 帮助信息
  - [x] 配置 `[project.scripts]` CLI 入口点
- **Git Commit**: `feat: implement basic CLI framework with Typer`

### Issue #3: 实现交互式问答系统

- **状态**: ✅ DONE
- **描述**: 使用 Questionary 实现交互式项目配置
- **任务**:
  - [x] 安装 Questionary 依赖
  - [x] 创建 `fastapi_forge/prompts.py` 问答模块
  - [x] 实现项目基础信息收集 (名称、描述、作者)
  - [x] 实现包管理器选择 (uv/Poetry/pip)
  - [x] 实现数据库选择 (PostgreSQL/MySQL/SQLite/None)
  - [x] 实现功能模块选择 (Auth/Docker/Redis 等)
- **Git Commit**: `feat: implement interactive prompts with Questionary`

### Issue #4: 创建项目配置数据模型

- **状态**: ✅ DONE
- **描述**: 使用 Pydantic 定义项目配置数据结构
- **任务**:
  - [x] 创建 `fastapi_forge/models.py`
  - [x] 定义 `ProjectConfig` 数据类
  - [x] 定义 `DatabaseType` 枚举
  - [x] 定义 `PackageManager` 枚举
  - [x] 添加配置验证逻辑
- **Git Commit**: `feat: add ProjectConfig model with Pydantic`

---

## 阶段二：模板系统 (Template System)

### Issue #5: 创建 Jinja2 模板引擎

- **状态**: ✅ DONE
- **描述**: 搭建模板渲染基础设施
- **任务**:
  - [x] 安装 Jinja2 依赖
  - [x] 创建 `fastapi_forge/generator.py` 生成器模块
  - [x] 实现模板加载和渲染逻辑
  - [x] 实现目录结构生成逻辑
- **Git Commit**: `feat: implement Jinja2 template engine`

### Issue #6: 创建基础项目模板

- **状态**: ✅ DONE
- **描述**: 创建核心项目文件模板
- **任务**:
  - [x] 创建 `templates/base/` 目录结构
  - [x] 创建 `pyproject.toml.jinja` (uv 版本)
  - [x] 创建 `pyproject.toml.jinja` (Poetry 版本)
  - [x] 创建 `README.md.jinja`
  - [x] 创建 `.gitignore.jinja`
  - [x] 创建 `config.yaml.jinja`
- **Git Commit**: `feat: add base project templates`

### Issue #7: 创建 FastAPI 应用模板

- **状态**: ✅ DONE
- **描述**: 创建 FastAPI 应用核心文件模板
- **任务**:
  - [x] 创建 `templates/base/app/` 目录
  - [x] 创建 `main.py.jinja`
  - [x] 创建 `server.py.jinja`
  - [x] 创建 `__init__.py.jinja`
  - [x] 创建 `core/config.py.jinja`
  - [x] 创建 `core/deps.py.jinja`
  - [x] 创建 `api/health_api.py.jinja`
- **Git Commit**: `feat: add FastAPI application templates`

### Issue #8: 创建数据库模板

- **状态**: ✅ DONE
- **描述**: 创建数据库相关文件模板
- **任务**:
  - [x] 创建 `templates/database/` 目录
  - [x] 创建 `core/database.py.jinja`
  - [x] 创建 `models/base.py.jinja`
  - [x] 创建 `models/user.py.jinja`
  - [x] 创建 `daos/user_dao.py.jinja`
  - [x] 创建 Alembic 配置模板
- **Git Commit**: `feat: add database and Alembic templates`

### Issue #9: 创建认证模块模板

- **状态**: ✅ DONE
- **描述**: 创建 JWT 认证相关文件模板
- **任务**:
  - [x] 创建 `templates/auth/` 目录
  - [x] 创建 `core/auth.py.jinja`
  - [x] 创建 `api/auth_api.py.jinja`
  - [x] 创建 `services/auth_service.py.jinja`
  - [x] 创建 `schemas/auth_schema.py.jinja`
- **Git Commit**: `feat: add JWT authentication templates`

### Issue #10: 创建 Docker 模板

- **状态**: ✅ DONE
- **描述**: 创建 Docker 相关文件模板
- **任务**:
  - [x] 创建 `templates/docker/` 目录
  - [x] 创建 `Dockerfile.jinja`
  - [x] 创建 `docker-compose.yml.jinja`
  - [x] 创建 `.dockerignore.jinja`
- **Git Commit**: `feat: add Docker configuration templates`

### Issue #11: 创建测试框架模板

- **状态**: ✅ DONE
- **描述**: 创建 Pytest 测试相关文件模板
- **任务**:
  - [x] 创建 `templates/tests/` 目录
  - [x] 创建 `conftest.py.jinja`
  - [x] 创建 `pytest.ini.jinja`
  - [x] 创建示例测试文件模板
- **Git Commit**: `feat: add Pytest testing templates`

---

## 阶段三：核心命令实现 (Core Commands)

### Issue #12: 实现 `forge create` 命令

- **状态**: ✅ DONE
- **描述**: 实现项目创建主命令
- **任务**:
  - [x] 整合交互式问答
  - [x] 整合模板生成器
  - [x] 实现项目目录创建
  - [x] 实现文件写入逻辑
  - [x] 添加进度条显示
  - [x] 添加成功/失败提示
- **Git Commit**: `feat: implement forge create command`

### Issue #13: 实现非交互模式

- **状态**: ✅ DONE
- **描述**: 支持命令行参数跳过交互
- **任务**:
  - [x] 添加 `--no-interactive` 参数
  - [x] 添加 `--package-manager` 参数
  - [x] 添加 `--database` 参数
  - [x] 添加 `--auth` 参数
  - [x] 添加 `--docker` 参数
  - [x] 参数验证和错误处理
- **Git Commit**: `feat: add non-interactive mode with CLI flags`

---

## 阶段四：代码质量 (Quality Assurance)

### Issue #14: 添加 Ruff 配置模板

- **状态**: ✅ DONE
- **描述**: 创建代码质量工具配置
- **任务**:
  - [x] 创建 `ruff.toml.jinja` 模板
  - [x] 创建 `.pre-commit-config.yaml.jinja` 模板
- **Git Commit**: `feat: add Ruff and pre-commit templates`

### Issue #15: 添加 GitHub Actions CI 模板

- **状态**: ✅ DONE
- **描述**: 创建 CI/CD 配置模板
- **任务**:
  - [x] 创建 `templates/ci/` 目录
  - [x] 创建 `.github/workflows/ci.yml.jinja`
- **Git Commit**: `feat: add GitHub Actions CI template`

### Issue #16: 添加 VS Code 配置模板

- **状态**: ✅ DONE
- **描述**: 创建编辑器配置模板
- **任务**:
  - [x] 创建 `.vscode/settings.json.jinja`
  - [x] 创建 `.vscode/launch.json.jinja`
- **Git Commit**: `feat: add VS Code configuration templates`

---

## 阶段五：测试与文档 (Testing & Documentation)

### Issue #17: 编写 CLI 单元测试

- **状态**: ✅ DONE
- **描述**: 为 CLI 工具编写测试
- **任务**:
  - [x] 创建 `tests/test_cli.py`
  - [x] 创建 `tests/test_generator.py`
  - [x] 创建 `tests/test_templates.py`
  - [x] 达到 80%+ 测试覆盖率
- **Git Commit**: `test: add unit tests for CLI and generator`

### Issue #18: 完善项目文档

- **状态**: ✅ DONE
- **描述**: 编写用户文档
- **任务**:
  - [x] 完善 `README.md`
  - [x] 添加安装说明
  - [x] 添加使用示例
  - [x] 添加贡献指南 `CONTRIBUTING.md`
  - [x] 添加变更日志 `CHANGELOG.md`
- **Git Commit**: `docs: add comprehensive documentation`

---

## 阶段六：发布准备 (Release Preparation)

### Issue #19: 配置 PyPI 发布

- **状态**: ✅ DONE
- **描述**: 准备 PyPI 发布流程
- **任务**:
  - [x] 完善 `pyproject.toml` 元数据
  - [x] 添加 `LICENSE` 文件
  - [ ] 测试本地构建 `uv build`
  - [ ] 测试 TestPyPI 发布
- **Git Commit**: `chore: prepare for PyPI release`

### Issue #20: 发布 v0.1.0 MVP

- **状态**: ⬜ TODO
- **描述**: 发布首个 MVP 版本
- **任务**:
  - [ ] 创建 Git tag `v0.1.0`
  - [ ] 发布到 PyPI
  - [ ] 发布 GitHub Release
  - [ ] 社区宣传
- **Git Commit**: `release: v0.1.0 MVP`

---

## 📊 进度统计

| 阶段       | 总任务 | 已完成 | 进度    |
| ---------- | ------ | ------ | ------- |
| 项目初始化 | 4      | 4      | 100%    |
| 模板系统   | 7      | 7      | 100%    |
| 核心命令   | 2      | 2      | 100%    |
| 代码质量   | 3      | 3      | 100%    |
| 测试文档   | 2      | 2      | 100%    |
| 发布准备   | 2      | 1      | 50%     |
| **总计**   | **20** | **19** | **95%** |

---

## 📝 开发日志

### 2026-02-28

- 创建设计文档 `DESIGN.md`
- 创建任务跟踪文档 `TODO.md`
- ✅ 完成 Issue #1: 初始化 uv 项目结构
- ✅ 完成 Issue #2: 实现基础 CLI 框架 (Typer + Rich)
- ✅ 完成 Issue #3: 实现交互式问答系统 (Questionary)
- ✅ 完成 Issue #4: 创建项目配置数据模型 (Pydantic)
- ✅ 完成 Issue #5-11: 实现 Jinja2 模板引擎和所有项目模板
- ✅ 完成 Issue #12-13: 实现 forge create 命令 (交互/非交互模式)
- ✅ 完成 Issue #14-16: 添加代码质量和 CI/CD 模板
- ✅ 完成 Issue #17: 编写 CLI 和 Generator 单元测试 (31 tests)
- ✅ 完成 Issue #18: 完善项目文档 (README, CONTRIBUTING, CHANGELOG)
