from sqlalchemy.orm import Session

from rossmann_oltp.models import Country, City, Shop, Employee


def create_country(db: Session, name: str) -> Country:
    country = Country(country_name=name)
    db.add(country)
    db.commit()
    db.refresh(country)
    return country

def create_city(db: Session, country: Country, name: str) -> City:
    city = City(city_name=name, country=country)
    db.add(city)
    db.commit()
    db.refresh(city)
    return city

def create_shop(db: Session, 
                city: City, 
                address: str, 
                employees: list[Employee] = None) -> Shop:
    shop = Shop(city=city, address=address)    
    if employees:
        for employee in employees:
            db.add(employee)

    db.add(shop)
    db.commit()
    db.refresh(shop)
    return shop