from app.bootstrap.runner import init_app


def main():
    init_app(
        config_path="./config.ini"
    )

    from app.cli import register_commands
    cli = register_commands()
    cli()

if __name__ == "__main__":
    main()
