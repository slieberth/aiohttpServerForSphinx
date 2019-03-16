import pathlib
import sys
import argparse

from aiohttp import web


def main():

    epilogTXT = """

    ... a mini http server for Sphinx HTML builds  """

    parser = argparse.ArgumentParser(epilog=epilogTXT, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-p", "--port",
                            default=8080, type=int,
                            help="http listening port")
    cliargs = parser.parse_args()
    cliArgsDict = vars(cliargs)
    print (cliArgsDict)
    app = web.Application()
    app.router.add_static('/', pathlib.Path(__file__).parent, show_index=True)
    #web.run_app(app)
    web.run_app(app, host='0.0.0.0', port=cliArgsDict["port"])


if __name__ == "__main__":
    sys.exit(main())
