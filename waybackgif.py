from waybackpy import WaybackMachineCDXServerAPI
from PIL import Image
import imageio
from selenium import webdriver
from time import sleep
import argparse
import datetime

def generate_wayback_gif(
    url,
    start_year="2020", 
    end_year=datetime.datetime.now().year
):
    print("Generating gif of " +
    f"annual screenshots of {url} "+
    f"from {start_year} - {end_year}")

    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(
            executable_path="~/tmp/chromedriver",
            options=options)

    api = WaybackMachineCDXServerAPI(
        url,
        "waybackgif agent",
        start_timestamp=f"{start_year}0101000000",
        end_timestamp=f"{end_year}1231235959"
    )
    snapshots = api.snapshots()

    screenshots = []

    count = 1
    datemonth = {}
    for snapshot in snapshots:
        if snapshot.statuscode != "200":
            continue
        date = str(snapshot.datetime_timestamp)[0:4]
        if date in datemonth:
            continue
        datemonth[date] = True
        driver.get(snapshot.archive_url)
        sleep(1)
        filename = "snapshot" + str(count) + ".png"
        driver.get_screenshot_as_file(filename)
        screenshots.append(filename)
        count += 1

    images = [Image.open(img) for img in screenshots]
    imageio.mimsave("result.gif", images, fps=2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a wayback gif')
    parser.add_argument('url', type=str, help='A valid URL')
    parser.add_argument(
        '--start_year',
        type=str,
        help='start year (optional, default: 2020)',
        default='2020')
    parser.add_argument(
        '--end_year', 
        type=str, 
        help='end year (optional, default: current year)', 
        default=str(datetime.datetime.now().year))
    args = parser.parse_args()

    generate_wayback_gif(args.url, args.start_year, args.end_year)