from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from rossmann_oltp_models import Terminal

from rossmann_oltp.db import get_db

router = APIRouter(prefix="/terminals", tags=["terminals"])


@router.get('/get_available', response_model=list[int])
async def get_id_available_terminals(shop_id: int, 
                                     db: Session = Depends(get_db)):
    terminals = db.query(Terminal) \
                  .filter(Terminal.shop_id == shop_id) \
                  .all()
    if not terminals:
        raise HTTPException(status_code=404, detail="No terminals found for this shop")
    
    available_terminals = [terminal.terminal_id for terminal in terminals]
    return available_terminals

@router.get('/authorize', response_model=bool)
async def authorize_terminal(terminal_id: int, 
                             shop_id: int,
                             password: str, 
                             db: Session = Depends(get_db)):
    terminal = db.query(Terminal) \
                 .filter(Terminal.terminal_id == terminal_id) \
                 .first()
        
    if not terminal:
        raise HTTPException(status_code=404, detail="Terminal not found")
    if terminal.shop_id != shop_id:
        raise HTTPException(status_code=403, detail="Invalid shop ID, terminal not authorized for this shop")
    if terminal.password != password:
        raise HTTPException(status_code=401, detail="Invalid password")
    
    return True
