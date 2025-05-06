from sqlalchemy.orm import Session

from rossmann_oltp.models import Shop, Employee, ShopEmployee


def create_shop(db: Session,
                country: str,
                city: str,
                address: str,
                employees: list[Employee] = None) -> Shop:
    shop = Shop(
        country=country,
        city=city,
        address=address,
    )
    if employees:
        for employee in employees:
            shop_employee = ShopEmployee(
                shop=shop,
                employee=employee
            )
            db.add(shop_employee)

    db.add(shop)
    db.commit()
    db.refresh(shop)
    return shop