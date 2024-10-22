# Template for project with fastapi + dependency-injector
Simple project template for quick repository initialization.

## Venv
Create virtual environment
```shell
uv venv  # expected installed uv
```

Sync dependencies
```shell
uv sync
```

## Secrets
Docker compose will load secrets from `secrets/.env.prod`. To create it you can run
```shell
cp secrets/.env.example secrets/.env.prod
```

As an example empty `SECRET` var was added. You can generate random string using `openssl`
```ssh
openssl rand -hex 32
```
After that manually copy and paste resutl into `secrets/.env.prod`.