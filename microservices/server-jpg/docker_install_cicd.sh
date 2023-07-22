apt remove docker-desktop;
rm -r $HOME/.docker/desktop;
rm /usr/local/bin/com.docker.cli;
apt purge docker-desktop;
apt-get update;
apt-get install ./docker-desktop-4.21.1-x86_64.deb;
systemctl --user start docker-desktop;
docker run hello-world;