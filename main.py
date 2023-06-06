from replicate import Client
from args import Args
from fileManager import FileManager
from requests import get
from loguru import logger


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


if __name__ == '__main__':
    from datetime import datetime


    args = Args.getArgs()
    inputFM = FileManager(args.inputPath)
    outputFM = FileManager(args.outputPath)

    logger.add(f"logs/{datetime.now().strftime('%d-%m-%y_%H:%M:%S')}.log")

    imgs = inputFM.getImagesDirs()
    client = getClient(args.apiKeyPath)

    nameGenerator = outputFM.getNextValidName(
                    FileManager.getExtension("output.png"))

    for img in imgs:
        try:
            logger.debug(f"Processing -> {img}")

            # Enhance the image
            # output = enhanceImage(
            #     client, img, args.scale, args.face_enhance)

            # __validateUrl(output)

            outputFilePath = next(nameGenerator)

            # # Save the enhanced image
            # downloadImage(output, outputFilePath)

            logger.debug(f"Saved enhanced image to {outputFilePath}")

        except Exception as e:
            # Log the failure
            logger.error(f"Failed to enhance {img} because of {e}")

        logger.debug(f" Finished processing {img} ".center(100, '-') + '')

    logger.info(f"Enhanced {len(imgs)} images")
