


```
# 1. Use a base image
FROM python:3.10-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy files from host into container
COPY . .

# 4. Install dependencies
RUN pip install -r requirements.txt

# 5. Expose a port (optional, for web apps)
EXPOSE 5000

# 6. Define default command
CMD ["python", "app.py"]

```
