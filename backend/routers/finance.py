from fastapi import APIRouter

router = APIRouter(prefix='/finance', tags=['finance'])

@router.get('/summary')
def summary():
    return {'portfolio':'pending','mortgage':'pending'}
