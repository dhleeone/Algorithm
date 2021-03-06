"""
ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
ANIMAL_INS 테이블 구조는 다음과 같으며, 
ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 
각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.
"""


-- 역순 정렬하기
SELECT NAME, DATETIME from ANIMAL_INS ORDER BY ANIMAL_ID DESC;


-- where절
SELECT ANIMAL_ID, NAME from ANIMAL_INS WHERE INTAKE_CONDITION='Sick';


-- where절(아닐 때)
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged';


-- 이름이 같을 시 늦은 날짜 순으로
SELECT ANIMAL_ID, NAME, DATETIME 
FROM ANIMAL_INS 
ORDER BY NAME, DATETIME DESC;


-- 상위 1개 레코드
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME LIMIT 1;


-- 최댓값 구하기
SELECT DATETIME AS '시간' FROM ANIMAL_INS
ORDER BY DATETIME 
DESC LIMIT 1;


-- 동물 수 구하기
SELECT COUNT(*) AS 'count' FROM ANIMAL_INS;


-- 중복 제거하기
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS;
-- count 함수는 Null을 세지 않음


-- 같은 테이블 join (https://programmers.co.kr/learn/courses/30/lessons/62284)
SELECT A.CART_ID
FROM CART_PRODUCTS AS A
INNER JOIN CART_PRODUCTS AS B
ON A.CART_ID = B.CART_ID
WHERE A.NAME = "Milk" AND B.NAME = "Yogurt";
