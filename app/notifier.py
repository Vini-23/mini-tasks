from plyer import notification

def notify(message: str, type: str):
    icon = "yellow_" if type == "lembrete" else "red"
    time = 15 if type == "lembrete" else 30

    notification.notify(
        title=type,
        message=message,
        timeout=time,
        app_icon=f"img/{icon}bell.ico",
        toast=True,
    )
