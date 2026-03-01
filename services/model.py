from .DB import engine, Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Organization(Base):
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True, index=True)
    organization_name = Column(String, nullable=False, unique=True, index=True)
    organization_password = Column(String, nullable=False)
    organization_email = Column(String, nullable=False)
    organization_phone = Column(String, nullable=False)
    super_admin_name = Column(String, nullable=False)
    super_admin = Column(Boolean, default=True)
    super_admin_password = Column(String, nullable=False)
    super_admin_email = Column(String, nullable=False)
    admin = relationship("Admin", back_populates="organization")
    staff = relationship("Staff", back_populates="organization")  
    booking_service = relationship("Booking_Service", back_populates="organization")
    service = relationship("Service", back_populates="organization")

class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    admin_name = Column(String, nullable=False)
    admin_password = Column(String, nullable=False)
    admin_email = Column(String, nullable=False)
    admin_phone = Column(String, nullable=False)
    is_admin = Column(Boolean, default=True)
    #foreign key
    organization_id = Column(Integer, ForeignKey("organization.id"))
    organization = relationship("Organization", back_populates="admin")
    

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    staff_name = Column(String, nullable=False)
    staff_password = Column(String, nullable=False)
    staff_email = Column(String, nullable=False)
    staff_phone = Column(String, nullable=False)
    staff_salary = Column(Integer, nullable=False)
    access_leads = Column(Boolean, default=False)
    access_bookings = Column(Boolean, default=False)
    access_services = Column(Boolean, default=False)
    access_inventory = Column(Boolean, default=False)
    access_reports = Column(Boolean, default=False)
    department = Column(String, nullable=False)
    is_staff = Column(Boolean, default=True)
    #foreign key
    organization_id = Column(Integer, ForeignKey("organization.id"))
    organization = relationship("Organization", back_populates="staff")


class service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    service_price = Column(Integer, nullable=False)
    service_description = Column(String)
    #foreign key
    organization_id = Column(Integer, ForeignKey("organization.id"))
    organization = relationship("Organization", back_populates="service")
    booking_service = relationship("Booking_Service", back_populates="service")

class Booking_Service(Base):   
    __tablename__ = "booking_service"

    id = Column(Integer, primary_key=True, index=True)
    booking_service_customer_name = Column(String, nullable=False)
    booking_service_customer_email = Column(String, nullable=False)
    booking_service_customer_phone = Column(String, nullable=False)
    booking_service_customer_address = Column(String, nullable=False)
    booking_service_customer_message = Column(String)
    booking_service_name = Column(String, nullable=False)
    booking_service_price = Column(Integer, nullable=False)
    booking_service_status = Column(Boolean, default=False)
    booking_service_date = Column(DateTime, default=datetime.now)
    #foreign key
    organization_id = Column(Integer, ForeignKey("organization.id"))
    service_id = Column(Integer, ForeignKey("service.id"))
    organization = relationship("Organization", back_populates="booking_service")
    service = relationship("Service", back_populates="booking_service")
 
class product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    product_price = Column(Integer, nullable=False)
    product_description = Column(String)
    product_quantity = Column(Integer, nullable=False)
    #foreign key
    organization_id = Column(Integer, ForeignKey("organization.id"))
    organization = relationship("Organization", back_populates="product")
    booking_product = relationship("Booking_Product", back_populates="product")


class Booking_Product(Base):   
    __tablename__ = "booking_product"

    id = Column(Integer, primary_key=True, index=True)
    booking_product_customer_name = Column(String, nullable=False)
    booking_product_customer_email = Column(String, nullable=False)
    booking_product_customer_phone = Column(String, nullable=False)
    booking_product_customer_address = Column(String, nullable=False)
    booking_product_customer_message = Column(String)
    booking_product_name = Column(String, nullable=False)
    booking_product_price = Column(Integer, nullable=False)
    booking_product_quantity = Column(Integer, nullable=False)
    booking_product_status = Column(Boolean, default=False)
    booking_product_date = Column(DateTime, default=datetime.now)
    #foreign key
    organization_id = Column(Integer, ForeignKey("organization.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    organization = relationship("Organization", back_populates="booking_product")
    product = relationship("Product", back_populates="booking_product")