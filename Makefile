#####################################
### RUFF
#####################################
fmt:
	uv run ruff format .

# lint code
lint:
	uv run ruff check --fix .

#####################################
### DJANGO
#####################################
migrations:
	uv run piccolo migrations new all --auto

migrate:
	uv run piccolo migrations forwards all

createuser:
	uv run piccolo user create

run-infra:
	docker compose -f docker-compose.local.yaml up -d

stop-infra:
	docker compose -f docker-compose.local.yaml down

run-server:
	uv run python main.py

#####################################
### TESTING
#####################################
test:
	uv run piccolo tester run