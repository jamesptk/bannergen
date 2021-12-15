from io import BytesIO

from flask import Flask, request, render_template, send_file
from flask_bootstrap import Bootstrap
from PIL import Image
from banner import make_banner

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template('banner.html')

    errors = []
    left = request.files.get('left-file')
    right = request.files.get('right-file')
    if not left:
        errors.append("Provide an image for the left side")
    if not right:
        errors.append("Provide an image for the right side")
    if errors:
        return render_template('banner.html', errors=errors)

    try:
        left_image = Image.open(left.stream)
    except OSError:
        errors.append("Left side file is not a recognised image format")
        left_image = None

    try:
        right_image = Image.open(right.stream)
    except OSError:
        errors.append("Right side file is not a recognised image format")
        right_image = None

    if errors:
        return render_template('banner.html', errors=errors)

    height = int(request.form.get('height', 640))
    banner = make_banner(left_image, right_image, height)
    img_io = BytesIO()
    banner.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run()
