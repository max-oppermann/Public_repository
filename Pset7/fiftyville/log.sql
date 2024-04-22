-- Keep a log of any SQL queries you execute as you solve the mystery.

-- July 28, 2023 and that it took place on Humphrey Street
SELECT description FROM crime_scene_reports
WHERE street = 'Humphrey Street' AND year = 2023 AND month = 7 AND day = 28;

-- Theft of the CS50 duck took place at 10:15am. Interviews today (28.7.2012) with three witnesses
--  each of their interview transcripts mentions the bakery.
SELECT name, transcript FROM interviews
WHERE year = 2023 AND month = 7 and day = 28;

-- Ruth: Saw Thief leave within 10 minutes by car (license plate; bakery surveillance)
-- EUgene: saw thief withdraw money from ATM on Leggett Street "earlier this morning" (before 10:15)
-- Raymond: a) Thief on phone when leaving (less than 1 minute)
--          b) Planning on taking earliest flight out "tomorrow" = 29.07.2023
--          c) Other person should buy the tickets
-- Lily: Sons RObert/Patrick took loud rooster from courthouse; crows at 6am

-- bakery_security_logs activity/license_plate between 10:15 and 10:25; WHERE minute BETWEEN 15 AND 25;
-- phone_calls caller/receiver
-- atm_transactions account_number (-> table bank_accounts)

-- finding out what to put into the query:
SELECT DISTINCT transaction_type FROM atm_transactions;
SELECT DISTINCT duration FROM phone_calls;

SELECT activity, license_plate
FROM bakery_security_logs
WHERE minute BETWEEN 15 AND 25
AND year = 2023 AND month = 7 and day = 28 AND hour = 10;
-- 8 plates, all exit

SELECT caller, receiver FROM phone_calls
WHERE year = 2023 AND month = 7 and day = 28
AND duration BETWEEN 0 and 60;
-- 10 different numbers

SELECT account_number, amount FROM atm_transactions
WHERE year = 2023 AND month = 7 and day = 28
AND transaction_type = 'withdraw'
AND atm_location = 'Leggett Street';
-- 8 different account numbers



-- Every person has a license plate
SELECT name FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE minute BETWEEN 15 AND 25
    AND year = 2023 AND month = 7 and day = 28 AND hour = 10);
-- Barry, Bruce, Diana, Iman, Kelsey, Luca, Sofia, Vanessa

-- Every person has a phone number
SELECT name from people
WHERE phone_number in (
    SELECT caller FROM phone_calls
    WHERE year = 2023 AND month = 7 and day = 28
    AND duration BETWEEN 0 and 60
);
-- Full list: Benista, Bruce, Carina, Diana, Kathryn, Kelsey, Kenny, Sofia, Taylor
-- Leftovers: Bruce, Diana, Kelsey, Sofia

-- Bank accounts have numbers and person_ids
SELECT name FROM
people JOIN bank_accounts on people.id = bank_accounts.person_id
WHERE bank_accounts.account_number IN (
    SELECT account_number FROM atm_transactions
    WHERE year = 2023 AND month = 7 and day = 28
    AND transaction_type = 'withdraw'
    AND atm_location = 'Leggett Street'
);
-- Full list: Benista, Brooke, Bruce, Diana, Iman, Kenny, Luca, Taylor
-- Leftovers:
-- Bruce and Diana left from the bakery at the correct time, made a call with the correct duration,
-- and withdrew money at the right time and place.

-- from where do they even leave
SELECT id, full_name, abbreviation FROM airports WHERE city = 'Fiftyville';
-- id = 8; Fiftyville Regional Airport; CSF

-- Earliest flights, then can compare passengers:
SELECT id, destination_airport_id, hour from flights
WHERE year = 2023 AND month = 7 and day = 29
ORDER BY hour LIMIT 5;
--| 36 | 4                      | 8
--| 43 | 1                      | 9
-- flight-id; destination id; hour

SELECT passport_number, name FROM people
WHERE name = 'Bruce' or name = 'Diana';
-- | 3592750733      | Diana
-- | 5773159633      | Bruce

SELECT passport_number from passengers
WHERE flight_id = 36 AND passport_number = 3592750733 or passport_number = 5773159633;
-- 5773159633; Bruce was on the earliest flight out of Fiftyville, but not Diana.

SELECT destination_airport_id FROM flights
WHERE id = 36;
-- 4

Select abbreviation, full_name, city from airports
WHERE id = 4;
-- | LGA          | LaGuardia Airport | New York City

-- The accomplice must be the receiver of the call:
Select phone_number FROM people
WHERE name = 'Bruce';
-- (367) 555-5533

SELECT id, receiver FROM phone_calls
WHERE year = 2023 AND month = 7 and day = 28
AND duration BETWEEN 0 and 60
AND caller = '(367) 555-5533';
--  233 | (375) 555-8161

SELECT name from people
WHERE phone_number = '(375) 555-8161';
-- Robin ('Bruce' like Bruce Wayne ...)
