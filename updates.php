d<?php 

function all_delete()
{
	if(have_posts()){

		while(have_posts()){
			$id_post = get_the_ID();
			the_post();
			print '<p>';
			print $id_post;
			wp_delete_post($id_post);			
			print '<p>';
					
		}	
	}

}



	require('./wp-blog-header.php');
       


        $my_post = array(
        'post_title' => '',
        'post_content' => 'This is my post.',
        'post_status' => 'publish',
        'post_author' => 1,
        'post_category' => array(8,39)
        );



	$hostname = DB_HOST; 
	$username = DB_USER; 
	$password = DB_PASSWORD; 
	$dbName = DB_NAME; 
	$userstable = "tb_small_pictures";
    $path = "wp-content/small_pic/";	

//	echo "Hello";
	echo "<p>";

//	$id = 0;

	$id = apc_fetch('current_value');
//	apc_store('current_value', $id);

	print $id;


	$link = mysql_connect($hostname,$username,$password) OR DIE("Не могу создать соединение "); 
     	mysql_select_db($dbName) or die(mysql_error());  
	$query = "SELECT * FROM $userstable where id > $id order by rand()"; 
//		print $query;
	print '<p>';

	$res = mysql_query($query) or die(mysql_error()); 
	
	$number = mysql_num_rows($res);
	$size = $number;

	$id = $id + $number;
	apc_store('current_value', $id);


	print $id;
	print '<p>';
 	
	$i = 1;
	
	while($row=mysql_fetch_array($res)) {

		$small_name = $row['name']; 
        $name = substr($small_name, 6, 36);

        $text = "<div id=\"gallery\"> <a href=\"wp-content/pic/".$name."\"><img src=\"wp-content/small_pic/".$small_name."\"  alt=\"\"/></a> </div>"."

<div class=\"share42init\" data-url=\"http://178.49.201.102/wordpress/wp-content/pic/".$name."\" data-title=\"Funny pic\"></div>

<script type=\"text/javascript\" src=\"/wordpress/js/share42.js\"></script>
<script type=\"text/javascript\">share42('/wordpress/img/')</script>";

//		$record = "<img src='".$path.$small_name."'>"; 

		$my_post['post_title'] = strval($i);
		$my_post['post_content'] = $text;				

//        print $text;

		wp_insert_post( $my_post );
		
		$i+=1;
		$size-=1;
		print "<p>";	
	}


//	all_delete();

?>
