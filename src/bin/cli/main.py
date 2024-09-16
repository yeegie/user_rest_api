from app.bootstrap.runner import init_app


if __name__ == "__main__":
    init_app()
    
    from bin.cli.main import register_commands
    cli = register_commands()
    cli()
