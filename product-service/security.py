from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.security.utils import get_authorization_scheme_param

ADMIN_TOKEN = "ABC123ADMIN"
CLIENT_TOKEN = "XYZ789CLIENT"

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


def get_role_from_token(authorization: str | None = Depends(api_key_header)):
    if not authorization:
        return "CLIENT"  # sin token = solo lectura

    scheme, token = get_authorization_scheme_param(authorization)

    if token == ADMIN_TOKEN:
        return "ADMIN"
    if token == CLIENT_TOKEN:
        return "CLIENT"

    raise HTTPException(status_code=401, detail="Token inválido")


def require_admin(role: str):
    if role != "ADMIN":
        raise HTTPException(
            status_code=403,
            detail="No tienes permisos de administrador."
        )
