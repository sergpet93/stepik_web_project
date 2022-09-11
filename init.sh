sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
mysql -uroot -e "grant all privileges on web.*to'box'@'localhost' with grant option;"
~/ask/manage.py makemigrations
~/ask/manage.py migrate
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c hello.py hello:wsgi_application & 
gunicorn -c /home/box/web/etc/qa.py ask.wsgi:application

