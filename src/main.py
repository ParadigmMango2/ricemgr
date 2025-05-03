from core import init
from shared import logger
from parser import parser


if __name__ == "__main__":
    init()

    # Pull args and invoke function
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
        logger.info("Invoked {}".format(args.func.__name__))
    else:
        parser.print_help()
        logger.info("Unable to invoke a function")
