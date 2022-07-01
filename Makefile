.PHONY: dev run lint test build

dev:
	huey_consumer.py florican.main.huey -k process -w 2

run:
	huey_consumer.py florican.main.huey -k process -w 2

lint:
	black --check .

unit:
	FLORICAN_CONFIG=/dev/null pytest --cov=florican --cov-report=xml --cov-fail-under=100

functional:
	bash ./tests/functional/test.sh

build:
	python -m build

image:
	docker build --tag florican:latest .
