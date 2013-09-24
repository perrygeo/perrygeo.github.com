# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.share_folder "v-app", "/usr/local/src/perrygeo.github.com", "./"
  #config.vm.provision :shell, :inline => "sudo apt-get update -y && sudo apt-get install -y ruby rubygems libmysql-ruby1.9.1 libhtmlentities-ruby1.9.1 python-pygments ruby-liquid && sudo gem install jekyll"
  config.vm.forward_port 4000, 4000
end
