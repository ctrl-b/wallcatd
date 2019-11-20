wallcatd
========

Pictures of the day for your desktop and lockscreen using [wallcat](https://beta.wall.cat/)

## Dependencies

- python3

## Instructions

```shell
# Create the services folder if it doesn´t exist
mkdir -p ~/.config/systemd/user/

# Clone the repo
git clone https://github.com/6bytes/wallcatd.git ~/services/wallcatd/

# Create a symbolic link for your user
ln -s ~/services/wallcatd/wallcatd.service ~/.config/systemd/user/
ln -s ~/services/wallcatd/wallcatd.timer ~/.config/systemd/user/

# Enable the service:
systemctl enable --user wallcatd.service
systemctl enable --user wallcatd.timer
```


## To do/wishlist 

- [x] ~~Check for new wallpapers on unlock  session~~ This is handled by the timer

