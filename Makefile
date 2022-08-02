black:
	pre-commit run black

test-mock-only:
	pytest -s --client mock

test-twilio-only:
	pytest -s --client twilio

test-coverage-report:
	pytest --cov=twilio_conversations_mock --client mock tests/
