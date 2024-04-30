select (
        select count(*) 
        from fish_info 
        where fish_type = (select fish_type from fish_name_info where fish_name = 'BASS')
       )
    +   
       (
        select count(*) 
        from fish_info 
        where fish_type = (select fish_type from fish_name_info where fish_name = 'SNAPPER')
       )
as fish_count;