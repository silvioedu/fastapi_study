from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Cursos API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
  import uvicorn
  uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2NjQwMjU4MTAsImlhdCI6MTY2MzQyMTAxMCwic3ViIjoiMiJ9.r4NLbhFCCX_40DdwxfpjE4AHOVu3kkpYeDYJYNarTME
Type: bearer

Token Ray: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2NjQwNjM0MzksImlhdCI6MTY2MzQ1ODYzOSwic3ViIjoiMyJ9.pJHhQm4fvpEFSndVHnqN1QLIgbFwmTaeeduQJcYcVK8
"""