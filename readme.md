wallcatd
========

Pictures of the day for your desktop and lockscreen using [wallcat](https://beta.wall.cat/)

## Dependencies

- python3

## Instructions

```shell
# Create the services folder if it doesn´t exist
mkdir -p ~/.config/systemd/user/

# Clone the repo and cd into it
git clone https://github.com/6bytes/wallcatd.git ~/services/wallcatd/ && cd services/wallcatd/

# Copy the service file for your user
cp wallcatd.service ~/.config/systemd/user/

# Enable the service:
systemctl enable --user wallcatd.service
```


## To do/wishlist 

- [ ] Check for new wallpapers on unlock  session
