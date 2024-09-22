from utils.argument_parser import get_parser
from utils.task_utils import add_task, update_task, delete_task, list_task, list_task_by_status, update_task_generic

args = get_parser().parse_args()


if args.function == "add":
    add_task(args.description)

if args.function == "update":
    update_task(args.id, args.description)

if args.function == "delete":
    delete_task(args.id)

if args.function == "list":
    if args.status is not None:
        list_task_by_status(args.status)
    else:
        list_task()

if args.function == "mark-in-progress":
    update_task_generic(args.id, "status", "in-progress")

if args.function == "mark-done":
    update_task_generic(args.id, "status", "done")