from pathlib import Path

def main():
    Path("out/").mkdir(exist_ok=True)
    Path("out/blogs").mkdir(exist_ok=True)
    with open("header.html", "r") as header:
        header_text = header.read()
        with open("out/home.html", "w") as new:
            with open("home.html", "r") as old:
                new.write(header_text)
                new.write(old.read())
        with open("out/contact.html", "w") as new:
            with open("contact.html", "r") as old:
                new.write(header_text)
                new.write(old.read())
        with open("out/blogs.html", "w") as blogs_html:
            blogs_html.write(header_text)
            blogs_html.write("<ul>")
            for blog in BLOGS:
                with open(f"out/blogs/{blog[0]}", "w") as new:
                    with open(f"blogs/{blog[0]}", "r") as old:
                        new.write(header_text)
                        new.write(old.read())
                        blogs_html.write(f"<li> <a href='blogs/{blog[0]}'>{blog[1]}</a> </li>")
            blogs_html.write("</ul>")


BLOGS = [('nietzsche_antichrist_57.html', "An Interesting Aphorism from Nietzsche's The Antichrist")]

main()
