sudo /etc/init.d/mysql start
#mysql -uroot -e "create database web;"
#mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'box';"
#mysql -uroot -e "grant all privileges on web.*to'box'@'localhost' with grant option;"
sudo mysql -uroot -e "CREATE DATABASE ask CHARACTER SET utf8;"
sudo mysql -uroot -e "CREATE USER 'sa'@'localhost' IDENTIFIED BY 'pass';"
sudo mysql -uroot -e "GRANT ALL ON ask.* TO 'sa'@'localhost';"
~/web/ask/manage.py makemigrations qa
~/web/ask/manage.py migrate qa
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c hello.py hello:wsgi_application & 
gunicorn -c /home/box/web/etc/qa.py ask.wsgi:application

