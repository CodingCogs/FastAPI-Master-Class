FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    UV_COMPILE_BYTECODE=1




WORKDIR /app

COPY . .

RUN uv sync --locked


EXPOSE 8000

CMD ["uv","run","fastapi", "run"]