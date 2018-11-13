import sys
from argparse import ArgumentParser


class Parameters(object):

    def __init__(self):
        self.user_name = None
        self.token = None
        self.graph_name = None
        self.poem = None

    def parse(self, default_user_name: str, default_token: str):
        parser = self._create_parser(default_user_name, default_token)
        args = parser.parse_args()

        self.user_name = args.user_name
        self.token = args.token
        self.graph_name = args.graph
        self.poem = args.poem

        if not self.user_name:
            self._parameter_error(parser, 'user name is not set')
        if not self.token:
            self._parameter_error(parser, 'token is not set')

    @staticmethod
    def _create_parser(default_user_name, default_token):
        parser = ArgumentParser(prog='pixela-letters',
                                description="Let's write poems on Pixela graph!",
                                epilog='Thanks Pixela: https://pixe.la')

        parser.add_argument('-u', '--user-name', default=default_user_name,
                            help='set Pixela username. use environment value if option is not specified.')
        parser.add_argument('-t', '--token', default=default_token,
                            help='set Pixela token. use environment value if option is not specified.')
        parser.add_argument('-g', '--graph', required=True,
                            help='set Pixela graph name that will be written letters.')
        parser.add_argument('poem',
                            help='set poem that will be written to the graph.')
        return parser

    @staticmethod
    def _parameter_error(parser: ArgumentParser, message: str):
        print(message, file=sys.stderr)
        parser.print_help(file=sys.stderr)
        exit(1)
