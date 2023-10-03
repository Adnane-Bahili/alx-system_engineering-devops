# Installs an Nginx server with a custom HTTP response header using Puppet
exec { 'command':
  command  => 'apt-get -y update; apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
