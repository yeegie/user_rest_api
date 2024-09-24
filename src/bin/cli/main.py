from app.infrastructure.bootstrap.runner import init_app


def main():
    init_app(
        app_config_path="./config/app.yaml",
        database_config_path="./config/database.yaml",
        smtp_config_path="./config/smtp.yaml",
    )

    from app.cli import register_commands
    cli = register_commands()
    cli()

if __name__ == "__main__":
    main()
