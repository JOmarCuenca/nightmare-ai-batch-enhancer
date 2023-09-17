#!/home/omarcuenca/Coding/ai/image_enhancer/env/bin/python3

from loguru import logger
from replicate import Client
from requests import get

from args import Args
from fileManager import FileManager

__REATEMPTS = 5
__REATTEMPT_DELAY = 3  # seconds


def __getKey(apiKeyPath: str):
    key = open(apiKeyPath, "r").read().strip()
    assert key != "", "Please enter your API key in api.key"
    return key


def __validateUrl(url: str):
    assert url != "", "Please enter a valid url"
    assert url.startswith("http"), "Please enter a valid url"
    return url


def getClient(apiKeyPath: str):
    return Client(api_token=__getKey(apiKeyPath))


def enhanceImage(client: Client, outputPath: str, scale: int, face_enhance: bool):
    output = client.run(
        "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
        input={"image": open(outputPath, "rb"),
               "scale": scale, "face_enhance": face_enhance},
    )
    return output


def downloadImage(url: str, path: str):
    with open(path, "wb") as file:
        response = get(url)
        file.write(response.content)


def __downloadImage(img_path: tuple[str, str]):
    from time import sleep

    img, outputFilePath = img_path

    try:
        logger.debug(f"Processing -> {img}")

        counter = 0

        success = False

        while not success and counter < __REATEMPTS:
            try:
                # Enhance the image
                output = enhanceImage(
                    client, img, args.scale, args.face_enhance)

                __validateUrl(output)
                success = True
            except Exception as e:
                logger.error(
                    '\n'.join([f"Failed to enhance {img} because of {e}", f"Retrying... {counter + 1}/{__REATEMPTS}", f"URL: {output}"]))
                counter += 1
                sleep(__REATTEMPT_DELAY)

        if not success and counter == __REATEMPTS:
            raise Exception(
                f"Failed to enhance {img} after {counter} attempts, aborting...")

        # Save the enhanced image
        downloadImage(output, outputFilePath)

        logger.debug(f"Saved enhanced image to {outputFilePath}")

    except Exception as e:
        # Log the failure
        logger.error(f"Failed to enhance {img} because of {e}")

    logger.debug(f" Finished processing {img} ".center(100, '-') + '')


if __name__ == '__main__':
    from datetime import datetime
    from multiprocessing import Pool

    from tqdm import tqdm

    __THREAD_POOL_SIZE = 4

    args = Args.getArgs()
    inputFM = FileManager(args.inputPath)
    outputFM = FileManager(args.outputPath)

    if not args.verbose:
        logger.disable("__main__")

    logger.add(f"logs/{datetime.now().strftime('%d-%m-%y_%H:%M:%S')}.log")

    imgs = inputFM.getImagesDirs()
    client = getClient(args.apiKeyPath)

    nameGenerator = outputFM.getNextValidName(
        FileManager.getExtension("output.png"))

    imgs_paths = zip(imgs, [next(nameGenerator) for _ in range(len(imgs))])

    with Pool(__THREAD_POOL_SIZE) as p:
        list(tqdm(p.imap(__downloadImage, imgs_paths), total=len(imgs)))

    logger.enable("__main__")

    logger.info(f"Enhanced {len(imgs)} images")
    logger.info("Done!")
