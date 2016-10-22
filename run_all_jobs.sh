end_date=$(date +%Y-%m-%d)
d=2016-10-07
all_jobs="users total_hits total_users top_10_pages sessions users_by_country new_users lost_users facebook_conversion"	 
while [ "$d" != "$end_date" ]; do 
	for job in $all_jobs 
	do
		hadoop fs -test -d /user/aseregin/$job/$d
		if [ $? = 0 ] 
			then echo "$job/$d already exists skip"
		else
			./$job.sh $d
		fi
	done
	d=$(date -I -d "$d + 1 day")
done
