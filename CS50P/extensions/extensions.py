# extensions.py
file_name = input("File name: ").strip().lower()
junk, dot, suffix = file_name.rpartition(".")

match suffix:
    case "gif" | "jpg" | "jpeg" | "png":
        print("image/" + suffix)
    case "pdf" | "zip":
        print("application/" + suffix)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")

