import sys
import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description="Argument Parser"
    )
    sub_parser = parser.add_subparsers(dest='function', required=True)

    parser_add_function = sub_parser.add_parser('add', help='Call function "add"')
    parser_add_function.add_argument('description', help='Description is needed for "add" functionality')

    parser_update_function = sub_parser.add_parser('update', help='Call function "update"')
    parser_update_function.add_argument('id', help='id is needed for "update" functionality')
    parser_update_function.add_argument('description', help='description is needed for "update" functionality')

    parser_delete_function = sub_parser.add_parser('delete', help='Call function "delete"')
    parser_delete_function.add_argument('id', help='id is needed for "delete" functionality')

    parser_MIP_function = sub_parser.add_parser('mark-in-progress', help='Call function "mark-in-progress"')
    parser_MIP_function.add_argument('id', help='id is needed for "mark-in-progress" functionality')

    parser_MD_function = sub_parser.add_parser('mark-done', help='Call function "mark-done"')
    parser_MD_function.add_argument('id', help='id is needed for "mark-done" functionality')

    parser_list_function = sub_parser.add_parser('list', help='Call function "list"')
    parser_list_function.add_argument('status', nargs='?', help='status is optional for "list" functionality')

    return parser
