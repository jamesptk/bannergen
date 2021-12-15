# Code originally by Sean Bamforth https://bitbucket.org/snippets/seanbamforth/5AMEEG
from PIL import Image, ImageDraw


def resize_image(img, iMaxHeight):
    wpercent = (iMaxHeight / float(img.size[1]))
    vsize = int((float(img.size[0]) * float(wpercent)))
    img = img.resize((vsize, iMaxHeight), Image.LANCZOS)
    return img


def make_banner(image1, image2, iHeight=640):
    image1 = resize_image(image1, iHeight)
    image2 = resize_image(image2, iHeight)

    iMaxWidth = image1.size[0] + image2.size[0]
    iMid = image1.size[0]

    nBarWidth = 0.28
    nTopTriangleHeight = 0.6

    output = Image.new('RGB', (iMaxWidth, iHeight))
    output.paste(image1, (0, 0))
    output.paste(image2, (iMid, 0))

    # put some triangles on it.
    draw = ImageDraw.Draw(output, 'RGBA')
    iLength = iHeight / 2
    iStart = int(iHeight * 0.3)
    draw.polygon([(iMid, iStart), (iMid - iLength, iHeight), (iMid + iLength, iHeight)], fill=(250, 160, 26, 255))

    iMid = image1.size[0]
    ileftBlack = iMid - int(iHeight * 0.215)
    iRightBlack = ileftBlack + int(iHeight * 0.6)
    iMidBlack = ileftBlack + int(iHeight * 0.3)
    iBar = int(iHeight * 0.1)

    draw.polygon([(ileftBlack, 0), (iRightBlack, 0), (iMidBlack, int(iHeight * 0.42))], fill=(21, 33, 23, 255))
    transpo = [(ileftBlack, 0), (ileftBlack + iBar, 0), (iMid + iLength + iBar, 640), (iMid + iLength, 640)]

    draw.polygon(transpo, fill=(250, 160, 26, 127))
    return output.convert('RGB')
