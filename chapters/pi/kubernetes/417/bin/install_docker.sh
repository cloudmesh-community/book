#!/bin/sh

# Install Docker
curl -sSL get.docker.com | sh && \
  sudo usermod pi -aG docker

# Disable Swap
sudo dphys-swapfile swapoff && \
  sudo dphys-swapfile uninstall && \
  sudo update-rc.d dphys-swapfile remove
echo Adding " cgroup_enable=cpuset cgroup_enable=memory" to /boot/cmdline.txt and rebooting...
sudo cp /boot/cmdline.txt /boot/cmdline_backup.txt
# if you encounter problems, try changing cgroup_memory=1 to cgroup_enable=memory.
orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=1"
echo $orig | sudo tee /boot/cmdline.txt
reboot
