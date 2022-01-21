from configutils import get_config


def main():
    config = get_config()
    print("Config retrieved:")
    print(config)


if __name__ == "__main__":
    main()
