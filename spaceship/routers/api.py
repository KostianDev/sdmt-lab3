from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get("/matrix-mult")
def matrix_mult():
    a = np.random.randint(0, 10, (10, 10))
    b = np.random.randint(0, 10, (10, 10))
    return {
        "matrix_a": a.tolist(),
        "matrix_b": b.tolist(),
        "product":  (a @ b).tolist(),
    }