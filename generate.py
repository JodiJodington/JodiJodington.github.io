from pathlib import Path
import textwrap
from PIL import Image, ImageDraw, ImageFont

def main():
    Path("out/").mkdir(exist_ok=True)
    Path("out/blogs").mkdir(exist_ok=True)
    Path("out/images").mkdir(exist_ok=True)
    Path("out/images/blogs").mkdir(exist_ok=True)
    tail = open("tail.html", "r").read()
    with open("out/index.html", "w") as new:
        with open("index.html", "r") as old:
            new.write(prepareHeaderForFile("index.html", "Home"))
            new.write(old.read())
            new.write(tail)
    with open("out/contact.html", "w") as new:
        with open("contact.html", "r") as old:
            new.write(prepareHeaderForFile("contact.html", "Contact Me"))
            new.write(old.read())
            new.write(tail)
    with open("out/styles.css", "w") as new:
        with open("styles.css", "r") as old:
            new.write(old.read())
    with open("out/blogs.html", "w") as blogs_html:
        blogs_html.write(prepareHeaderForFile("blogs.html", "Blogs List"))
        blogs_html.write("<ul>")
        for blog in BLOGS:
            with open(f"out/{blog[0]}", "w") as new:
                with open(f"{blog[0]}", "r") as old:
                    new.write(prepareHeaderForFile(blog[0], blog[1]))
                    new.write(old.read())
                    new.write(tail)
                    blogs_html.write(f"<li> <a href='{blog[0]}'>{blog[1]}</a> </li>")
        blogs_html.write("</ul>")
        blogs_html.write(tail)

def prepareHeaderForFile(file, title):
    header = open("header.html", "r").read()
    header = header.replace("INSERT_TITLE_HERE", title)
    header = header.replace("INSERT_OG_URL_HERE", f"{BASE_URL}/file")
    header = header.replace("INSERT_OG_IMAGE_URL_HERE", getImageUrlForFile(file, title))
    return header

def getImageUrlForFile(file, text):
    path = f"images/{file}.png"
    img = generateImageWithText(text)
    img.save(f"out/{path}")
    return f"{BASE_URL}/{path}"

def generateImageWithText(text):
    img = Image.new('RGB', (1200, 630), color=(100, 100, 100))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default(100)
    wrapped_text = textwrap.fill(text, width=25, break_long_words=False, subsequent_indent='    ')
    draw.multiline_text((img.width // 2, img.height // 2), wrapped_text, font=font, fill=(255, 255, 255), anchor="mm")
    return img

BLOGS = [('blogs/nietzsche_antichrist_57.html', "An Interesting Aphorism from Nietzsche's The Antichrist")]
BASE_URL = "https://JodiJodington.github.io"

if __name__ == "__main__":
    main()
