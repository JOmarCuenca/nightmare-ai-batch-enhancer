import replicate

key = open("api.key", "r").read().strip()

assert key != "", "Please enter your API key in api.key"

aiClient = replicate.Client(api_token=key)

output = aiClient.run(
    "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
    input={"image": open("example2.jpg", "rb")}
)
print(f"Output: {output}")

## now using requests we download the image
import requests
with open("output.png", "wb") as f:
    f.write(requests.get(output).content)
