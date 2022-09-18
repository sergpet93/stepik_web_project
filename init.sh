sudo /etc/init.d/mysql start
#mysql -uroot -e "create database web;"
#mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'box';"
#mysql -uroot -e "grant all privileges on web.*to'box'@'localhost' with grant option;"
sudo mysql -u root -e "CREATE DATABASE stepik_course;"
sudo mysql -u root -e "CREATE USER box@'%' IDENTIFIED BY 'box';"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON stepic_course.* TO box@'%' WITH GRANT OPTION;"
sudo mysql -u root -e "FLUSH PRIVILEGES;"
~/web/ask/manage.py makemigrations qa
~/web/ask/manage.py migrate qa
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c hello.py hello:wsgi_application & 
gunicorn -c /home/box/web/etc/qa.py ask.wsgi:application

