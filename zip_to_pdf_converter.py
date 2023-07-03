import sys
from zipfile import ZipFile
from PIL import Image
import io


def encode(zip_path: str) -> None:
    archive = ZipFile(zip_path, 'r')
    images = []
    for file in sorted(info.filename for info in archive.infolist()):
        data = archive.read(file)
        img = Image.open(io.BytesIO(data)).convert("RGB")
        images.append(img)

    images[0].save(zip_path + ".pdf", save_all=True, append_images=images[1:])


if __name__ == "__main__":
    encode(sys.argv[1])
