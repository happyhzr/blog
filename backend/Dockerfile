FROM astral/uv:python3.12-bookworm-slim

ENV UV_DEFAULT_INDEX=https://mirrors.aliyun.com/pypi/simple/

WORKDIR /app

# Copy dependency files first for Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy source code
COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]