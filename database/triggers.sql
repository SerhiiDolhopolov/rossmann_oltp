DROP TRIGGER IF EXISTS trigger_update_last_updated_utc_products ON products;
DROP TRIGGER IF EXISTS trigger_update_last_updated_utc_categories ON categories;
DROP TRIGGER IF EXISTS trigger_update_last_updated_utc_city_products ON city_products;
DROP TRIGGER IF EXISTS trigger_update_last_updated_utc_employees ON employees;

CREATE OR REPLACE FUNCTION update_last_updated_utc()
RETURNS TRIGGER AS $$
BEGIN
    NEW.last_updated_utc = CURRENT_TIMESTAMP AT TIME ZONE 'UTC';
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_last_updated_utc_products
BEFORE UPDATE ON products
FOR EACH ROW
EXECUTE FUNCTION update_last_updated_utc();

CREATE TRIGGER trigger_update_last_updated_utc_categories
BEFORE UPDATE ON categories
FOR EACH ROW
EXECUTE FUNCTION update_last_updated_utc();

CREATE TRIGGER trigger_update_last_updated_utc_city_products
BEFORE UPDATE ON city_products
FOR EACH ROW
EXECUTE FUNCTION update_last_updated_utc();

CREATE TRIGGER trigger_update_last_updated_utc_employees
BEFORE UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION update_last_updated_utc();