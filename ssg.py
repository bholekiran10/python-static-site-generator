import typer
import Site from ssg.site

def main(source="content", dest="dist"):
    config ={source: "source",  dest:"dest"}
    my_site = Site(**config)
    my_site.build()

typer.run(main)