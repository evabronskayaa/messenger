Generic single-database configuration.

docs: https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment

Create migration:

```shell
alembic revision -m ""
```

Autogenerate migration:
```shell
alembic revision --autogenerate -m "Initial state"
```

```shell
alembic upgrade head
```

can't locate revision identified by ..., alembic:
https://stackoverflow.com/questions/32311366/alembic-util-command-error-cant-find-identifier