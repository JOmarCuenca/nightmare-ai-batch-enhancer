from argparse import ArgumentParser
from dataclasses import dataclass

MIN_SCALE = 1
MAX_SCALE = 10


@dataclass(frozen=True)
class Args:
    inputPath: str
    outputPath: str
    verbose: bool
    scale: int
    face_enhance: bool


    def getArgs():
        parser = ArgumentParser(
            prog="Nightmae AI batch uploader",
            description="Sends images to be processed by Nightmare AI",
        )

        parser.add_argument('input_path', type=str,)
        parser.add_argument('--scale', type=int, default=4, dest="scale",
                            help="Scale factor for the AI model")
        parser.add_argument('--output', type=str, help="Output path",
                            dest="output_path", default="output")
        parser.add_argument('-v', default=False, help="Verbose", dest="verbose",
                            action="store_true")
        parser.add_argument('--face-enhance', default=False, action="store_true",
                            help="Enable face enhancing functionality in the AI model", dest="face_enhance",)

        args = parser.parse_args()

        return Args(
            args.input_path,
            args.output_path,
            args.verbose,
            max(MIN_SCALE, min(MAX_SCALE, args.scale)),
            args.face_enhance,
        )


if __name__ == '__main__':
    args = Args.getArgs()
    print(args)
