from pathlib import Path

def main():
    Path("out/").mkdir(exist_ok=True)
    Path("out/blogs").mkdir(exist_ok=True)
    header = open("header.html", "r").read()
    tail = open("tail.html", "r").read()
    with open("out/index.html", "w") as new:
        with open("index.html", "r") as old:
            new.write(header.replace("INSERT_TITLE_HERE", "Jodi's Site"))
            new.write(old.read())
            new.write(tail)
    with open("out/contact.html", "w") as new:
        with open("contact.html", "r") as old:
            new.write(header.replace("INSERT_TITLE_HERE", "Contact Me"))
            new.write(old.read())
            new.write(tail)
    with open("out/styles.css", "w") as new:
        with open("styles.css", "r") as old:
            new.write(old.read())
    with open("out/blogs.html", "w") as blogs_html:
        blogs_html.write(header.replace("INSERT_TITLE_HERE", "Blogs"))
        blogs_html.write("<ul>")
        for blog in BLOGS:
            with open(f"out/blogs/{blog[0]}", "w") as new:
                with open(f"blogs/{blog[0]}", "r") as old:
                    new.write(header.replace("INSERT_TITLE_HERE", blog[1]))
                    new.write(old.read())
                    new.write(tail)
                    blogs_html.write(f"<li> <a href='blogs/{blog[0]}'>{blog[1]}</a> </li>")
        blogs_html.write("</ul>")
        blogs_html.write(tail)


BLOGS = [('nietzsche_antichrist_57.html', "An Interesting Aphorism from Nietzsche's The Antichrist")]

main()
