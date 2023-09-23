#setting up a client's SSH configuration file
exec { 'ssh_config':
  path    => '/etc/ssh',
  command => "/bin/echo 'IdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config; /bin/echo 'PasswordAuthentication no' >> /etc/ssh/ssh_config",
}
