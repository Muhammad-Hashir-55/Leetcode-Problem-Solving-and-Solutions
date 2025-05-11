-- Cheapest flight for each aircraft
SELECT * FROM Flights f1
WHERE price = (
  SELECT MIN(price)
  FROM Flights
  WHERE aircraft_id = f1.aircraft_id
);

-- Most expensive flight for each aircraft
SELECT * FROM Flights f2
WHERE price = (
  SELECT MAX(price)
  FROM Flights
  WHERE aircraft_id = f2.aircraft_id
);
