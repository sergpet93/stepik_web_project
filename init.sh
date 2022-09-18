sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
#mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'box';"
#mysql -uroot -e "grant all privileges on web.*to'box'@'localhost' with grant option;"
mysql -uroot -e "create database foo_db;"
mysql -uroot -e "create user foo_user identified by 'foo_password';"
mysql -uroot -e "grant all on foo_db.* to 'foo_user'@'localhost';"
mysql -uroot -e "flush privileges;"
~/web/ask/manage.py makemigrations qa
~/web/ask/manage.py migrate qa
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c hello.py hello:wsgi_application & 
gunicorn -c /home/box/web/etc/qa.py ask.wsgi:application

