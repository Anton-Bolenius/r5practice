import os
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

def get_image_list():
    """
    Returns a sorted list of valid image filenames
    from the static/images/ directory.
    """
    image_directory = os.path.join(app.static_folder, 'images')
    if not os.path.exists(image_directory):
        return []

    allowed_extensions = {'.png', '.jpg', '.jpeg', '.gif'}
    files = []
    for file_name in sorted(os.listdir(image_directory)):
        extension = os.path.splitext(file_name)[1].lower()
        if extension in allowed_extensions:
            files.append(file_name)

    return files

@app.route('/')
def default():
    """
    Redirects to /0 (the first image).
    """
    return redirect('/0')

@app.route('/<int:index>')
def show_image(index):
    """
    Displays a single image at the given index.
    Shows next and previous links to cycle through images.
    """
    images = get_image_list()
    total = len(images)

    if total == 0:
        return "<h1>No images found in static/images</h1>"

    # Ensure index is within valid range by wrapping around
    index = index % total  # e.g., if index == total, wrap to 0

    image_file = images[index]
    next_index = (index + 1) % total
    prev_index = (index - 1) % total

    return render_template(
        'show_image.html',
        image_file=image_file,
        index=index,
        next_index=next_index,
        prev_index=prev_index,
        total=total
    )

if __name__ == '__main__':
    app.run(debug=True)
