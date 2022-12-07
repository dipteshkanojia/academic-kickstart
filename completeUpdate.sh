#!/bin/bash

echo "<footer class=\"site-footer\">
	<p>Last Updated: $(date +"%d-%m-%Y %H:%M:%S")</p>
	<p>\"Nearly everyone can stand adversity, but if you want to test their character, give them power.\"</p>
</footer>" > layouts/partials/site_footer.html

git add .
git commit -m "updates"
git push
hugo
cd public
git add .
git commit -m "updates"
git push
cd ..

