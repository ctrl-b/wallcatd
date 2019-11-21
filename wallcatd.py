import requests, json, urllib.request, os, time, subprocess

url = 'https://beta.wall.cat/api/v1/channels/'
fresh = 'ea4KhWHUGE'
structure = 'RX1BtSlCrq'
north = 'tdA5aG8zpa'
time_day = '/image/' + time.strftime("%Y-%m-%d") + 'T00:00:00.000Z'

backgrounds = ['background', 'screensaver']
potd_background = url + fresh + time_day
potd_screensaver = url + structure + time_day
hostname = 'google.com'
response = os.system('ping -c 1 ' + hostname)

def urlify( str ):
    img = json.loads(requests.get( str ).text)['payload']['image']['url']['o']
    return img;

def current( str ):
    curr = subprocess.Popen('gsettings get org.gnome.desktop.' + str + ' picture-uri', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    return curr;

# Download picture of the day function
def downloadpotd( image, path ):
    with urllib.request.urlopen(image) as response, open(path, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)

# Set background function
def setbackground( where, image ):
    if where == 'background':
        os.system("/usr/bin/gsettings set org.gnome.desktop." + where + " picture-options 'zoom'")
    os.system("/usr/bin/gsettings set org.gnome.desktop." + where  + " picture-uri " + "'" + image + "'")

# Check if the image already exist locally
def checkexist( image ):
    picture = os.path.isfile(image)
    return picture;

# Get the image filename
def getimg( type ):
    calc = 'potd_' + type
    imguri = urlify(eval(calc))
    filename = imguri[imguri.rfind("/")+1:]
    path = os.environ['HOME'] + '/Pictures/' + filename + '.jpg'
    imgdata = [imguri, filename, path]
    return imgdata;
           
# check for internet connection first
if response == 0:

    print(hostname, 'is reachable, downloading images...')
    images = [
        urlify(potd_background),
        urlify(potd_screensaver)
    ]
   
    # Main loop function to setup, check and download images
    for background in backgrounds:

        # Get image of the day and set
        today = getimg(background)

        # Check if already exists as background
        if today[1] in current(background):
            print(background + ' already configured')

        # if not
        else:
            # check if exist on local, if exists, set it up
            if checkexist(today[2]):
                print(background + ' exists on local')
                setbackground( background, today[2])
                print('Setting ' + background)

            # If doesn't exists on local, download
            else:
                downloadpotd(today[0],today[2])
                print('Downloading ' + background)
                # Configurar
                setbackground( background, today[2])
                print('Setting ' + background)
else:
    print(hostname, ' not reachable')

