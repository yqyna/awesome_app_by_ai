# Awesome App by AI

一个完整的前后端模板：
- 前端：Vue 3 + Vite
- 后端：FastAPI（采用 Django 风格分层与目录组织）

## 项目结构

```text
backend/
  manage.py                # 类 Django 启动入口
  app/
    config/                # settings / urls
    core/                  # 通用异常处理等
    apps/                  # 按业务拆分（health, tasks）
      <module>/
        views.py           # 路由层
        services.py        # 业务层
        repositories.py    # 数据访问层（可选）
        schemas.py         # Pydantic 模型
frontend/
  src/
    views/
    router/
    services/
```

## 启动后端

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e .
./manage.py
```

## 启动前端

```bash
cd frontend
npm install
npm run dev
```

前端默认代理 `/api` 到 `http://localhost:8000`。
