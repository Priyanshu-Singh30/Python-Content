def htp_status(status):
    match status:
        case 200:
            return "ok"
        case 400:
            return "Not found"
        case 500:
            return "Internal server error"
        case _:
            "unknown status"
print(htp_status(500))

## Dictionary merge & update operators
##