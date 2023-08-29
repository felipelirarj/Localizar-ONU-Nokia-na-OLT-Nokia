start:
	docker-compose up -d --build
stop:
	docker-compose down
restart:
	docker-compose restart
pylint:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && pylint src/app
