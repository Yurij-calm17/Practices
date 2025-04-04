-- 1. Отримати всі маршрути
SELECT * FROM Routes;
-- 2. Отримати всі транспортні засоби
SELECT * FROM Vehicles;
-- 3. Отримати всіх співробітників
SELECT * FROM Personnel;
-- 4. Отримати всі маршрути, які обслуговуються певним транспортним засобом
SELECT * FROM Serves WHERE vehicle_id = 1;
-- 5. Отримати всі транспортні засоби, що обслуговують певний маршрут
SELECT * FROM Serves WHERE route_id = 2;
-- 6. Отримати всі транспортні засоби та їх моделі
SELECT id, type, model FROM Vehicles;
-- 7. Отримати всіх водіїв
SELECT * FROM Personnel WHERE position = 'Driver';
-- 8. Отримати всі маршрути, довжина яких більша за 500 км
SELECT * FROM Routes WHERE distance_km > 500;
-- 9. Отримати всі транспортні засоби, швидкість яких перевищує 100 км/год
SELECT * FROM Vehicles WHERE speed_kmh > 100;

-- 10. Отримати всі транспортні засоби з вантажопідйомністю більше 10 тонн
SELECT * FROM Vehicles WHERE load_capacity_ton > 10;

-- 11. Отримати всіх співробітників з досвідом більше 5 років
SELECT * FROM Personnel WHERE experience_years > 5;

-- 12. Отримати всі маршрути між Києвом та будь-яким містом
SELECT * FROM Routes WHERE start_point = 'Kyiv' OR end_point = 'Kyiv';

-- 13. Отримати всіх співробітників, які призначені на певний транспортний засіб
SELECT * FROM serves WHERE vehicle_id = 3;

-- 14. Додати новий маршрут
INSERT INTO Routes (name, start_point, end_point, distance_km, average_time_hr) 
VALUES ('Route F', 'Kharkiv', 'Odessa', 650.00, 7.8);

-- 15. Оновити середній час проходження маршруту
UPDATE Routes SET average_time_hr = 8.2 WHERE id = 1;

-- 16. Видалити маршрут
DELETE FROM Routes WHERE id = 5;

-- 17. Отримати всі транспортні засоби, що мають тип "Truck"
SELECT * FROM Vehicles WHERE type = 'Truck';

-- 18. Отримати кількість співробітників за кожною посадою
SELECT position, COUNT(*) FROM Personnel GROUP BY position;

-- 19. Отримати список маршрутів з відповідними транспортними засобами
SELECT r.name, v.model FROM Routes r 
JOIN Serves s ON r.id = s.route_id 
JOIN Vehicles v ON s.vehicle_id = v.id;