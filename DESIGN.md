# ForgeAPI 设计文档

> 🚀 **项目代号:** ForgeAPI  
> **版本:** v0.1.0 (MVP)  
> **最后更新:** 2026年2月28日  
> **作者:** Zachary

---

## 📋 目录

1. [项目概述](#1-项目概述)
2. [核心功能](#2-核心功能)
3. [技术栈](#3-技术栈)
4. [CLI 设计](#4-cli-设计)
5. [生成项目结构](#5-生成项目结构)
6. [模板系统设计](#6-模板系统设计)
7. [配置系统](#7-配置系统)
8. [AI 代理集成](#8-ai-代理集成)
9. [测试策略](#9-测试策略)
10. [发布与分发](#10-发布与分发)
11. [路线图](#11-路线图)

---

## 1. 项目概述

### 1.1 项目定位

ForgeAPI 是一款高度模块化、面向 AI 应用时代的 FastAPI 项目脚手架 CLI 工具。它旨在解决开发者在创建 FastAPI 项目时面临的"重复造轮子"问题，提供一键生成包含 **鉴权 + Docker + 数据库 + LLM 集成** 的完整项目结构。

### 1.2 核心价值主张

| 痛点                             | ForgeAPI 解决方案      |
| -------------------------------- | --------------------------- |
| 现有模板太简单或太复杂           | 模块化选择，按需生成        |
| 每次都要配置 Docker/Alembic/测试 | 开箱即用的最佳实践配置      |
| 手写样板代码耗时                 | AI 驱动的代码生成           |
| 架构不统一难维护                 | 强制执行 Clean Architecture |

### 1.3 目标用户

- 🎯 需要快速启动 FastAPI 项目的后端开发者
- 🎯 希望学习 FastAPI 最佳实践的初学者
- 🎯 需要统一团队项目结构的技术负责人
- 🎯 构建 AI/LLM 应用的开发者

---

## 2. 核心功能

### 2.1 阶段一：核心骨架 (MVP)

| 功能               | 描述                                        | 优先级 |
| ------------------ | ------------------------------------------- | ------ |
| 交互式项目创建     | 通过命令行交互选择项目配置                  | P0     |
| 包管理器选择       | 支持 uv（默认）/ Poetry 管理依赖            | P0     |
| Clean Architecture | 自动生成 API/Service/DAO 分层结构           | P0     |
| 数据库集成         | SQLAlchemy (Async) + Alembic 迁移           | P0     |
| Docker 支持        | 生成优化的 Dockerfile 和 docker-compose.yml | P0     |
| 认证模块           | JWT 认证开箱即用                            | P1     |
| 配置管理           | 多环境配置（dev/staging/prod）              | P0     |
| 测试框架           | Pytest + pytest-asyncio 配置                | P0     |
| 代码质量           | Ruff linter/formatter 配置                  | P1     |

### 2.2 阶段二：AI 赋能

| 功能           | 描述                                | 优先级 |
| -------------- | ----------------------------------- | ------ |
| AI Model 生成  | 自然语言描述生成 SQLAlchemy Model   | P1     |
| AI Schema 生成 | 根据 Model 自动生成 Pydantic Schema | P1     |
| AI API 生成    | 生成完整的 CRUD API 端点            | P2     |

### 2.3 阶段三：高级模板

| 功能            | 描述                | 优先级 |
| --------------- | ------------------- | ------ |
| Celery 任务队列 | 异步任务处理支持    | P2     |
| WebSocket 支持  | 实时通信模板        | P2     |
| 支付集成        | Stripe/微信支付模板 | P3     |
| RBAC 权限       | 复杂角色权限管理    | P3     |

---

## 3. 技术栈

### 3.1 CLI 工具技术栈

```
forgeapi/
├── Python >= 3.10
├── Typer              # CLI 框架
├── Rich               # 终端美化输出
├── Questionary        # 交互式命令行
├── Jinja2             # 模板引擎
├── PyYAML             # 配置文件解析
└── httpx              # HTTP 客户端（AI API 调用）
```

### 3.2 生成项目技术栈

```
generated-project/
├── Python >= 3.10
├── FastAPI            # Web 框架
├── Uvicorn            # ASGI 服务器
├── Pydantic V2        # 数据验证
├── SQLAlchemy 2.0     # ORM (Async)
├── Alembic            # 数据库迁移
├── Redis              # 缓存/Session
├── PostgreSQL         # 数据库
├── PyJWT              # JWT 认证
├── Pytest             # 测试框架
└── Ruff               # Linter/Formatter
```

---

## 4. CLI 设计

### 4.1 命令结构

```bash
# 安装
pip install forgeapi
# 或使用 uv
uv pip install forgeapi

# 主要命令
forge create <project-name>    # 创建新项目
forge add model <description>  # AI 生成 Model（阶段二）
forge add api <model-name>     # AI 生成 CRUD API（阶段二）
forge version                  # 显示版本信息
forge --help                   # 帮助信息
```

### 4.2 交互式创建流程

```
$ forge create my-awesome-api

🚀 ForgeAPI - 创建新项目

? 项目名称: my-awesome-api
? 项目描述: A awesome FastAPI project
? 作者名称: Your Name
? 作者邮箱: your@email.com
? Python 版本: (3.10 / 3.11 / 3.12) [3.11]

📦 包管理器配置
? 选择包管理器: (Use arrow keys)
 ❯ uv (推荐 - 更快)
   Poetry
   pip (仅 requirements.txt)

🗄️ 数据库配置
? 选择数据库: (Use arrow keys)
 ❯ PostgreSQL (推荐)
   MySQL
   SQLite (仅开发)
   None (无数据库)

? 是否启用数据库迁移 (Alembic)? (Y/n) Yes

🔐 认证配置
? 是否包含 JWT 认证模块? (Y/n) Yes

🐳 Docker 配置
? 是否生成 Docker 配置? (Y/n) Yes
? 是否生成 docker-compose.yml? (Y/n) Yes
? docker-compose 包含哪些服务? (多选)
  ✔ PostgreSQL
  ✔ Redis
  ◯ RabbitMQ
  ◯ MinIO (对象存储)

🧪 测试配置
? 是否配置 Pytest? (Y/n) Yes

✨ 额外选项
? 是否配置 Ruff (Linter/Formatter)? (Y/n) Yes
? 是否生成 GitHub Actions CI? (Y/n) Yes
? 是否生成 .vscode 配置? (Y/n) Yes

📁 正在生成项目结构...
✅ 项目 my-awesome-api 创建成功！

下一步:
  cd my-awesome-api
  uv sync                    # 安装依赖
  uv run alembic upgrade head # 运行数据库迁移
  uv run python -m app.main  # 启动服务

📚 文档: https://forgeapi.dev
```

### 4.3 命令行参数（非交互模式）

支持通过命令行参数跳过交互，便于 CI/CD 或脚本使用：

```bash
forge create my-api \
  --package-manager uv \
  --database postgres \
  --auth jwt \
  --docker \
  --no-interactive
```

---

## 5. 生成项目结构

### 5.1 完整目录结构

基于参考项目 `PROJECT_website/backend` 的最佳实践，生成以下结构：

```
my-awesome-api/
├── .github/                      # GitHub 配置
│   └── workflows/
│       └── ci.yml               # CI 工作流
├── .vscode/                      # VS Code 配置
│   ├── settings.json
│   └── launch.json
├── alembic/                      # 数据库迁移
│   ├── versions/                # 迁移版本文件
│   ├── env.py                   # Alembic 环境配置
│   ├── script.py.mako           # 迁移脚本模板
│   └── README.md
├── app/                          # 应用主目录
│   ├── __init__.py
│   ├── main.py                  # 应用入口 (uvicorn 启动)
│   ├── server.py                # FastAPI 应用配置
│   ├── api/                     # API 层 (路由)
│   │   ├── __init__.py
│   │   ├── auth_api.py          # 认证 API
│   │   └── health_api.py        # 健康检查 API
│   ├── config/                  # 配置模块
│   │   ├── __init__.py
│   │   ├── base.py              # 基础配置类
│   │   └── env.py               # 环境配置类
│   ├── core/                    # 核心模块
│   │   ├── __init__.py
│   │   ├── auth.py              # JWT 认证处理
│   │   ├── config.py            # 配置加载
│   │   ├── deps.py              # FastAPI 依赖注入
│   │   ├── database.py          # 数据库连接
│   │   └── redis.py             # Redis 连接
│   ├── daos/                    # 数据访问层 (DAO)
│   │   ├── __init__.py
│   │   └── user_dao.py          # 用户 DAO
│   ├── exceptions/              # 异常处理
│   │   ├── __init__.py
│   │   ├── exception.py         # 自定义异常
│   │   └── handler.py           # 全局异常处理器
│   ├── models/                  # SQLAlchemy 模型
│   │   ├── __init__.py
│   │   ├── base.py              # 基础模型类
│   │   └── user.py              # 用户模型
│   ├── schemas/                 # Pydantic Schema
│   │   ├── __init__.py
│   │   ├── api_schema.py        # 通用 API Schema
│   │   └── auth_schema.py       # 认证 Schema
│   ├── services/                # 业务逻辑层
│   │   ├── __init__.py
│   │   ├── auth_service.py      # 认证服务
│   │   └── user_service.py      # 用户服务
│   └── utils/                   # 工具模块
│       ├── __init__.py
│       ├── log.py               # 日志工具
│       └── profile.py           # 项目路径工具
├── scripts/                      # 脚本目录
│   ├── migrate_database.sh      # 数据库迁移脚本
│   └── start_up_service.sh      # 启动脚本
├── tests/                        # 测试目录
│   ├── __init__.py
│   ├── conftest.py              # Pytest 配置和 fixtures
│   ├── api/                     # API 测试
│   │   └── test_auth_api.py
│   ├── services/                # 服务层测试
│   │   └── test_auth_service.py
│   └── daos/                    # DAO 测试
│       └── test_user_dao.py
├── .dockerignore                 # Docker 忽略文件
├── .env.example                  # 环境变量示例
├── .gitignore                    # Git 忽略文件
├── .python-version               # Python 版本 (pyenv)
├── alembic.ini                   # Alembic 配置
├── config.yaml                   # 应用配置文件
├── docker-compose.yml            # Docker Compose 配置
├── Dockerfile                    # Docker 镜像配置
├── pyproject.toml                # 项目配置 (uv/Poetry)
├── pytest.ini                    # Pytest 配置
├── README.md                     # 项目文档
└── ruff.toml                     # Ruff 配置
```

### 5.2 分层架构说明

```
┌─────────────────────────────────────────────────────────────┐
│                        API Layer                            │
│  (app/api/) - 路由定义、请求/响应处理、参数验证               │
├─────────────────────────────────────────────────────────────┤
│                      Service Layer                          │
│  (app/services/) - 业务逻辑、事务处理、跨 DAO 协调           │
├─────────────────────────────────────────────────────────────┤
│                        DAO Layer                            │
│  (app/daos/) - 数据访问、SQL 查询、CRUD 操作                 │
├─────────────────────────────────────────────────────────────┤
│                       Model Layer                           │
│  (app/models/) - SQLAlchemy ORM 模型定义                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. 模板系统设计

### 6.1 模板目录结构

```
fastapi_forge/
├── templates/
│   ├── base/                    # 基础模板（必选）
│   │   ├── app/
│   │   │   ├── __init__.py.jinja
│   │   │   ├── main.py.jinja
│   │   │   ├── server.py.jinja
│   │   │   └── ...
│   │   ├── config.yaml.jinja
│   │   ├── pyproject.toml.jinja
│   │   └── README.md.jinja
│   ├── auth/                    # 认证模块模板
│   │   ├── api/
│   │   │   └── auth_api.py.jinja
│   │   ├── core/
│   │   │   └── auth.py.jinja
│   │   └── ...
│   ├── database/                # 数据库模板
│   │   ├── postgres/
│   │   ├── mysql/
│   │   └── sqlite/
│   ├── docker/                  # Docker 模板
│   │   ├── Dockerfile.jinja
│   │   ├── docker-compose.yml.jinja
│   │   └── .dockerignore.jinja
│   ├── ci/                      # CI/CD 模板
│   │   └── github-actions.yml.jinja
│   └── package_managers/        # 包管理器模板
│       ├── uv/
│       │   └── pyproject.toml.jinja
│       └── poetry/
│           └── pyproject.toml.jinja
```

### 6.2 模板变量

Jinja2 模板中使用的变量：

```python
class ProjectConfig:
    # 基础信息
    project_name: str              # 项目名称
    project_slug: str              # 项目标识符（snake_case）
    project_description: str       # 项目描述
    author_name: str               # 作者名称
    author_email: str              # 作者邮箱
    python_version: str            # Python 版本

    # 包管理器
    package_manager: Literal["uv", "poetry", "pip"]

    # 数据库
    database: Literal["postgres", "mysql", "sqlite", "none"]
    use_alembic: bool              # 是否使用数据库迁移

    # 功能模块
    use_auth: bool                 # JWT 认证
    use_redis: bool                # Redis
    use_docker: bool               # Docker 支持
    use_docker_compose: bool       # docker-compose
    docker_services: List[str]     # ["postgres", "redis", "rabbitmq"]

    # 测试和代码质量
    use_pytest: bool               # Pytest
    use_ruff: bool                 # Ruff
    use_github_actions: bool       # GitHub Actions
    use_vscode: bool               # VS Code 配置
```

### 6.3 模板示例

**pyproject.toml.jinja (uv 版本)**

```jinja
[project]
name = "{{ project_slug }}"
version = "0.1.0"
description = "{{ project_description }}"
authors = [
    { name = "{{ author_name }}", email = "{{ author_email }}" }
]
readme = "README.md"
requires-python = ">={{ python_version }}"

dependencies = [
    "fastapi[standard]>=0.115.0",
    "uvicorn>=0.34.0",
    "pyyaml>=6.0.2",
    "pydantic>=2.0.0",
    "pydantic-settings>=2.0.0",
{%- if database != "none" %}
    "sqlalchemy[asyncio]>=2.0.0",
{%- endif %}
{%- if database == "postgres" %}
    "asyncpg>=0.29.0",
    "psycopg[binary]>=3.2.0",
{%- elif database == "mysql" %}
    "aiomysql>=0.2.0",
{%- endif %}
{%- if use_alembic %}
    "alembic>=1.15.0",
{%- endif %}
{%- if use_redis %}
    "redis>=5.2.0",
{%- endif %}
{%- if use_auth %}
    "pyjwt>=2.10.0",
    "passlib[bcrypt]>=1.7.4",
    "bcrypt==4.0.1",
{%- endif %}
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.26.0",
    "ruff>=0.11.0",
{%- if use_redis %}
    "fakeredis>=2.27.0",
{%- endif %}
{%- if database == "postgres" %}
    "pytest-postgresql>=4.1.0",
{%- endif %}
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["app"]
```

**pyproject.toml.jinja (Poetry 版本)**

```jinja
[tool.poetry]
name = "{{ project_slug }}"
version = "0.1.0"
description = "{{ project_description }}"
authors = ["{{ author_name }} <{{ author_email }}>"]
readme = "README.md"
package-mode = false

[tool.poetry.dependencies]
python = "^{{ python_version }}"
fastapi = {extras = ["all"], version = "^0.115.0"}
uvicorn = "^0.34.0"
pyyaml = "^6.0.2"
pydantic = "^2.0.0"
pydantic-settings = "^2.0.0"
{%- if database != "none" %}
sqlalchemy = {extras = ["asyncio"], version = "^2.0.0"}
{%- endif %}
{%- if database == "postgres" %}
asyncpg = "^0.29.0"
psycopg = {extras = ["binary"], version = "^3.2.0"}
{%- elif database == "mysql" %}
aiomysql = "^0.2.0"
{%- endif %}
{%- if use_alembic %}
alembic = "^1.15.0"
{%- endif %}
{%- if use_redis %}
redis = "^5.2.0"
{%- endif %}
{%- if use_auth %}
pyjwt = "^2.10.0"
passlib = {extras = ["bcrypt"], version = "^1.7.4"}
bcrypt = "4.0.1"
{%- endif %}

[tool.poetry.group.dev.dependencies]
pytest = "^8.3.0"
pytest-asyncio = "^0.26.0"
ruff = "^0.11.0"
{%- if use_redis %}
fakeredis = "^2.27.0"
{%- endif %}
{%- if database == "postgres" %}
pytest-postgresql = "^4.1.0"
{%- endif %}

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

## 7. 配置系统

### 7.1 生成项目的配置结构

**config.yaml**

```yaml
env: dev

# 开发环境
dev:
  app:
    name: {{ project_name }} (dev)
    description: {{ project_description }}
    api: /api
    host: 0.0.0.0
    port: 8000
    uvicorn: app.server:app
    version: 0.1.0
    reload: true

  db:
    host: localhost
    port: 5432
    user: postgres
    password: postgres
    database: {{ project_slug }}
    driver_name: postgresql+asyncpg
    echo: true
    pool_size: 5
    max_overflow: 10
    pool_recycle: 3600
    pool_timeout: 30

  redis:
    host: localhost
    port: 6379
    db: 0

  jwt:
    secret_key: your-secret-key-change-in-production
    algorithm: HS256
    expire_minutes: 1440

# 生产环境
prod:
  app:
    name: {{ project_name }}
    reload: false

  db:
    echo: false
    pool_size: 20

  # 生产环境建议使用环境变量
```

### 7.2 配置类设计

**app/config/base.py**

```python
from pydantic_settings import BaseSettings
from app.config.env import AppConfig, RedisConfig, JwtConfig, DataBaseConfig


class BaseConfig(BaseSettings):
    """基础配置 - 所有环境通用"""
    env: str
    app: AppConfig
    db: DataBaseConfig
    redis: RedisConfig
    jwt: JwtConfig


class DevConfig(BaseConfig):
    """开发环境配置"""
    pass


class StagingConfig(BaseConfig):
    """预演环境配置"""
    pass


class ProdConfig(BaseConfig):
    """生产环境配置"""
    pass
```

---

## 8. AI 代理集成

### 8.1 设计目标

通过自然语言描述，自动生成：

- SQLAlchemy Model
- Pydantic Schema
- DAO 层代码
- Service 层代码
- API 路由

### 8.2 命令设计

```bash
# 生成 Model
forge add model "Product with name, price (decimal), description, and category_id foreign key to Category"

# 生成完整 CRUD API
forge add api Product --crud

# 使用自然语言描述生成 API
forge add api "用户可以创建订单，订单包含多个商品"
```

### 8.3 AI Prompt 模板

````python
MODEL_GENERATION_PROMPT = """
你是一个 FastAPI 专家，请根据以下描述生成 SQLAlchemy Model 代码。

要求:
1. 使用 SQLAlchemy 2.0 风格 (Mapped, mapped_column)
2. 使用 uuid7 作为主键
3. 包含完整的类型注解
4. 包含字段注释 (comment)

描述: {description}

请生成以下格式的代码:

```python
# models/{model_name}.py
import uuid
from uuid_extensions import uuid7
from sqlalchemy import String, Integer, DateTime, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class {ModelName}(Base):
    __tablename__ = "{table_name}"

    # ... fields
````

"""

````

### 8.4 LLM 配置

支持多种 LLM 提供商：

```yaml
# ~/.forgeapi/config.yaml
ai:
  provider: openai  # openai, anthropic, ollama
  model: gpt-4
  api_key: ${OPENAI_API_KEY}
  base_url: https://api.openai.com/v1  # 可自定义

  # 或使用本地模型
  # provider: ollama
  # model: codellama
  # base_url: http://localhost:11434
````

---

## 9. 测试策略

### 9.1 CLI 工具测试

```
tests/
├── test_cli.py              # CLI 命令测试
├── test_generator.py        # 项目生成器测试
├── test_templates.py        # 模板渲染测试
└── fixtures/                # 测试数据
    └── expected_outputs/
```

### 9.2 生成项目测试

生成的项目包含完整的测试配置：

```python
# tests/conftest.py
import pytest
import fakeredis.aioredis
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

@pytest.fixture
async def fake_redis_client():
    """创建 fakeredis 实例"""
    fake_redis = fakeredis.aioredis.FakeRedis(decode_responses=True)
    yield fake_redis
    await fake_redis.flushall()
    await fake_redis.aclose()

@pytest.fixture
async def fake_db_session(fake_async_engine):
    """创建测试数据库会话"""
    async_session = async_sessionmaker(
        fake_async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session
```

---

## 10. 发布与分发

### 10.1 PyPI 发布

```bash
# 发布到 PyPI
uv build
uv publish

# 或使用 Poetry
poetry build
poetry publish
```

### 10.2 安装方式

```bash
# 推荐: 使用 pipx 全局安装
pipx install forgeapi

# 或使用 uv
uv tool install forgeapi

# 或使用 pip
pip install forgeapi
```

### 10.3 版本管理

遵循语义化版本 (SemVer):

- `0.1.x`: MVP 阶段，核心功能开发
- `0.2.x`: AI 功能集成
- `1.0.0`: 稳定版本发布

---

## 11. 路线图

### 11.1 阶段一：核心骨架 (2026 Q1)

- [x] 项目初始化
- [ ] CLI 框架搭建 (Typer + Rich)
- [ ] 交互式问答实现 (Questionary)
- [ ] 基础模板系统
- [ ] uv/Poetry 支持
- [ ] SQLAlchemy + Alembic 模板
- [ ] Docker 配置模板
- [ ] JWT 认证模板
- [ ] Pytest 测试模板
- [ ] 发布到 PyPI

### 11.2 阶段二：AI 赋能 (2026 Q2)

- [ ] LLM API 集成
- [ ] `forge add model` 命令
- [ ] `forge add api` 命令
- [ ] 支持多种 LLM 提供商
- [ ] 本地模型支持 (Ollama)

### 11.3 阶段三：高级功能 (2026 Q3-Q4)

- [ ] Celery 任务队列模板
- [ ] WebSocket 模板
- [ ] RBAC 权限模板
- [ ] 支付集成模板
- [ ] Pro 模板商业化

---

## 附录

### A. 参考项目

- [PROJECT_website/backend](../PROJECT_website/backend) - 项目结构参考
- [tiangolo/full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template)
- [fastapi/cookiecutter-fastapi](https://github.com/fastapi/cookiecutter-fastapi)

### B. 相关链接

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 文档](https://docs.sqlalchemy.org/)
- [Typer 文档](https://typer.tiangolo.com/)
- [uv 文档](https://docs.astral.sh/uv/)

### C. 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request
