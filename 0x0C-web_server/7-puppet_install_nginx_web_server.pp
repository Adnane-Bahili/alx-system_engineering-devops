# Installs an Nginx server using Puppet

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx,
}
exec {'main page string'
path       => '/var/www/nginx/html'
command    => "/bin/echo 'Hello World!' | sudo tee /var/www/nginx/html/index.html",
}
exec { 'default config':
  path     => '/etc/nginx/sites-available',
  command  => "/bin/echo 'server {
  listen 80;
  listen [::]:80;
  server_name servingweb.tech;
  root /var/www/nginx/html;
  index index.html;
  location /redirect_me {
    return 301 https://en.wikipedia.org/wiki/Nginx;
  }
  error_page 404 /404.html;
  location /404 {
    root /etc/nginx/html;
    internal;
  }
}' > /etc/nginx/sites-available/default",
}
