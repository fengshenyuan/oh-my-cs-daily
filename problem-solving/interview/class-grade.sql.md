```sql
create table grade (
    ID VARCHAR(255),
    Name VARCHAR(255),
    Class VARCHAR(255), 
    Subject VARCHAR(255),
    Score Integer,
    Exam_round VARCHAR(255)
);

INSERT INTO GRADE VALUES 
('1', 'XIAOMING', '1', 'Chinese', 100, 1),
('1', 'XIAOMING', '1', 'Chinese', 90, 2),
('1', 'XIAOMING', '1', 'Chinese', 80, 3),
('1', 'XIAOMING', '1', 'Math', 100, 1),
('1', 'XIAOMING', '1', 'Math', 90, 2),
('1', 'XIAOMING', '1', 'Math', 80, 3),
('1', 'XIAOMING', '1', 'English', 100, 1),
('1', 'XIAOMING', '1', 'English', 90, 2),
('1', 'XIAOMING', '1', 'English', 80, 3);



('3', 'XIAOYu', '2', 'Chinese', 90, 1),
('3', 'XIAOYu', '2', 'Chinese', 95, 2),
('3', 'XIAOYu', '2', 'Chinese', 100, 3),
('3', 'XIAOYu', '2', 'Math', 85, 1),
('3', 'XIAOYu', '2', 'Math', 95, 2),
('3', 'XIAOYu', '2', 'Math', 100, 3),
('3', 'XIAOYu', '2', 'English', 100, 1),
('3', 'XIAOYu', '2', 'English', 90, 2),
('3', 'XIAOYu', '2', 'English', 100, 3);


1. Max_Round Score Sheet
ID, Name, Class, Chinese, Math, English, Total
1, XIAOMING, 1, 80, 80, 80, 240
2, XIAOHONG, 1, 85, 85, 85, 255


2. Max_Round Score Sheet with Rank
ID, Name, Class, Chinese, Math, English, Total, Class_Rank, Grade_Rank
1, XIAOMING, 1, 80, 80, 80, 240, 2, 2
2, XIAOHONG, 1, 85, 85, 85, 255, 1, 1


3. Max_Round Score Sheet with Rank with Upgarde
ID, Name, Class, Chinese, Math, English, Total, Class_Rank, Grade_Rank, Class_Upgrade, Grade_Upgrade
1, XIAOMING, 1, 80, 80, 80, 240, 2, 2, -1, -1
2, XIAOHONG, 1, 85, 85, 85, 255, 1, 1, 1, 1

// Solution with Snowflake SQL
with gradex as (
  select 
      ID, 
      NAME, 
      CLASS, 
      CHINESE, 
      MATH, 
      ENLIGHST, 
      IFNULL(PHYSICS, 0) as PHYSICS, 
      (CHINESE + MATH + ENLIGHST + IFNULL(PHYSICS, 0)) as TOTAL, 
      EXAM_ROUND,
      rank() over (partition by class, EXAM_ROUND order by total desc) Class_Rank,
      rank() over (partition by EXAM_ROUND order by total desc) Grade_Rank
  from 
      TEST.GRADE PIVOT(max(SCORE) for subject in ('Chinese', 'Math', 'English', 'Physics')) as p(ID, NAME, CLASS, EXAM_ROUND, CHINESE, MATH, ENLIGHST, PHYSICS) 
)
select 
    *,
    LAG(Class_Rank, 1, null) over (partition by ID, class order by exam_round ASC) - Class_Rank as Class_Upgrade, 
    LAG(Grade_Rank, 1, null) over (partition by ID, class order by exam_round ASC) - Grade_Rank as Grade_Upgrade 
from
    gradex
order by
    ID, exam_round
;


```
