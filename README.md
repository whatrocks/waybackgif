# waybackgif
create a gif of chronological screenshots from any website on Wayback Machine

## Initial setup

```bash
python -m venv .waybackgif
source .waybackgif/bin/activate
pip install -r requirements.txt
```

Install [Chrome driver](https://sites.google.com/chromium.org/driver/) to `~/tmp/chromedriver`

## How to run

Change the url to the website of your choosing. Right now, the code is also only storing 1 image per year, but you can remove this filtering. Also these should both be command line options down the road!

```bash
python waybackgif.py
```

## Examples

Annual snapshot of apple.com (1996 - 2023)
![apple](./apple.gif)

Annual snapshot of stripe.com (2009 - 2023)
![stripe](./stripe.gif)


## Tips

Clean up snapshots:

```bash
rm snapshot*.png
```

Reduce file size of gif:

```bash
gifsicle -i original.gif -O3 --colors 256 -o optimized.gif
```
