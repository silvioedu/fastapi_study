from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
  """
  Configurações gerais usadas na aplicação
  """
  API_V1_STR: str = '/api/v1'
  DB_URL: str = 'postgresql+asyncpg://geek:university@localhost:5432/faculdade'
  DBBaseModel = declarative_base()
  
  JWT_SECRET: str = 'WfBEp2X2KhIslE2XcPUSBcc9HmV2avSXX5rvfm7ZspQ'
  """
  import secrets
  token: str = secrets.token_urlsafe(42)
  """
  ALGORITHM: str = 'HS256'

  ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7
  
  class Config:
    case_sensitive = True


settings: Settings = Settings()