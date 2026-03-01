from pydantic import BaseModel
from typing import Optional

class Organizationlogin(BaseModel):
    organization_name: str
    organization_password: str


class Organizationregister(BaseModel):
    organization_name: str
    organization_password: str
    organization_email: str
    organization_phone: str
    super_admin_name: str
    super_admin_password: str
    super_admin_email: str
    super_admin_phone: str


class Adminlogin(BaseModel):
    organization_name: str
    admin_email: str
    admin_password: str


class Adminregister(BaseModel):
    organization_id: int
    organization_name: str
    admin_email: str
    admin_password: str
    admin_phone: str
    admin_name: str