import random

from db import init_db, get_db
from services.location_service import create_country, create_city, create_shop
from services.employee_service import create_employee
from services.product_service import create_product, create_category
from services.product_service import add_product_to_city, add_product_to_shop
from employee_role import EmployeeRole
from rossmann_oltp.models import Category, Shop, City


def main():
    init_db()
    create_start_data()

def create_start_data():
    db = next(get_db())
    try:
        if db.query(Shop).count() > 0:
            return
        
        country_a_b = create_country(db, 'Germany')
        country_c = create_country(db, 'Spain')
        city_a = create_city(db, country_a_b, 'Berlin')
        city_b = create_city(db, country_a_b, 'Nurnberg')
        city_c = create_city(db, country_c, 'La Nucia')
        
        shop_a = create_shop_a(db, city_a)
        shop_b = create_shop_b(db, city_b)
        shop_c = create_shop_c(db, city_c)
        categories = create_categories(db)
        create_products(db, categories, [shop_a, shop_b, shop_c])
    finally:
        db.close()
    
def create_shop_a(db, city: City) -> Shop:
    employees = [
        create_employee(
            db=db,
            first_name='Stannis',
            last_name='Baratheon',
            role=EmployeeRole.ADMIN,
            salary=2000        
            ),
        create_employee(
            db=db,
            first_name='Renly',
            last_name='Baratheon',
            role=EmployeeRole.CASHIER,
            salary=500        
            ),
        create_employee(
            db=db,
            first_name='Davos',
            last_name='Seaworth',
            role=EmployeeRole.CASHIER,
            salary=500        
            ),
        create_employee(
            db=db,
            first_name='Robert',
            last_name='Baratheon',
            role=EmployeeRole.CASHIER,
            salary=550        
            ),
    ]
    return create_shop(
        db=db,
        city=city,
        address='Am Ostbahnhof 9/1.03 Ostbahnhof 10243 Berlin Friedrichshain',
        employees=employees
    )
def create_shop_b(db, city: City) -> Shop:
    employees = [
        create_employee(
            db=db,
            first_name='Eddard',
            last_name='Stark',
            role=EmployeeRole.ADMIN,
            salary=1800        
            ),
        create_employee(
            db=db,
            first_name='Robb',
            last_name='Stark',
            role=EmployeeRole.CASHIER,
            salary=480       
            ),
        create_employee(
            db=db,
            first_name='Jon',
            last_name='Snow',
            role=EmployeeRole.CASHIER,
            salary=520        
            ),
        create_employee(
            db=db,
            first_name='Catelyn',
            last_name='Stark',
            role=EmployeeRole.CASHIER,
            salary=420        
            ),
    ]
    return create_shop(
        db=db,
        city=city,
        address='Rothenburger Str. 143 90439 Nürnberg St. Leonhard',
        employees=employees
    )   
def create_shop_c(db, city: City) -> Shop:
    employees = [
        create_employee(
            db=db,
            first_name='Tywin',
            last_name='Lannister',
            role=EmployeeRole.ADMIN,
            salary=1400        
            ),
        create_employee(
            db=db,
            first_name='Tyrion',
            last_name='Lannister',
            role=EmployeeRole.CASHIER,
            salary=350       
            ),
        create_employee(
            db=db,
            first_name='Jaime',
            last_name='Lannister',
            role=EmployeeRole.CASHIER,
            salary=360        
            ),
        create_employee(
            db=db,
            first_name='Cersei',
            last_name='Lannister',
            role=EmployeeRole.CASHIER,
            salary=310        
            ),
    ]
    return create_shop(
        db=db,
        city=city,
        address='Av. Sorolla, s/n, 03530 La Nucia, Alicante',
        employees=employees
    )

def create_categories(db) -> dict[str, Category]:
    categories = {
        'Baby & Toys': create_category(
                        db=db,
                        name='Baby & Toys',
                        description='Toys and products for babies and children'
                    ),
        'Health': create_category(
                        db=db,
                        name='Health',
                        description='Health and beauty products'
                    ),
        'Household': create_category(
                        db=db,
                        name='Household',
                        description='Household products'
                    ),
        'Decor': create_category(
                        db=db,
                        name='Decor',
                        description='Decorative products for home and office'
                    ),
        'Care and fragrance': create_category(
                        db=db,
                        name='Care and fragrance',
                        description='Personal care and fragrance products'
                    ),
    }
    return categories

def create_products(db, city: City, categories: dict[str, Category], shops: list[Shop]):
    create_products_baby(db, city, categories['Baby & Toys'], shops)
    create_products_health(db, city, categories['Health'], shops)
    create_products_household(db, city, categories['Household'], shops)
    create_products_decor(db, city, categories['Decor'], shops)
    create_products_care(db, city, categories['Care and fragrance'], shops)

baby_products = {
    'Set of 6 balancing stones': [
        'A set of 6 balancing stones in different colors and shapes. Perfect for developing fine motor skills and creativity in children.',
        'https://www.rossmann.de/media-neu/150/MAM_15035715/MAM_15035715_SHOP_IMAGE_1.4.png',
    ],
    'Water ball track': [
        'A water ball track that allows children to play with water and balls. It helps develop hand-eye coordination and fine motor skills.',
        'https://www.rossmann.de/media-neu/153/MAM_15369649/MAM_15369649_SHOP_IMAGE_1.4.png',
    ],
    'Foldable toilet seat duck': [
        'A foldable toilet seat in the shape of a duck. It is easy to carry and use, making it perfect for potty training on the go.',
        'https://www.rossmann.de/media-neu/152/MAM_15272272/MAM_15272272_SHOP_IMAGE_1.4.png',
    ],
    'Diapers Extra Soft Premium Junior Size 5 (11-16 kg)': [
        'Extra soft diapers for children weighing 11-16 kg. They provide comfort and protection for your baby.',
        'https://www.rossmann.de/media-neu/155/MAM_15565619/MAM_15565619_SHOP_IMAGE_1.4.png',
    ],
}

def create_products_baby(db, cities: list[City], category: Category, shops: list[Shop]):
    for name, (description, image_url) in baby_products.items():
        product = create_product(
            db=db,
            name=name,
            description=description,
            category=category,
            image_url=image_url   
        )
        for city in cities:
            if city.city_name == 'Germany':
                price_map = {
                    'Set of 6 balancing stones': (16.99, 0.1),
                    'Water ball track': (9.99, 0),
                    'Foldable toilet seat duck': (7.99, 0.2),
                    'Diapers Extra Soft Premium Junior Size 5 (11-16 kg)': (12.99, 0.1)
                }
                add_product_to_city(db, product, city, price_map[name][0], price_map[name][1])
        for shop in shops:
            add_product_to_shop(db, product, shop, random.randrange(50, 200, 10)) 

def create_products_baby(db, city: City, category: Category,  shops: list[Shop]):
    product = create_product(
        db=db,
        name='Set of 6 balancing stones',
        description='A set of 6 balancing stones in different colors and shapes. Perfect for developing fine motor skills and creativity in children.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/150/MAM_15035715/MAM_15035715_SHOP_IMAGE_1.4.png'
    )
    add_product_to_city(db, product, city, 16.99, 0.1)
    
    add_product_to_shop(db, product, shops[0], 200, 16.99, 0.1)
    add_product_to_shop(db, product, shops[1], 150, 16.99)
    add_product_to_shop(db, product, shops[2], 100, 14.99, 0.05)

    
    product = create_product(
        db=db,
        name='Water ball track',
        description='A water ball track that allows children to play with water and balls. It helps develop hand-eye coordination and fine motor skills.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/153/MAM_15369649/MAM_15369649_SHOP_IMAGE_1.4.png'  
    )
    add_product_to_shop(db, product, shops[0], 100, 9.99)
    add_product_to_shop(db, product, shops[1], 80, 9.49, 0.2)
    add_product_to_shop(db, product, shops[2], 120, 8.99)

    product = create_product(
        db=db,
        name='Foldable toilet seat duck',
        description='A foldable toilet seat in the shape of a duck. It is easy to carry and use, making it perfect for potty training on the go.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/152/MAM_15272272/MAM_15272272_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 300, 7.99, 0.4)
    add_product_to_shop(db, product, shops[1], 250, 7.99, 0.4)
    add_product_to_shop(db, product, shops[2], 200, 7.49, 0.3)


    product = create_product(
        db=db,
        name='Diapers Extra Soft Premium Junior Size 5 (11-16 kg)',
        description='Extra soft diapers for children weighing 11-16 kg. They provide comfort and protection for your baby.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/155/MAM_15565619/MAM_15565619_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 80, 12.99)
    add_product_to_shop(db, product, shops[1], 50, 12.49)
    add_product_to_shop(db, product, shops[2], 60, 10.99)
def create_products_health(db, category: Category, shops: list[Shop]):
    product = create_product(
        db=db,
        name='Super-Haftcreme Neutral',
        description='Super adhesive cream for dentures. Provides a strong hold and comfort for denture wearers.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/159/MAM_15920344/MAM_15920344_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 200, 1.59, 0.1)
    add_product_to_shop(db, product, shops[1], 150, 1.59, 0.1)
    add_product_to_shop(db, product, shops[2], 100, 1.59)
    
    product = create_product(
        db=db,
        name='EZB 6100 Electric Toothbrush',
        description='An electric toothbrush with a 2-minute timer and 30-second interval timer. It helps you brush your teeth effectively.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/160/MAM_16022592/MAM_16022592_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 150, 89.99, 0.05)
    add_product_to_shop(db, product, shops[1], 120, 85.99)
    add_product_to_shop(db, product, shops[2], 200, 79.99)
    
    product = create_product(
        db=db,
        name='Rapid Alcohol Test',
        description='A rapid alcohol test that provides quick results. It is easy to use and helps you check your blood alcohol level.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/160/MAM_16033331/MAM_16033331_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 300, 6.99)
    add_product_to_shop(db, product, shops[1], 250, 6.99)
    add_product_to_shop(db, product, shops[2], 280, 6.49)  
def create_products_household(db, category: Category, shops: list[Shop]):
    product = create_product(
        db=db,
        name='Universal detergent liquid fresh cotton blossom 20 WL',
        description='A universal detergent liquid with a fresh cotton blossom scent. It is suitable for all types of fabrics and provides a deep clean.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/159/MAM_15914468/MAM_15914468_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 50, 5.49)
    add_product_to_shop(db, product, shops[1], 40, 5.49)
    add_product_to_shop(db, product, shops[2], 40, 4.99)
    
    product = create_product(
        db=db,
        name='Fabric softener concentrate Aprilfrisch 59 WL',
        description='A fabric softener concentrate with an April fresh scent. It provides long-lasting freshness and softness to your laundry.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/158/MAM_15880260/MAM_15880260_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 80, 3.29)
    add_product_to_shop(db, product, shops[1], 50, 2.99)
    add_product_to_shop(db, product, shops[2], 60, 2.99, 0.1)
    
    product = create_product(
        db=db,
        name='All-purpose cleaner spray bathroom',
        description='An all-purpose cleaner spray for the bathroom. It effectively removes dirt and limescale, leaving your bathroom clean and fresh.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/160/MAM_16063656/MAM_16063656_SHOP_IMAGE_1.4.png'   
    )
    add_product_to_shop(db, product, shops[0], 80, 3.29)
    add_product_to_shop(db, product, shops[1], 50, 2.99)
    add_product_to_shop(db, product, shops[2], 60, 2.99, 0.05)
def create_products_decor(db, category: Category, shops: list[Shop]):
    product = create_product(
        db=db,
        name='PopGrip Premium Glitter Rainbow Void',
        description='A PopGrip with a premium glitter design. It provides a secure grip for your phone and can be used as a stand.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/162/MAM_16258211/MAM_16258211_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 30, 17.99)
    add_product_to_shop(db, product, shops[1], 20, 17.99)
    add_product_to_shop(db, product, shops[2], 25, 16.99)
    
    product = create_product(
        db=db,
        name='LED starry sky light green',
        description='A LED light that creates a starry sky effect. It is perfect for creating a relaxing atmosphere in your home.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/161/MAM_16141130/MAM_16141130_SHOP_IMAGE_2.3.png'
    )
    add_product_to_shop(db, product, shops[0], 50, 7.99, 0.1)
    add_product_to_shop(db, product, shops[1], 40, 7.99, 0.1)
def create_products_care(db, category: Category, shops: list[Shop]):
    product = create_product(
        db=db,
        name='Beauty Scrub Blueberry Caramel Bliss',
        description='A beauty scrub with a blueberry caramel scent. It exfoliates and nourishes your skin',
        category=category,
        image_url='https://www.rossmann.de/media-neu/159/MAM_15986768/MAM_15986768_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 200, 7.95, 0.35)
    add_product_to_shop(db, product, shops[1], 150, 7.49, 0.3)
    add_product_to_shop(db, product, shops[2], 120, 6.99, 0.35)
    
    product = create_product(
        db=db,
        name='Anti-Gray Effect Coloring Conditioner',
        description='A coloring conditioner that helps reduce gray hair. It provides a natural color and shine to your hair.',
        category=category,
        image_url='https://www.rossmann.de/media-neu/158/MAM_15852682/MAM_15852682_SHOP_IMAGE_1.4.png'
    )
    add_product_to_shop(db, product, shops[0], 150, 15.99, 0.2)
    add_product_to_shop(db, product, shops[1], 120, 14.99, 0.2)
    add_product_to_shop(db, product, shops[2], 140, 12.99, 0.25)


if __name__ == '__main__':
    main()