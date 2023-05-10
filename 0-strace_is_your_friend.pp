# 0-strace_is_your_friend.pp

# Ensure Apache package is installed
package { 'apache2':
  ensure => installed,
}

# Replace the faulty Apache configuration file with the correct one
file { '/etc/apache2/apache2.conf':
  ensure => file,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
  source => 'puppet:///modules/my_module/apache2.conf',  # Replace with the correct source path
  notify => Service['apache2'],
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}

