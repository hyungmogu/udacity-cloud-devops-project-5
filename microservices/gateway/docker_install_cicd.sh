apt remove docker-desktop;
rm -r $HOME/.docker/desktop;
rm /usr/local/bin/com.docker.cli;
apt purge docker-desktop;
apt-get update;
apt-get install ./docker-desktop-<version>-<arch>.deb;
systemctl --user start docker-desktop;
docker run hello-world;