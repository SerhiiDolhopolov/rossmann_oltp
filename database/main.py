from db import init_db, get_db
from services.location_service import create_country, create_city, create_shop, create_terminal
from services.employee_service import create_employee
from services.product_service import create_product, create_category
from services.product_service import add_product_to_city, add_product_to_shop
from rossmann_sync_schemas.employee_role import EmployeeRole
from rossmann_oltp_models import Category, Shop, City


def main():
    init_db()
    db = next(get_db())
    try:
        if db.query(Shop).count() > 0:
            return
        create_start_data()
    finally:
        db.close()


def create_start_data():
    db = next(get_db())
    try:
        country_a_b = create_country(db, "Germany")
        country_c = create_country(db, "Spain")
        city_a = create_city(db, country_a_b, "Berlin")
        city_b = create_city(db, country_a_b, "Nurnberg")
        city_c = create_city(db, country_c, "La Nucia")

        create_employee(
            db=db,
            first_name="Ramsay",
            last_name="Bolton",
            role=EmployeeRole.COURIER,
            salary=800,
        )
        shop_a = create_shop_a(db, city_a)
        shop_b = create_shop_b(db, city_b)
        shop_c = create_shop_c(db, city_c)
        categories = create_categories(db)
        shops = [shop_a, shop_b, shop_c]
        for shop in shops:
            for i in range(1, 4):
                create_terminal(
                    db=db,
                    shop=shop,
                )
        cities = [city_a, city_b, city_c]
        create_products(db, categories, cities, shops)
    finally:
        db.close()


def create_shop_a(db, city: City) -> Shop:
    employees = [
        create_employee(
            db=db,
            first_name="Stannis",
            last_name="Baratheon",
            role=EmployeeRole.ADMIN,
            salary=2000,
        ),
        create_employee(
            db=db,
            first_name="Renly",
            last_name="Baratheon",
            role=EmployeeRole.CASHIER,
            salary=500,
        ),
        create_employee(
            db=db,
            first_name="Davos",
            last_name="Seaworth",
            role=EmployeeRole.CASHIER,
            salary=500,
        ),
        create_employee(
            db=db,
            first_name="Robert",
            last_name="Baratheon",
            role=EmployeeRole.CASHIER,
            salary=550,
        ),
    ]
    return create_shop(
        db=db,
        city=city,
        address="Am Ostbahnhof 9/1.03 Ostbahnhof 10243 Berlin Friedrichshain",
        employees=employees,
    )


def create_shop_b(db, city: City) -> Shop:
    employees = [
        create_employee(
            db=db,
            first_name="Eddard",
            last_name="Stark",
            role=EmployeeRole.ADMIN,
            salary=1800,
        ),
        create_employee(
            db=db,
            first_name="Robb",
            last_name="Stark",
            role=EmployeeRole.CASHIER,
            salary=480,
        ),
        create_employee(
            db=db,
            first_name="Jon",
            last_name="Snow",
            role=EmployeeRole.CASHIER,
            salary=520,
        ),
        create_employee(
            db=db,
            first_name="Catelyn",
            last_name="Stark",
            role=EmployeeRole.CASHIER,
            salary=420,
        ),
    ]
    return create_shop(
        db=db,
        city=city,
        address="Rothenburger Str. 143 90439 Nürnberg St. Leonhard",
        employees=employees,
    )


def create_shop_c(db, city: City) -> Shop:
    employees = [
        create_employee(
            db=db,
            first_name="Tywin",
            last_name="Lannister",
            role=EmployeeRole.ADMIN,
            salary=1400,
        ),
        create_employee(
            db=db,
            first_name="Tyrion",
            last_name="Lannister",
            role=EmployeeRole.CASHIER,
            salary=350,
        ),
        create_employee(
            db=db,
            first_name="Jaime",
            last_name="Lannister",
            role=EmployeeRole.CASHIER,
            salary=360,
        ),
        create_employee(
            db=db,
            first_name="Cersei",
            last_name="Lannister",
            role=EmployeeRole.CASHIER,
            salary=310,
        ),
    ]
    return create_shop(
        db=db,
        city=city,
        address="Av. Sorolla, s/n, 03530 La Nucia, Alicante",
        employees=employees,
    )


def create_categories(db) -> dict[str, Category]:
    categories = {
        "Baby & Toys": create_category(
            db=db,
            name="Baby & Toys",
            description="Toys and products for babies and children",
        ),
        "Health": create_category(
            db=db,
            name="Health",
            description="Health and beauty products",
        ),
        "Household": create_category(
            db=db,
            name="Household",
            description="Household products",
        ),
        "Decor": create_category(
            db=db,
            name="Decor",
            description="Decorative products for home and office",
        ),
        "Care and fragrance": create_category(
            db=db,
            name="Care and fragrance",
            description="Personal care and fragrance products",
        ),
    }
    return categories


def create_products(db, categories: dict[str, Category], cities: list[City], shops: list[Shop]):
    create_products_baby(db, categories["Baby & Toys"], cities, shops)
    create_products_health(db, categories["Health"], cities, shops)
    create_products_household(db, categories["Household"], cities, shops)
    create_products_decor(db, categories["Decor"], cities, shops)
    create_products_care(db, categories["Care and fragrance"], cities, shops)


def create_products_baby(db, category: Category, cities: list[City], shops: list[Shop]):
    baby_products = {
        "Set of 6 balancing stones": (
            "A set of 6 balancing stones in different colors and shapes. Perfect for developing "
            "fine motor skills and creativity in children.",
            "product-images/Set_of_6_balancing_stones.webp",
            {
                "Berlin": (16.99, 0.1),
                "Nurnberg": (15.99, 0.05),
                "La Nucia": (14.99, 0.05),
            },
        ),
        "Water ball track": (
            "A water ball track that allows children to play with water and balls. It helps develop "
            "hand-eye coordination and fine motor skills.",
            "product-images/Water_ball_track.webp",
            {
                "Berlin": (9.99, 0),
                "Nurnberg": (9.49, 0),
                "La Nucia": (8.99, 0),
            },
        ),
        "Foldable toilet seat duck": (
            "A foldable toilet seat in the shape of a duck. It is easy to carry and use, making it "
            "perfect for potty training on the go.",
            "product-images/Foldable_toilet_seat_duck.webp",
            {
                "Berlin": (7.99, 0.2),
                "Nurnberg": (7.99, 0.2),
                "La Nucia": (7.49, 0.1),
            },
        ),
        "Diapers Extra Soft Premium Junior Size 5 (11-16 kg)": (
            "Extra soft diapers for children weighing 11-16 kg. They provide comfort and protection "
            "for your baby.",
            "product-images/Diapers.webp",
            {
                "Berlin": (12.99, 0.1),
                "Nurnberg": (11.99, 0.1),
                "La Nucia": (10.99, 0.05),
            },
        ),
    }
    add_products(db, baby_products, category, cities, shops)


def create_products_health(db, category: Category, cities: list[City], shops: list[Shop]):
    health_products = {
        "Super-Haftcreme Neutral": (
            "Super adhesive cream for dentures. Provides a strong hold and comfort for denture "
            "wearers.",
            "product-images/Super_haftcreme_neutral.webp",
            {
                "Berlin": (1.59, 0),
                "Nurnberg": (1.59, 0),
                "La Nucia": (1.59, 0.1),
            },
        ),
        "EZB 6100 Electric Toothbrush": (
            "An electric toothbrush with a 2-minute timer and 30-second interval timer. It helps you "
            "brush your teeth effectively.",
            "product-images/EZB_6100_electric_toothbrush.webp",
            {
                "Berlin": (89.99, 0.05),
                "Nurnberg": (84.99, 0.1),
                "La Nucia": (79.99, 0),
            },
        ),
        "Rapid Alcohol Test": (
            "A rapid alcohol test that provides quick results. It is easy to use and helps you check "
            "your blood alcohol level.",
            "product-images/Rapid_alcohol_test.webp",
            {
                "Berlin": (6.99, 0),
                "Nurnberg": (6.99, 0),
                "La Nucia": (6.49, 0),
            },
        ),
    }
    add_products(db, health_products, category, cities, shops)


def create_products_household(db, category: Category, cities: list[City], shops: list[Shop]):
    household_products = {
        "Universal detergent liquid fresh cotton blossom 20 WL": (
            "A universal detergent liquid with a fresh cotton blossom scent. It is suitable for all "
            "types of fabrics and provides a deep clean.",
            "product-images/Universal_detergent_liquid.webp",
            {
                "Berlin": (5.49, 0),
                "Nurnberg": (5.49, 0),
                "La Nucia": (4.99, 0.1),
            },
        ),
        "Fabric softener concentrate Aprilfrisch 59 WL": (
            "A fabric softener concentrate with an April fresh scent. It provides long-lasting "
            "freshness and softness to your laundry.",
            "product-images/Fabric_softener.webp",
            {
                "Berlin": (3.29, 0),
                "Nurnberg": (3.29, 0),
                "La Nucia": (2.99, 0),
            },
        ),
        "All-purpose cleaner spray bathroom": (
            "An all-purpose cleaner spray for the bathroom. It effectively removes dirt and limescale, "
            "leaving your bathroom clean and fresh.",
            "product-images/All_purpose_cleaner.webp",
            {
                "Berlin": (3.29, 0),
                "Nurnberg": (3.29, 0),
                "La Nucia": (2.99, 0.05),
            },
        ),
    }
    add_products(db, household_products, category, cities, shops)


def create_products_decor(db, category: Category, cities: list[City], shops: list[Shop]):
    decor_products = {
        "PopGrip Premium Glitter Rainbow Void": (
            "A PopGrip with a premium glitter design. It provides a secure grip for your phone and can "
            "be used as a stand.",
            "product-images/PopGrip_premium_glitter.webp",
            {
                "Berlin": (17.99, 0),
                "Nurnberg": (16.99, 0),
                "La Nucia": (16.99, 0),
            },
        ),
        "LED starry sky light green": (
            "A LED light that creates a starry sky effect. It is perfect for creating a relaxing "
            "atmosphere in your home.",
            "product-images/LED_starry.webp",
            {
                "Berlin": (7.99, 0),
                "Nurnberg": (7.99, 0),
                "La Nucia": (7.99, 0.1),
            },
        ),
    }
    add_products(db, decor_products, category, cities, shops)


def create_products_care(db, category: Category, cities: list[City], shops: list[Shop]):
    care_products = {
        "Beauty Scrub Blueberry Caramel Bliss": (
            "A beauty scrub with a blueberry caramel scent. It exfoliates and nourishes your skin",
            "product-images/Beauty_scrub.webp",
            {
                "Berlin": (7.99, 0.35),
                "Nurnberg": (7.49, 0.35),
                "La Nucia": (6.99, 0.3),
            },
        ),
        "Anti-Gray Effect Coloring Conditioner": (
            "A coloring conditioner that helps reduce gray hair. It provides a natural color and shine "
            "to your hair.",
            "product-images/Anti_gray.webp",
            {
                "Berlin": (15.99, 0.2),
                "Nurnberg": (13.99, 0.2),
                "La Nucia": (12.99, 0.25),
            },
        ),
    }
    add_products(db, care_products, category, cities, shops)


def add_products(
    db,
    map_products: dict[str, tuple[str, str, dict[str, tuple[float, float]]]],
    category: Category,
    cities: list[City],
    shops: list[Shop],
):
    for name, (description, image_url, map_price) in map_products.items():
        product = create_product(
            db=db,
            name=name,
            description=description,
            category=category,
            image_url=image_url,
        )
        for city in cities:
            add_product_to_city(
                db, product, city, map_price[city.city_name][0], map_price[city.city_name][1]
            )
        for shop in shops:
            add_product_to_shop(db, product, shop)


if __name__ == "__main__":
    main()
