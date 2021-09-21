
import jp_proxy_widget

def greeting():
    greeter = jp_proxy_widget.JSProxyWidget()
    greeter.element.html("<h2>Hello world</h2>")
    greeter.element.css("color", "magenta")
    greeter.element.css("background-color", "blue")
    greeter.element.width(200)
    # Add a click callback
    def callback(*ignored_arguments):
        greeter.element.html("<h1><em>That tickles</em></h1>")

    # attach the callback
    greeter.element.on("click", callback)
    return greeter
