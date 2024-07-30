with FilterPeriod as (
    select 
        car_id,
        MONTH(start_date) as month
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where Year(START_DATE) = 2022 and MONTH(start_date) in (8,9,10)

)
select 
    month, car_id, count(*) as records
from 
    FilterPeriod
where 
    car_id 
    in (
        select
            car_id
        from 
            FilterPeriod
        group by 
            car_id
        having 
            count(*) >= 5
        )
group by month, car_id
having count(*) > 0
order by month asc, car_id desc

