
Vagrant.configure(2) do |config|

  config.vm.define "1810"
  config.vm.hostname = "1810"
  config.vm.box = "archlinux/archlinux"
  config.vm.box_check_update = true
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "private_network", type: "dhcp"
  # config.vm.provision "shell", path: "https://raw.githubusercontent.com/cloudmesh-community/book/master/install-arch.sh"
  config.vm.provision "shell", path: "install-arch.sh"  

  # config.vm.network "public_network"
  config.vm.synced_folder ".", "/home/vagrant/book"
  config.vm.provider "virtualbox" do |vb|
     # vb.gui = true
     vb.memory = "4096"
  end


end
