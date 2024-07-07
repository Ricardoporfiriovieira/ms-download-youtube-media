run:
	uvicorn app.main:app --reload

build:
	docker build -t youtube-downloader .

run-docker:
	docker run -p 8000:8000 youtube-downloader