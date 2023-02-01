from waybackpy import WaybackMachineCDXServerAPI
from PIL import Image
import imageio
from selenium import webdriver
from time import sleep

def generate_wayback_gif(url):
    driver = webdriver.Chrome(executable_path="~/tmp/chromedriver")

    api = WaybackMachineCDXServerAPI(
        url,
        "waybackgif",
        start_timestamp=2022,
        end_timestamp=2023
    )
    snapshots = api.snapshots()

    screenshots = []

    count = 1
    for snapshot in snapshots:
        driver.get(snapshot.archive_url)
        sleep(1)
        filename = "snapshot" + str(count) + ".png"
        driver.get_screenshot_as_file(filename)
        screenshots.append(filename)
        count += 1

    images = [Image.open(img) for img in screenshots]
    imageio.mimsave('wayback.gif', images, fps=2)

print("start")
generate_wayback_gif("https://www.charlieharrington.com")
print("done")
