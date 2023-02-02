from waybackpy import WaybackMachineCDXServerAPI
from PIL import Image
import imageio
from selenium import webdriver
from time import sleep

def generate_wayback_gif(url):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(
            executable_path="~/tmp/chromedriver",
            options=options)

    api = WaybackMachineCDXServerAPI(
        url,
        "waybackgif agent",
        start_timestamp=1995,
        end_timestamp=2023
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
    imageio.mimsave('apple2.gif', images, fps=2)

print("start")
generate_wayback_gif("www.apple.com")
print("done")
