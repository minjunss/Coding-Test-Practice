# select count(fish_info) as fish_count
# from fish_name_info fni
# left join fish_info fi on fni.fish_type = fi.fish_type

select count(*) as fish_count
from fish_info fi
join fish_name_info fni on fi.fish_type = fni.fish_type
where fni.fish_name in('BASS', 'SNAPPER')