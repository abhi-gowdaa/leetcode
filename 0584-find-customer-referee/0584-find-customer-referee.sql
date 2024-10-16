# Write your MySQL query statement below
#coalese replases null with 0
#advance solution
# SELECT name 
# FROM Customer
# WHERE COALESCE(referee_id,0) != 2;

select name from Customer
where referee_id!=2 or referee_id is null;
 