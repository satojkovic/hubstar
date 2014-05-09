#-*- coding: utf-8 -*-
import sys
import argparse
import os
from hubstar import Hubstar
from exceptions import *


def main():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [--unstar | -u] <owner/reposname>",
        description="star/unstar a repository"
    )

    parser.add_argument("-u", "--unstar",
                        dest="is_unstar",
                        action="store_true",
                        default=False,
                        help="unstar a repository")

    parser.add_argument("owner_reposname",
                        help="owner and repository name")

    args = parser.parse_args()

    try:
        if args.is_unstar:
            Hubstar(args.owner_reposname).unstar()
        else:
            Hubstar(args.owner_reposname).star()
    except HsErrorUnauthorized, e:
        sys.stderr.write(e.args[0])
        return e.error_code
    except HsErrorInternal, e:
        sys.stderr.write("Internal Error: %s\n" % e.args[0])
        return e.error_code
    except HsErrorUnknownObject, e:
        sys.stderr.write("Unknown Object: %s\n" % e.args[0])
        return e.error_code
    except Exception:
        import traceback
        sys.stderr.write("\n")
        sys.stderr.write(traceback.format_exc())
        return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
