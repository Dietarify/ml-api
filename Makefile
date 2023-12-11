start:
	@uvicorn --app-dir src main:app

dev:
	@uvicorn --app-dir src main:app --reload