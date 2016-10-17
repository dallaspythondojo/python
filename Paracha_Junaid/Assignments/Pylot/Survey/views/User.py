<html>
	<head>
		<link rel="stylesheet" href="/static/css/styles.css" type="text/css">
	</head>
	<body>
		<h1>User:</h1>
		<h3>Name:  {{session['name']}}</h3>
		<h3>Dojo Location:  {{session['location']}}</h3>
		<h3>Favoriot Laungage:  {{session['language']}}</h3>
		<p>Comment: {{session['comment']}}</p>
		<form action='/' method='post'>    	
			<input type="submit" name="back" value="Go Back">
		</form>

	</body>
</html>