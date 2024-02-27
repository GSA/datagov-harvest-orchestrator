# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the local code to the container
COPY . .

# Install Poetry
RUN pip install poetry

# Install project dependencies using Poetry
# --no-root: Don't install the root package (your project), only dependencies
# --no-dev: Avoid installing development dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
