sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
#mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'box';"
#mysql -uroot -e "grant all privileges on web.*to'box'@'localhost' with grant option;"
mysql -uroot -e "CREATE USER 'trasea'@'localhost' IDENTIFIED BY 'trasea';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'trasea'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
~/web/ask/manage.py makemigrations qa
~/web/ask/manage.py migrate qa
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c hello.py hello:wsgi_application & 
gunicorn -c /home/box/web/etc/qa.py ask.wsgi:application

