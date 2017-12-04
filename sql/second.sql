Update Users
Set status = "block"
Where id_user in ( Select top 10 id_user
	           From Users 
	           Where id_user not in (
					Select Distinct id_user 
					from Comments
					)					
		 );
			
