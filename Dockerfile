FROM python:3.6
COPY auction auction
CMD ["python", "-m", "auction"]