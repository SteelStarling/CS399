# Hello Docker
FROM python:3.11
MAINTAINER Taylor Hancock <thancock0319@gmail.com>

# Code from Prof. Paulus's example
# Ensures .pyc files are not written and that the output goes to the log file
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

# Create working directory
WORKDIR "CS399/HW5_Docker/src"

# Copy main into directory
COPY main.py ./

# Run main
CMD [ "python", "main.py" ]