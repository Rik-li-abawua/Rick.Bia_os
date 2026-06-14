from fastapi import APIRouter

router = APIRouter(prefix='/passengers', tags=['passengers'])

@router.get('/')
def list_passengers():
    return []
