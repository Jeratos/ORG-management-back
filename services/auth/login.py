from fastapi import APIRouter, Depends, status, HTTPException
from ..schema import Organizationlogin,Organizationregister
from ..model import Organization
from ..DB import get_db
from sqlalchemy.orm import Session
from ..utils.jwt import create_access_token

router = APIRouter(
    prefix="/organization",
    tags=["Login"]
)

@router.post("/login", status_code=status.HTTP_200_OK)
def ORG_login(data: Organizationlogin, db: Session = Depends(get_db)):
    try:
        user= db.query(Organization).filter(Organization.organization_name == data.organization_name).first()
        if not user:
            return {
                "message": "User not found"
            }
        if not user.organization_password == data.organization_password:
            return {
                "message": "Incorrect password"
            }
        token = create_access_token(user)
        print(token)
        return {
            "message": "Login successful",
            "token": token
        }   
    except Exception as e:
        # return {
        #     "status_code": status.HTTP_400_BAD_REQUEST,
        #     "message": str(e)
        # }
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/register", status_code=status.HTTP_201_CREATED)
def ORG_register(data: Organizationregister, db: Session = Depends(get_db)):
    try:
        user= db.query(Organization).filter(Organization.organization_name == data.organization_name).first()
        if user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
        new_user = Organization(
            organization_name=data.organization_name,
            organization_password=data.organization_password,
            organization_email=data.organization_email,
            organization_phone=data.organization_phone,
            super_admin_name=data.super_admin_name,
            super_admin=data.super_admin,
            super_admin_password=data.super_admin_password,
            super_admin_email=data.super_admin_email
        )
        db.add(new_user)
        db.commit()
        token = create_access_token(user)
        return {
            "message": "User created successfully",
            "token": token
        }   
    except Exception as e:
        return {
            "message": str(e)
        }        