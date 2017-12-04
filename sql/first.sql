Select first_name
From User
Where id_user = (
		 Select TOP 1 id_user
		 From Comments
		 Group by id_user
		 Order by count(*) desc
		);

		
